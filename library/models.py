
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    author_image = models.ImageField(upload_to='author_images/', null=True, blank=True)
    author_description = models.TextField(null=True, blank=True, default="")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Book(models.Model):
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('FR', 'French'),
        ('DE', 'German'),
        ('HI', 'Hindi'),
        ('TA', 'Tamil'),
    ]

    GENRE_CHOICES = [
        ('FIC', 'Fiction'),
        ('NF', 'Non-Fiction'),
        ('SCI', 'Science Fiction'),
        ('FAN', 'Fantasy'),
        ('MYST', 'Mystery'),
        ('ROM', 'Romance'),
        ('THR', 'Thriller'),
        ('BIO', 'Biography'),
        ('HIST', 'Historical'),
        ('HOR', 'Horror'),
    ]

    CATEGORY_CHOICES = [
        ('NOV', 'Novel'),
        ('BIO', 'Biography'),
        ('COM', 'Comics'),
        ('POE', 'Poetry'),
        ('DRA', 'Drama'),
        ('ART', 'Art'),
        ('SEL', 'Self-help'),
        ('CHI', 'Children'),
        ('YA', 'Young Adult'),
        ('ACA', 'Academic'),
    ]

    AGE_GROUP_CHOICES = [
        ('CH', 'Children'),
        ('YA', 'Young Adult'),
        ('AD', 'Adult'),
    ]

    title = models.CharField(max_length=200, null=False, blank=False, default="Untitled")
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=False)
    description = models.TextField(null=True, blank=True, default="")
    published_year = models.PositiveIntegerField(null=False, blank=False, default=timezone.now().year)
    available_copies = models.PositiveIntegerField(default=1)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='EN')
    number_of_pages = models.PositiveIntegerField(null=False, blank=False, default=1)
    genre = models.CharField(max_length=4, choices=GENRE_CHOICES, null=False, blank=False, default='FIC')
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, null=False, blank=False, default='NOV')
    age_group = models.CharField(max_length=2, choices=AGE_GROUP_CHOICES, null=False, blank=False, default='AD')
    isbn = models.CharField(max_length=13, unique=True, null=False, blank=False, default="0000000000000")
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    # New fields
    book_pdf = models.FileField(upload_to='book_pdfs/', null=True, blank=True)
    book_pdf_demo = models.FileField(upload_to='book_pdf_demos/', null=True, blank=True)
    audio_book = models.FileField(upload_to='audio_books/', null=True, blank=True)
    audio_book_demo = models.FileField(upload_to='audio_book_demos/', null=True, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    
    def __str__(self):
        return f"{self.book.title} - Borrowed by {self.borrower.username}"


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"


class BookRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_sent = models.BooleanField(default=False)
    email = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} requested by {self.user.username}"
