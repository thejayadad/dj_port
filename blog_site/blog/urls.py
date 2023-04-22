
from django.urls import path
from blog import views

urlpatterns = [
    path("about/", views.AboutView.as_view(), name='about'),
    path("", views.AboutView.as_view(), name='about'),
    path("post/(?P<pk>\d+)S", views.PostDetailView.as_view(), name='post_detail'),
    path("post/new", views.CreatePostView.as_view(), name='post_new'),
    path("post/(?P<pk>\d+)S/edit/$", views.PostUpdateView.as_view(), name='post_edit')
]