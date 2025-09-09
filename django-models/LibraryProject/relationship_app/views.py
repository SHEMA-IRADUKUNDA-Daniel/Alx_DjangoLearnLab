from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
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
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # Redirect after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})