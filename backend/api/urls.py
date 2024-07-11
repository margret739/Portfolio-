from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    UserCreateView, UserListView, UserDetailView, UserUpdateView, UserDeleteView, ProfileCreateView,
    ProfileHideView, ProfileListView, ProfileDetailView, ProfileUpdateView, ProfileDeleteView,
    StoryCreateView, StoryDetailView, StoryUpdateView, StoryDeleteView,
    CommentCreateView, CommentDetailView, CommentUpdateView, CommentDeleteView
)


urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('user/', UserListView.as_view(), name='list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('users/<int:pk>/', UserUpdateView.as_view(), name='update'),
    path('users/<int:pk>/', UserDeleteView.as_view(), name='delete'),
    
    # urls for profile
    path('profiles/', ProfileCreateView.as_view(), name='create profile'),
    path('profiles/', ProfileListView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profiles/<int:pk>/', ProfileUpdateView.as_view(), name='Update-profile'),
    path('profiles/<int:pk>/', ProfileDeleteView.as_view(), name='profile-delete'),
    path('profiles/<int:pk>/', ProfileHideView.as_view(), name='profile-hide'),

    # story urls
    path('stories/', StoryCreateView.as_view(), name='story-create'),
    path('stories/<int:pk>/', StoryDetailView.as_view(), name='story-detail'),
    path('stories/<int:pk>/', StoryUpdateView.as_view(), name='story-update'),
    path('stories/<int:pk>/', StoryDeleteView.as_view(), name='story-delete'),

    # comment urls
    path('comments/', CommentCreateView.as_view(), name='create-comment'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('comments/<int:pk>/', CommentDeleteView.as_view(), name='delete-comment'),
    path('comments/<int:pk>/', CommentUpdateView.as_view(), name='update-comment'),
]