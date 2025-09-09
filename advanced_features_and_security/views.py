# advanced_features_and_security/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Article

@permission_required('advanced_features_and_security.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})

@permission_required('advanced_features_and_security.can_create', raise_exception=True)
def article_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Article.objects.create(title=title, content=content, author=request.user)
        return redirect('article_list')
    return render(request, 'articles/create.html')

@permission_required('advanced_features_and_security.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return redirect('article_list')
    return render(request, 'articles/edit.html', {'article': article})

@permission_required('advanced_features_and_security.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('article_list')
    return render(request, 'articles/delete.html', {'article': article})
