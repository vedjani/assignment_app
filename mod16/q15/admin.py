from django.contrib import admin
from django.db.models import Count, Q
from django.utils.html import format_html
from django.urls import reverse
from .models import Author, Category, Publisher, Book, Borrower, Loan

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_active', 'book_count', 'created_at')
    list_filter = ('is_active', 'created_at', 'birth_date')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('last_name', 'first_name')
    readonly_fields = ('created_at',)
    list_editable = ('is_active',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('first_name', 'last_name', 'email', 'birth_date')
        }),
        ('Additional Info', {
            'fields': ('bio', 'is_active'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Full Name'

    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Books Written'

    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, f"{queryset.count()} authors marked as active.")
    mark_as_active.short_description = "Mark selected authors as active"

    def mark_as_inactive(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, f"{queryset.count()} authors marked as inactive.")
    mark_as_inactive.short_description = "Mark selected authors as inactive"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'book_count', 'color_display', 'description_short')
    search_fields = ('name', 'description')
    ordering = ('name',)

    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Books in Category'

    def color_display(self, obj):
        return format_html('<div style="width: 20px; height: 20px; background-color: {}; border-radius: 50%;"></div>', obj.color)
    color_display.short_description = 'Color'

    def description_short(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    description_short.short_description = 'Description'


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'contact_email', 'book_count')
    search_fields = ('name', 'contact_email')
    ordering = ('name',)

    def book_count(self, obj):
        return obj.book_set.count()
    book_count.short_description = 'Published Books'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors', 'publisher', 'publication_date', 'status', 'price', 'stock_quantity')
    list_filter = ('status', 'publication_date', 'publisher', 'categories', 'authors')
    search_fields = ('title', 'isbn', 'authors__first_name', 'authors__last_name')
    ordering = ('-publication_date',)
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('status', 'stock_quantity')
    filter_horizontal = ('authors', 'categories')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'authors', 'publisher', 'isbn', 'publication_date')
        }),
        ('Content', {
            'fields': ('pages', 'description', 'cover_image'),
        }),
        ('Inventory', {
            'fields': ('price', 'status', 'stock_quantity'),
            'classes': ('collapse',)
        }),
        ('Categories', {
            'fields': ('categories',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_authors(self, obj):
        return ", ".join([f"{author.first_name} {author.last_name}" for author in obj.authors.all()])
    get_authors.short_description = 'Authors'

    actions = ['mark_as_available', 'mark_as_borrowed', 'update_stock']

    def mark_as_available(self, request, queryset):
        queryset.update(status='available')
        self.message_user(request, f"{queryset.count()} books marked as available.")
    mark_as_available.short_description = "Mark selected books as available"

    def mark_as_borrowed(self, request, queryset):
        queryset.update(status='borrowed')
        self.message_user(request, f"{queryset.count()} books marked as borrowed.")
    mark_as_borrowed.short_description = "Mark selected books as borrowed"

    def update_stock(self, request, queryset):
        # This would typically open a form, but for simplicity we'll just add 1 to stock
        for book in queryset:
            book.stock_quantity += 1
            book.save()
        self.message_user(request, f"Stock updated for {queryset.count()} books.")
    update_stock.short_description = "Increase stock by 1"


@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'username', 'phone', 'membership_date', 'is_active', 'loan_count')
    list_filter = ('is_active', 'membership_date')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'phone')
    ordering = ('user__last_name', 'user__first_name')
    readonly_fields = ('membership_date',)

    def get_full_name(self, obj):
        return obj.user.get_full_name() or obj.user.username
    get_full_name.short_description = 'Full Name'
    get_full_name.admin_order_field = 'user__last_name'

    def username(self, obj):
        return obj.user.username
    username.short_description = 'Username'

    def loan_count(self, obj):
        return obj.loan_set.count()
    loan_count.short_description = 'Active Loans'


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'borrower_name', 'loan_date', 'due_date', 'return_date', 'is_overdue_display', 'fine_amount')
    list_filter = ('loan_date', 'due_date', 'return_date', 'book__status')
    search_fields = ('book__title', 'borrower__user__username', 'borrower__user__first_name', 'borrower__user__last_name')
    ordering = ('-loan_date',)
    readonly_fields = ('loan_date',)
    list_editable = ('return_date', 'fine_amount')

    def book_title(self, obj):
        return obj.book.title
    book_title.short_description = 'Book'
    book_title.admin_order_field = 'book__title'

    def borrower_name(self, obj):
        return obj.borrower.user.get_full_name() or obj.borrower.user.username
    borrower_name.short_description = 'Borrower'
    borrower_name.admin_order_field = 'borrower__user__last_name'

    def is_overdue_display(self, obj):
        if obj.is_overdue():
            return format_html('<span style="color: red; font-weight: bold;">OVERDUE</span>')
        elif obj.return_date:
            return format_html('<span style="color: green;">Returned</span>')
        else:
            return format_html('<span style="color: orange;">Active</span>')
    is_overdue_display.short_description = 'Status'

    actions = ['mark_as_returned', 'calculate_fine']

    def mark_as_returned(self, request, queryset):
        from django.utils import timezone
        today = timezone.now().date()
        queryset.update(return_date=today)
        self.message_user(request, f"{queryset.count()} loans marked as returned.")
    mark_as_returned.short_description = "Mark selected loans as returned"

    def calculate_fine(self, request, queryset):
        # Simple fine calculation: $0.50 per day overdue
        from django.utils import timezone
        today = timezone.now().date()
        updated_count = 0
        for loan in queryset:
            if loan.return_date is None and today > loan.due_date:
                days_overdue = (today - loan.due_date).days
                fine = days_overdue * 0.50
                loan.fine_amount = fine
                loan.save()
                updated_count += 1
        self.message_user(request, f"Fines calculated for {updated_count} overdue loans.")
    calculate_fine.short_description = "Calculate fines for overdue loans"


# Custom admin site configuration
admin.site.site_header = "Library Management System"
admin.site.site_title = "Library Admin"
admin.site.index_title = "Welcome to Library Management"

