from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.About.as_view(), name='about'),
    url(r'^registration$', views.RegistrationView.as_view(), name="registration"),

    url(r'^search_category/(?P<pk>\d+)&/&', views.search_category, name="search_category"),

    url(r'^books/$', views.BookListView.as_view(), name='books'),

    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/', views.AuthorListView.as_view(), name="authors"),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name="author-detail")
]

urlpatterns += [
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]

urlpatterns += [
    url(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    url(r'^book/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book_delete'),
    url(r'^book/(?P<pk>\d+)/update/$', views.BookUpdate.as_view(), name='book_update'),
]
