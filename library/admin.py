from django.contrib import admin
from django.utils.html import format_html
from .models import Author, Book, BorrowedBook, Wishlist, BookRequest

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year', 'available_copies', 'borrowed_count')
    list_filter = ('author', 'published_year')
    search_fields = ('title', 'author__name')

    def borrowed_count(self, obj):
        return obj.borrowedbook_set.count()
    borrowed_count.short_description = 'Borrowed Count'

class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower', 'borrowed_date', 'due_date', 'return_book_link')
    list_filter = ('borrowed_date', 'due_date')
    search_fields = ('book__title', 'borrower__username')

    def return_book_link(self, obj):
        try:
            if not getattr(obj, 'returned', False):
                return format_html('<a href="{}">Return Book</a>', f'/admin/library/borrowedbook/{obj.id}/change/')
            return "Returned"
        except AttributeError:
            return "Attribute 'returned' not found"
    return_book_link.short_description = 'Return'

    actions = ['mark_returned']

    def mark_returned(self, request, queryset):
        queryset.update(returned=True)
    mark_returned.short_description = 'Mark selected books as returned'

admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(BorrowedBook, BorrowedBookAdmin)
admin.site.register(Wishlist)
admin.site.register(BookRequest)
