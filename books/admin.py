from django.contrib import admin
from .models import Book, Author, BookAuthor, BookReview


class BookAuthorInline(admin.TabularInline):
    model = BookAuthor
    extra = 1


class BookReviewInline(admin.TabularInline):
    model = BookReview
    extra = 0
    readonly_fields = ('user', 'stars_given', 'comment')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'description')
    search_fields = ('title', 'isbn')
    inlines = [BookAuthorInline, BookReviewInline]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('book', 'author')
    search_fields = ('book__title', 'author__first_name', 'author__last_name')


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'stars_given')
    list_filter = ('stars_given',)
    search_fields = ('book__title', 'user__username', 'comment')