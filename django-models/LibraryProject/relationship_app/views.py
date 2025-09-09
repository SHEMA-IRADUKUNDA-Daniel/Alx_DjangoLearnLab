from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    # ✅ Use namespaced template path
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ Namespaced path
    context_object_name = 'library'
