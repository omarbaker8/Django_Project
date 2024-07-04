from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Message
from django.db.models import Q
from .forms import MessageForm  # We'll create this form

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user, is_archived=False).order_by('-timestamp')
    return render(request, 'messaging/inbox.html', {'messages': messages})

@login_required
def sent_messages(request):
    messages = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'messaging/sent_messages.html', {'messages': messages})

@login_required
def archived_messages(request):
    messages = Message.objects.filter(recipient=request.user, is_archived=True).order_by('-timestamp')
    return render(request, 'messaging/archived_messages.html', {'messages': messages})

@login_required
def compose_message(request):
    initial_recipient = request.GET.get('recipient', '')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, "Message sent successfully!")
            return redirect('inbox')
    else:
        form = MessageForm(initial={'recipient': initial_recipient})
    
    return render(request, 'messaging/compose.html', {'form': form})

@login_required
def archive_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, recipient=request.user)
    message.is_archived = True
    message.save()
    messages.success(request, "Message archived successfully!")
    return redirect('inbox')

@login_required
def unarchive_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, recipient=request.user)
    message.is_archived = False
    message.save()
    messages.success(request, "Message unarchived successfully!")
    return redirect('archived_messages')