from . import views
from django.urls import path
from .views import AddPostView, EditPostView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('<int:pk>/<post_slug>/',
         views.CommentDeleteView.as_view(), name='comment_delete'),
    path('add_post.html/', views.AddPostView.as_view(), name='add_post'),
    path('update/<slug:slug>',
         views.EditPostView.as_view(), name='update_post'),
]
