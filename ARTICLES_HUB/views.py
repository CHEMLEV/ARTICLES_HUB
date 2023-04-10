from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import ArticleCategory, ArticleType, Article
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from .filters import ArticleFilter
from . import views
from django.contrib.auth import logout
from django.shortcuts import redirect


def HomePageView(request):
    return render (request, 'home.html') 


def register(request):
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                 form.save()
                 username = form.cleaned_data.get('username')
                 return redirect('login')
        else:
            form = NewUserForm()

        return render(request,'register.html',{'form':form})


def article_filter_list(request):
    
    articles = Article.objects.all()

    articleFilter = ArticleFilter(queryset=articles)

    if request.method == "POST":
        articleFilter = ArticleFilter(request.POST, queryset=articles)

    context = {
        'articleFilter': articleFilter
    }

    return render(request, 'article_list.html', context)

# Articles
class ArticlesListView(ListView):
    model = Article
    template_name = "article_list.html"

    def get(self, request, *args, **kwargs):
        view = views.article_filter_list
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = views.article_filter_list
        return view(request, *args, **kwargs)

class ArticleDetailsView(DetailView): 
    model = Article
    template_name = "article_detail.html"

class ArticleCreateView(LoginRequiredMixin, CreateView):  # new 
    model = Article
    template_name = "article_new.html"
    fields = ("type_id", "category_id", "article_name", "year_of_born", "year_of_died", "nationality", "notable_work", "article_about", "known_for", "article_year", "medium", "dimensions", "location", "designed", "developer")
    success_url = reverse_lazy('article_list')


class ArticleUpdateView(UpdateView): #LoginRequiredMixin, UserPassesTestMixin, 
    model = Article
    fields = (
        "type_id", "category_id", "article_name", "year_of_born", "year_of_died", "nationality", "notable_work", "article_about", "known_for", "article_year", "medium", "dimensions", "location", "designed", "developer"
    )
    template_name = "article_edit.html"
    success_url = reverse_lazy('article_list')

    def test_func(self):  # new
        obj = self.get_object()
        return obj.developer == self.request.user


class ArticleDeleteView(DeleteView): #LoginRequiredMixin, UserPassesTestMixin, 
    model = Article
    fields = (
        "article_name",
        "article_about",
    )
    template_name = "article_delete.html"
    success_url = reverse_lazy('article_list')

    def test_func(self):  # new
        obj = self.get_object()
        return obj.developer == self.request.user
