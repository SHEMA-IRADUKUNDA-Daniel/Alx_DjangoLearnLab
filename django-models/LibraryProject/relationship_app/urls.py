from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, register  # register view needs to exist in views.py

urlpatterns = [
    # Function-based view for listing books
    path('books/', list_books, name='list_books'),

    # Class-based view for library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views
    path('register/', register, name='register'),  # FBV for user registration
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
