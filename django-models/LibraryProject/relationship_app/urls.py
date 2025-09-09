from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('books/', list_books, name='list_books'),  # FBV
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # CBV
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # Include the app’s URLs
]