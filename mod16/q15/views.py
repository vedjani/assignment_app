from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q, Count
from .models import Author, Category, Publisher, Book, Borrower, Loan
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date, timedelta

# Create your views here.

def home15(request):
    # Get statistics
    total_books = Book.objects.count()
    available_books = Book.objects.filter(status='available').count()
    total_authors = Author.objects.count()
    active_loans = Loan.objects.filter(return_date__isnull=True).count()

    # Get recent books
    recent_books = Book.objects.order_by('-created_at')[:5]

    # Get popular categories
    popular_categories = Category.objects.annotate(
        book_count=Count('books')
    ).order_by('-book_count')[:6]

    context = {
        'total_books': total_books,
        'available_books': available_books,
        'total_authors': total_authors,
        'active_loans': active_loans,
        'recent_books': recent_books,
        'popular_categories': popular_categories,
    }

    return render(request, "index15.html", context)


def books_list(request):
    # Get filter parameters
    category_id = request.GET.get('category')
    status = request.GET.get('status')
    search = request.GET.get('search')

    # Start with all books
    books = Book.objects.select_related('publisher').prefetch_related('authors', 'categories')

    # Apply filters
    if category_id:
        books = books.filter(categories__id=category_id)

    if status:
        books = books.filter(status=status)

    if search:
        books = books.filter(
            Q(title__icontains=search) |
            Q(authors__first_name__icontains=search) |
            Q(authors__last_name__icontains=search) |
            Q(isbn__icontains=search)
        ).distinct()

    # Get all categories for filter dropdown
    categories = Category.objects.all()

    context = {
        'books': books,
        'categories': categories,
        'selected_category': category_id,
        'selected_status': status,
        'search_query': search,
    }

    return render(request, "books_list.html", context)


def book_detail(request, book_id):
    book = get_object_or_404(Book.objects.select_related('publisher').prefetch_related('authors', 'categories'), id=book_id)

    # Check if book is available for borrowing
    can_borrow = book.status == 'available' and book.stock_quantity > 0

    context = {
        'book': book,
        'can_borrow': can_borrow,
    }

    return render(request, "book_detail.html", context)


def authors_list(request):
    search = request.GET.get('search')

    authors = Author.objects.annotate(
        book_count=Count('books')
    ).order_by('-book_count')

    if search:
        authors = authors.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search)
        )

    context = {
        'authors': authors,
        'search_query': search,
    }

    return render(request, "authors_list.html", context)


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = author.books.select_related('publisher').order_by('-publication_date')

    context = {
        'author': author,
        'books': books,
    }

    return render(request, "author_detail.html", context)


def categories_list(request):
    categories = Category.objects.annotate(
        book_count=Count('books')
    ).order_by('-book_count')

    context = {
        'categories': categories,
    }

    return render(request, "categories_list.html", context)


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    books = category.books.select_related('publisher').prefetch_related('authors').order_by('-publication_date')

    context = {
        'category': category,
        'books': books,
    }

    return render(request, "category_detail.html", context)


@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Check if book is available
    if book.status != 'available' or book.stock_quantity <= 0:
        messages.error(request, "This book is not available for borrowing.")
        return redirect('book_detail', book_id=book_id)

    # Get or create borrower
    borrower, created = Borrower.objects.get_or_create(
        user=request.user,
        defaults={'phone': '', 'address': ''}
    )

    # Check if user already has this book on loan
    existing_loan = Loan.objects.filter(
        book=book,
        borrower=borrower,
        return_date__isnull=True
    ).exists()

    if existing_loan:
        messages.error(request, "You already have this book on loan.")
        return redirect('book_detail', book_id=book_id)

    # Create loan
    due_date = date.today() + timedelta(days=14)  # 2 weeks loan period
    loan = Loan.objects.create(
        book=book,
        borrower=borrower,
        due_date=due_date
    )

    # Update book status and stock
    book.stock_quantity -= 1
    if book.stock_quantity == 0:
        book.status = 'borrowed'
    book.save()

    messages.success(request, f"You have successfully borrowed '{book.title}'. Due date: {due_date}")
    return redirect('my_loans')


@login_required
def my_loans(request):
    borrower = get_object_or_404(Borrower, user=request.user)
    loans = Loan.objects.filter(borrower=borrower).select_related('book').order_by('-loan_date')

    # Calculate overdue loans
    today = date.today()
    overdue_loans = loans.filter(return_date__isnull=True, due_date__lt=today)

    context = {
        'loans': loans,
        'overdue_loans': overdue_loans,
    }

    return render(request, "my_loans.html", context)


@login_required
def return_book(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id, borrower__user=request.user)

    if loan.return_date is not None:
        messages.error(request, "This book has already been returned.")
        return redirect('my_loans')

    # Update loan
    loan.return_date = date.today()

    # Calculate fine if overdue
    if loan.return_date > loan.due_date:
        days_overdue = (loan.return_date - loan.due_date).days
        loan.fine_amount = days_overdue * 0.50  # $0.50 per day

    loan.save()

    # Update book stock and status
    loan.book.stock_quantity += 1
    if loan.book.stock_quantity > 0:
        loan.book.status = 'available'
    loan.book.save()

    messages.success(request, f"You have returned '{loan.book.title}'.")
    if loan.fine_amount > 0:
        messages.warning(request, f"Fine amount: ${loan.fine_amount}")

    return redirect('my_loans')
