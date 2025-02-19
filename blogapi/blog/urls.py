from django.urls import path
from .views import (
    BlogPostListCreateView, BlogPostDetailView,
    CommentCreateView, LikeCreateView,
    UserRegistrationView, UserLoginView
)

urlpatterns = [
    path('posts/', BlogPostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_id>/likes/', LikeCreateView.as_view(), name='like-create'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]