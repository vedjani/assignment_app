from django.urls import path
from . import views

urlpatterns = [
    path("", views.home15, name="q15_home"),
    path("books/", views.books_list, name="books_list"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),
    path("authors/", views.authors_list, name="authors_list"),
    path("authors/<int:author_id>/", views.author_detail, name="author_detail"),
    path("categories/", views.categories_list, name="categories_list"),
    path("categories/<int:category_id>/", views.category_detail, name="category_detail"),
    path("borrow/<int:book_id>/", views.borrow_book, name="borrow_book"),
    path("my-loans/", views.my_loans, name="my_loans"),
    path("return/<int:loan_id>/", views.return_book, name="return_book"),
]
