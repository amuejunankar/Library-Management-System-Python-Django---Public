from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book , BorrowedBook , Wishlist , BookRequest
from django.contrib.auth.decorators import login_required



def index(request):
    
    all_books = list(Book.objects.all()) # Get list oof all books
    best_books = random.sample(all_books, min(5, len(all_books))) # Select 5 random books
    
    context = {
        'best_books': best_books
    }
    
    return render(request, 'library/index.html', context)





@login_required
def my_books(request):
    borrowed_books = BorrowedBook.objects.filter(borrower=request.user).select_related('book', 'book__author')
    
    context = {
        'borrowed_books': borrowed_books
    }
    
    return render(request, 'library/my_books.html', context)










@login_required(login_url='../../login')
def add_to_wishlist(request, pk):
    book = get_object_or_404(Book, id=pk)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, book=book)
    return redirect('wishlist')



@login_required(login_url='../../login')
def remove_from_wishlist(request, pk):
    book = get_object_or_404(Book, id=pk)  
    wishlist = Wishlist.objects.filter(user=request.user, book=book)
    wishlist.delete()
    return redirect('wishlist')



@login_required(login_url="../../login")
def wishlist(request):
    search_query = request.POST.get('search_query')
    search_type = request.POST.get('search_type')
    sort_option = request.POST.get('sort')

    books = Book.objects.filter(wishlist__user=request.user)

    if search_query and search_type:
        if search_type == 'book':
            books = books.filter(title__icontains=search_query)
        elif search_type == 'author':
            books = books.filter(author__name__icontains=search_query)
    
    # Sorting books
    if sort_option:
        if sort_option == 'name_asc':
            books = books.order_by('title')
        elif sort_option == 'name_desc':
            books = books.order_by('-title')
        elif sort_option == 'published_year_desc':
            books = books.order_by('-published_year')

    return render(request, 'library/wishlist.html', {'books': books, 'search_query': search_query})




from django.shortcuts import render
from .models import Book

# def book_list(request):
#     search_query = request.POST.get('search_query')
#     search_type = request.POST.get('search_type')
#     sort_option = request.POST.get('sort')
#     language = request.POST.get('language')
#     genre = request.POST.get('genre')
#     category = request.POST.get('category')
#     age_group = request.POST.get('age_group')

#     books = Book.objects.all()

#     if search_query and search_type:
#         if search_type == 'book':
#             books = books.filter(title__icontains=search_query)
#         elif search_type == 'author':
#             books = books.filter(author__name__icontains=search_query)

#     if language:
#         books = books.filter(language=language)

#     if genre:
#         books = books.filter(genre=genre)

#     if category:
#         books = books.filter(category=category)

#     if age_group:
#         books = books.filter(age_group=age_group)

#     if sort_option:
#         if sort_option == 'name_asc':
#             books = books.order_by('title')
#         elif sort_option == 'name_desc':
#             books = books.order_by('-title')
#         elif sort_option == 'published_year_desc':
#             books = books.order_by('-published_year')

#     context = {
#         'books': books,
#         'search_query': search_query,
#         'selected_language': language,
#         'selected_genre': genre,
#         'selected_category': category,
#         'selected_age_group': age_group,
#         'selected_sort': sort_option,
#     }

#     return render(request, 'library/book_list.html', context)




# def book_list(request):
    
#     search_query = ''
#     search_type = ''
#     sort_option = ''
#     language = ''
#     genre = ''
#     category = ''
#     age_group = ''

#     # Check if it's a POST request (from the filter form)
#     if request.method == 'POST':
#         search_query = request.POST.get('search_query')
#         search_type = request.POST.get('search_type')
#         sort_option = request.POST.get('sort')
#         language = request.POST.get('language')
#         genre = request.POST.get('genre')
#         category = request.POST.get('category')
#         age_group = request.POST.get('age_group')
        
#     # Check if it's a GET request (from feature category links)
#     elif request.method == 'GET':
#         genre = request.GET.get('genre')
#         sort_option = request.GET.get('sort')
#         language = request.GET.get('language')
#         category = request.GET.get('category')
#         age_group = request.GET.get('age_group')

#     books = Book.objects.all()

#     if search_query and search_type:
#         if search_type == 'book':
#             books = books.filter(title__icontains=search_query)
#         elif search_type == 'author':
#             books = books.filter(author__name__icontains=search_query)

#     if language:
#         books = books.filter(language=language)

#     if genre:
#         books = books.filter(genre=genre)

#     if category:
#         books = books.filter(category=category)

#     if age_group:
#         books = books.filter(age_group=age_group)

#     if sort_option:
#         if sort_option == 'name_asc':
#             books = books.order_by('title')
#         elif sort_option == 'name_desc':
#             books = books.order_by('-title')
#         elif sort_option == 'published_year_desc':
#             books = books.order_by('-published_year')

#     context = {
#         'books': books,
#         'search_query': search_query,
#         'selected_language': language,
#         'selected_genre': genre,
#         'selected_category': category,
#         'selected_age_group': age_group,
#         'selected_sort': sort_option,
#     }

#     return render(request, 'library/book_list.html', context)




def book_list(request):
    search_query = ''
    search_type = ''
    sort_option = ''
    language = ''
    genre = ''
    category = ''
    age_group = ''

    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')
        search_type = request.POST.get('search_type', '')
        sort_option = request.POST.get('sort', '')
        language = request.POST.get('language', '')
        genre = request.POST.get('genre', '')
        category = request.POST.get('category', '')
        age_group = request.POST.get('age_group', '')
    elif request.method == 'GET':
        search_query = request.GET.get('search_query', '')
        search_type = request.GET.get('search_type', '')
        sort_option = request.GET.get('sort', '')
        language = request.GET.get('language', '')
        genre = request.GET.get('genre', '')
        category = request.GET.get('category', '')
        age_group = request.GET.get('age_group', '')

    books = Book.objects.all()

    if search_query and search_type:
        if search_type == 'book':
            books = books.filter(title__icontains=search_query)
        elif search_type == 'author':
            books = books.filter(author__name__icontains=search_query)

    if language:
        books = books.filter(language=language)

    if genre:
        books = books.filter(genre=genre)

    if category:
        books = books.filter(category=category)

    if age_group:
        books = books.filter(age_group=age_group)

    if sort_option:
        if sort_option == 'name_asc':
            books = books.order_by('title')
        elif sort_option == 'name_desc':
            books = books.order_by('-title')
        elif sort_option == 'published_year_desc':
            books = books.order_by('-published_year')

    context = {
        'books': books,
        'search_query': search_query,
        'selected_language': language,
        'selected_genre': genre,
        'selected_category': category,
        'selected_age_group': age_group,
        'selected_sort': sort_option,
    }

    return render(request, 'library/book_list.html', context)




def book_detail(request, pk):
    # Logic to retrieve and display details of a specific book
    book = Book.objects.get(pk=pk)  # Assuming Book is your model
    return render(request, 'library/book_detail.html', {'book': book})

from datetime import datetime, timedelta

@login_required(login_url="../../login")
def borrow_book(request, pk):
    if request.method == 'POST':
        issueDate = request.POST.get('issue-date')
        returnDate = request.POST.get('return-date')

        if issueDate and returnDate:  # Ensure both dates are provided
            book = Book.objects.get(pk=pk)
            borrower = request.user  # Assuming the user is authenticated

            # Convert date strings to datetime objects
            issue_date = datetime.strptime(issueDate, '%Y-%m-%d').date()
            return_date = datetime.strptime(returnDate, '%Y-%m-%d').date()

            # Create a new BorrowedBook instance
            borrowed_book = BorrowedBook.objects.create(
                book=book,
                borrower=borrower,
                borrowed_date=issue_date,
                due_date=return_date
            )
            
            if book.available_copies == 0:
                print("Copies Not available")
                redirect('book_list')
            else:
                book.available_copies -= 1
                book.save()

            return redirect('book_list')
        else:
            # Handle case where one or both dates are missing
            return HttpResponse("Please provide both issue date and return date.")
    else:
        book = Book.objects.get(pk=pk)
        return render(request, 'library/borrow_book.html', {'book': book})


@login_required(login_url="../../login")
def notify(request, pk):
    book = Book.objects.get(pk=pk)
    Logged_user = request.user 
    
    isthere = BookRequest.objects.filter(user=Logged_user, book=book)
    if isthere:
        return HttpResponse("You have already requested this book")
    else:
        book_request = BookRequest.objects.create(book=book, user=Logged_user)
        print("Book Added to DB")
        return redirect('book_list')
    return redirect('book_list')


@login_required(login_url="../../login")
def return_book(request, pk):
    if request.method == 'POST':
        # Retrieve the borrowed book
        borrowed_book_id = request.POST.get('borrowed_book_id')
        borrowed_book = BorrowedBook.objects.get(id=borrowed_book_id)

        # Increase the availability of the book
        book = borrowed_book.book
        # +1 BOOK AND SAVE
        book.available_copies += 1
        book.save()
        
        # Send mail if the book's available copies become 1
        if book.available_copies == 1:
            entries = BookRequest.objects.filter(book=book, is_sent=False)
            for entry in entries:
                send_mail(
                    'Book Available Notification',
                    f'Dear {entry.user.username}, the book "{book.title}" you requested is now available.',
                    'LibraryPune@gmail.com',
                    [entry.user.email],  
                    fail_silently=False,
                )
                entry.is_sent = True
                entry.save()  
            
        # Remove the entry from BorrowedBook
        borrowed_book.delete()

        print("Book returned successfully")
        
        return redirect('user_profile') 

    else:
        borrowed_book = BorrowedBook.objects.get(pk=pk)
        
        return render(request, 'library/return_book.html', { 'borrowed_book': borrowed_book })

# -----------------------------------------------------------------------------

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib import messages


# @login_required(login_url="../../login")
# def user_profile(request):
#     if request.method == 'POST':
#         form_type = request.POST.get('form_type')

#         if form_type == 'change_password':
#             old_password = request.POST['old_password']
#             new_password1 = request.POST['new_password1']
#             new_password2 = request.POST['new_password2']

#             # Check if the old password is correct
#             if not check_password(old_password, request.user.password):
#                 messages.error(request, 'Your old password was entered incorrectly. Please enter it again.')
#                 return redirect('user_profile')

#             if new_password1 != new_password2:
#                 messages.error(request, 'The new passwords do not match. Please enter them again.')
#                 return redirect('user_profile')

#             user = request.user
#             user.set_password(new_password1) 
#             user.save()

#             # Update the session to prevent the user from being logged out
#             update_session_auth_hash(request, user)

#             # Inform the user that the password was changed successfully
#             messages.success(request, 'Your password was changed successfully.')
#             return redirect('user_profile')

#         elif form_type == 'delete_account':
#             confirm_delete = request.POST['confirm_delete']

#             if confirm_delete == "DELETE":
#                 user = request.user
#                 user.delete()
#                 messages.success(request, 'Your account has been deleted successfully.')
#                 return redirect('index')
#             else:
#                 messages.error(request, 'You need to type "DELETE" to confirm account deletion.')
#                 return redirect('user_profile')

#         elif form_type == 'raise_issue':
#             issue_description = request.POST['issue_description']
#             messages.success(request, 'Your issue has been submitted successfully.')
#             print("HANDLE RAISE ISSUE")
#             return redirect('user_profile')

#     borrowed_books = BorrowedBook.objects.filter(borrower=request.user)
#     return render(request, 'library/profile.html', {'borrowed_books': borrowed_books})




@login_required(login_url="../../login")
def user_profile(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'change_password':
            old_password = request.POST['old_password']
            new_password1 = request.POST['new_password1']
            new_password2 = request.POST['new_password2']

            if not check_password(old_password, request.user.password):
                messages.error(request, 'Your old password was entered incorrectly. Please enter it again.')
                return redirect('user_profile')

            if new_password1 != new_password2:
                messages.error(request, 'The new passwords do not match. Please enter them again.')
                return redirect('user_profile')

            user = request.user
            user.set_password(new_password1) 
            user.save()

            update_session_auth_hash(request, user)

            messages.success(request, 'Your password was changed successfully.')
            return redirect('user_profile')

        elif form_type == 'delete_account':
            confirm_delete = request.POST['confirm_delete']

            if confirm_delete == "DELETE":
                user = request.user
                user.delete()
                messages.success(request, 'Your account has been deleted successfully.')
                return redirect('index')
            else:
                messages.error(request, 'You need to type "DELETE" to confirm account deletion.')
                return redirect('user_profile')

        elif form_type == 'raise_issue':
            issue_description = request.POST['issue_description']
            # Here you would typically save the issue to the database
            # For example: Issue.objects.create(user=request.user, description=issue_description)
            messages.success(request, 'Your issue has been submitted successfully.')
            return redirect('user_profile')

    return render(request, 'library/profile.html')

# --------------------** LOGIN AND SIGNUP **-------------------------
 
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'library/login.html')

def user_logout(request):
    logout(request)
    return redirect('index')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Storeing data in session
        request.session['username'] = username
        request.session['email'] = email
        request.session['password'] = password
        
        
        # Check username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'library/signup.html', {'error': 'Username is already taken'})
        else:
            otp = generate_otp()
            request.session['session_otp'] = otp  # Store OTP in session
            send_mail("OTP", otp, 'junankgg@gmail.com', [email], fail_silently=True)
            return redirect('signupOTP') 
    else:
        request.session.flush()
        return render(request, 'library/signup.html')
 
# -----------------------------------< Email > ---------------------

def signupOTP(request):
    if request.method == 'POST':
        username = request.session.get('username')
        email = request.session.get('email')
        password = request.session.get('password')
        session_otp = request.session.get('session_otp')
        otp = request.POST['otp']
        
        if otp == session_otp:
            print("OTP MATCHED")
            user = User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(request, username=username, password=password)
            if user:
                request.session.flush()
                login(request, user)
                
                return redirect('index')
        else:
            request.session.flush() 
            return redirect('user_signup')
        
    return render(request, 'library/signupOTP.html')


# ---------------------------------- RESET PASSWORD -----------------------------------------------------------


def forgot_password(request):
    print("\n'Welcome in FORGOT PASSWORD'")
    # Check if user is already in the process of resetting password
    if request.session.get('password_reset_state') != 'forgot_password':
        # Clear session data to start a new password reset process
        request.session.flush()
        # Set session state to indicate that user is in the forgot password process
        request.session['password_reset_state'] = 'forgot_password'
        
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = generate_otp()
        subject = 'Password Reset OTP'
        html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Password Reset OTP</title>
                <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap">
                <style>
                    body {{
                        font-family: 'Roboto', sans-serif;
                        background-color: #f4f4f4;
                        margin: 0;
                        padding: 0;
                    }}
                    .container {{
                        max-width: 500px;
                        margin: 50px auto;
                        padding: 20px;
                        background-color: #ffffff;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }}
                    h1 {{
                        text-align: center;
                        color: #333333;
                        margin-bottom: 20px;
                    }}
                    .otp-container {{
                        background-color: #007bff;
                        color: #ffffff;
                        padding: 20px;
                        border-radius: 5px;
                        text-align: center;
                        margin-bottom: 20px;
                    }}
                    .otp-container p {{
                        margin: 0;
                        font-size: 18px;
                    }}
                    .info {{
                        background-color: #f0f0f0;
                        padding: 15px;
                        border-radius: 5px;
                        margin-bottom: 20px;
                    }}
                    .info p {{
                        margin: 0;
                        font-size: 14px;
                        color: #555555;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Password Reset OTP</h1>
                    <div class="otp-container">
                        <p>Your One Time Password (OTP) for password reset is: <strong>{otp}</strong></p>
                    </div>
                    <div class="info">
                        <p>Important: This OTP is valid for a single use only. Please do not share it with anyone.</p>
                    </div>
                </div>
            </body>
            </html>
        """
        to_emails = [email]

        send_mail(subject, '', settings.EMAIL_HOST_USER, to_emails, html_message=html_content)

        # Store email and OTP in session for verification
        request.session['reset_email'] = email
        request.session['reset_otp'] = otp
        
        return redirect('otp_verification')
        
    # where user enter their email and otp will be sent to his email
    return render(request, 'library/password/forgot_password.html')

def otp_verification(request):
    print("Welcome in OTP VERIFY")
    
    if request.session.get('password_reset_state') == 'forgot_password':
       
        if request.method == 'POST':
            reset_otp = request.session.get('reset_otp')
            otp = request.POST.get('otp')

            if otp == reset_otp:
                # Set session state to indicate that user is in the OTP verification process
                request.session['password_reset_state'] = 'otp_verification'
                return redirect('reset_password')
            else:
                messages.error(request, 'Invalid OTP. Please try again.')
                return redirect('forgot_password')
        
        else:
            return render(request, 'library/password/otp_verification.html')
    else:
        # Clear session data if the state is not properly set
        request.session.flush()
        return redirect('forgot_password')  # Redirect if user didn't access this page after forgot_password

def reset_password(request):
    print("Welcome in RESET PASSWORD")
    # Check if user accessed this page after otp_verification
    if request.session.get('password_reset_state') == 'otp_verification':
        # Check if new password is submitted and update password
        if request.method == 'POST':
            reset_email = request.session.get('reset_email')
            p1 = request.POST.get('password1')
            p2 = request.POST.get('password2')
            
            if p1 == p2:
                # Retrieve the user using get() instead of filter()
                try:
                    user = User.objects.get(email=reset_email)
                    user.set_password(p1)
                    user.save()
                    
                    # Add success message
                    messages.success(request, 'Password successfully changed!')
                    
                    # Clear session data
                    request.session.flush()
                    print("password changes successful")
                    return redirect('user_login')
                except User.DoesNotExist:
                    # Add error message if user does not exist
                    messages.error(request, 'No user found with this email address.')
            else:
                # Add error message if passwords don't match
                messages.error(request, "Passwords don't match. Please try again.")
        
        
        return render(request, 'library/password/reset_password.html')
    else:
        # Clear session data if the state is not properly set
        request.session.flush()
        return redirect('forgot_password')  # Redirect if user didn't access this page after otp_verification

# ------------------------ EMAIL -----------------------------

import random
import string
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

def generate_otp(length=4):
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

# ============================================================


# ---------------------------------* DUMP AREA *----------------------------------------------------------------------------------------

# def user_account(request):
#     # Retrieve all borrowed books for the current user
#     borrowed_books = BorrowedBook.objects.filter(borrower=request.user)
#     return render(request, 'library/user_account.html', {'borrowed_books': borrowed_books})


# def user_profile(request):
#     if request.user.is_authenticated:
#         borrowed_books = BorrowedBook.objects.filter(borrower=request.user)
#         return render(request, 'library/profile.html', {'borrowed_books': borrowed_books})



