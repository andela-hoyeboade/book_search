from books import views
from django.conf.urls import url

urlpatterns = [
    url(r'^', views.BookListView.as_view(), name='book_list')
]
