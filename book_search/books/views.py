from books.models import Book
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView


class BookListView(TemplateView):
    template_name = 'books/books.html'

    def get_context_data(self, **kwargs):
        query_string = self.request.GET.get('q', '')
        context = super(BookListView, self).get_context_data(**kwargs)
        context['query_string'] = query_string
        context['books'] = self.get_queryset()
        return context

    def get_queryset(self):
        query_string = self.request.GET.get('q', '')
        search_type = self.request.GET.get('search_type', '')

        if search_type == 'category':
            return Book.objects.filter(category__name__iexact=query_string)

        if search_type == 'title':
            return Book.objects.filter(title__icontains=query_string)

        return Book.objects.filter(Q(category__name__iexact=query_string) | Q(title__icontains=query_string))
