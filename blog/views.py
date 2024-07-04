from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post,Project,Comments
from .forms import CommentForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def home(request):
    context = {
       'projects': Project.objects.all()
    }
    return render(request, 'blog/home.html', context)
class ProjectListView(ListView):
    model = Project
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-start_date']

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date', 'status', 'stakeholders']
     
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date', 'status', 'stakeholders']
     
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        project = self.get_object()
        if self.request.user == project.owner:
            return True
        return False
    
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'blog/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comments.objects.filter(project=self.object)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = self.object
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('project-detail', pk=self.object.pk)
        else:
            context = self.get_context_data(object=self.object)
            context['form'] = form
            return self.render_to_response(context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] 

class PostDetailView(DetailView):
    model = Post  
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
     
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
     
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


