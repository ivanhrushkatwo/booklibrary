from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.About.as_view(), name='about'),
    url(r'^contact$', views.contact, name='contacts'),
    url(r'^send_email_to_admin/$', views.send_email_to_admin, name='send_email_to_admin'),


    url(r'^delete_from_basket/$', views.delete_from_basket, name="delete_from_basket"),
    url(r'^basket$', views.basket, name="basket"),
    url(r'add_to_basket/(?P<pk>\d+)$', views.add_to_basket, name="add_to_basket"),
    url(r'delete_one_book_from_basket/(?P<pk>\d+)$', views.delete_one_book_from_basket, name="delete_one_book_from_basket"),


    url(r'^clear_basket/$', views.clear_basket, name="clear_basket"),

    url(r'^search/$', views.search, name="search"),
    url(r'^search_category/(?P<pk>\d+)$', views.search_category, name="search_category"),

    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),

    url(r'^download_sample/(?P<pk>\d+)$', views.download_sample, name='download_sample'),

    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name="author-detail"),
]
