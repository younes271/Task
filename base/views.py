from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .models import Task
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
# Create your views here.




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = UserCreationForm()
    return render(request, 'base/signup.html', {'form': form})
    
    
    



class Tasklist(LoginRequiredMixin, ListView):
    model=Task
    context_object_name='tasks'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['tasks']=context['tasks'].filter(user=self.request.user)
        context['count']=context['tasks'].filter(complete=False).count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'].filter(title_icontains=search_input)
        return context



class TaskDetail(LoginRequiredMixin, DetailView):
    model=Task
    context_object_name='task'
    template_name='base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model=Task
    fields= ['title','description','complete']
    template_name='base/task-create.html'
    success_url=reverse_lazy('tasks')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class Taskupdate(LoginRequiredMixin, UpdateView):
    model=Task
    fields=['title','description','complete']
    template_name='base/task-update.html'
    success_url=reverse_lazy('tasks')

class Taskdelete(LoginRequiredMixin, DeleteView):
    model=Task
    template_name='base/task-delete.html'
    context_object_name='task'
    success_url=reverse_lazy('tasks')






