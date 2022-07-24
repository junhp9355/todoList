from django.shortcuts import render

from article.forms import ArticleForm
from article.models import Article


def create_todo(request):

    lists = Article.objects.all()

    if request.method == 'GET':
        form = ArticleForm()
    return render(request, 'index.html', {
        "form" : form,
        "lists" : lists,
    })
    if request.method == 'POST':
        form = ArticleForm(request.POST)
       if form.is_valid():
           todo = form.save()
           return HttpResponseRedirect(reverse('create_todo'))
    else:
        form = ArticleForm()
    return render(request, 'index.html', {
        "form":form,
        "lists":lists,
    })