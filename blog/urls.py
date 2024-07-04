from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDetailView,
)
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', ProjectListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('project/update/<int:pk>/', views.ProjectUpdateView.as_view(), name='project-update'),
    path('about/', views.about, name='blog-about'),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='users/password_reset.html'
        ),
        name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]

