from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('sent/', views.sent_messages, name='sent_messages'),
    path('archived/', views.archived_messages, name='archived_messages'),
    path('compose/', views.compose_message, name='compose_message'),
    path('archive/<int:message_id>/', views.archive_message, name='archive_message'),
    path('unarchive/<int:message_id>/', views.unarchive_message, name='unarchive_message'),
]