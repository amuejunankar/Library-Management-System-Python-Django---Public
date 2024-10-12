from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('borrow/<int:pk>/', views.borrow_book, name='borrow_book'),
    path('return/<int:pk>', views.return_book, name='return_book'),
    path('my_books/', views.my_books, name='my_books'),
    
    
    # path('user_account/', views.user_account, name='user_account'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='user_signup'),
    path('login/', views.user_login, name='user_login'),
    path('signupOTP/', views.signupOTP, name='signupOTP'),
    
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:pk>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:pk>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('notify/<int:pk>', views.notify, name='notify'),
    
]


urlpatterns += [
    path("forgot_password", views.forgot_password, name="forgot_password"),
    path("otp_verification", views.otp_verification, name="otp_verification"),
    path("reset_password", views.reset_password, name="reset_password"),

]


