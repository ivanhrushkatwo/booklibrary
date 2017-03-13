from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.About.as_view(), name='about'),

    url(r'^basket$', views.basket, name="basket"),
    url(r'^add_to_basket/(?P<pk>\d+)$', views.add_to_basket, name="add_to_basket"),
    url(r'^clear_basket/$', views.clear_basket, name="clear_basket"),

    url(r'^search_category/(?P<pk>\d+)$', views.search_category, name="search_category"),

    url(r'^books/$', views.BookListView.as_view(), name='books'),

    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),

    url(r'^like_book/(?P<pk>\d+)$', views.like_book, name="like_book"),
    url(r'^dislike_book/(?P<pk>\d+)$', views.dislike_book, name="dislike_book"),

    url(r'^authors/', views.AuthorListView.as_view(), name="authors"),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name="author-detail"),
    url(r'^author_like/(?P<pk>\d+)$', views.like_author, name="like_author"),
]
