from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import todo_task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class Task_list(ListView):
    model = todo_task
    template_name = 'Home.html'
    context_object_name = 'key_task'

class Task_detail(DetailView):
    model = todo_task
    template_name = 'Detail.html'
    context_object_name = 'key_task'

class Task_Update(UpdateView):
    model = todo_task
    template_name = 'Updation.html'
    context_object_name = 'key_updt'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('GenericDetailView',kwargs = {'pk':self.object.id})

class Task_delete(DeleteView):
    model = todo_task
    template_name = 'Delete.html'
    success_url = reverse_lazy('GenericListView')

# Create your views here.
def basic(request):
    var_direct = todo_task.objects.all()
    if request.method == 'POST':
        var_name=request.POST.get('Task')
        var_priority = request.POST.get('Priority')
        var_date = request.POST.get('Date')
        todo_user = todo_task(name = var_name,priority = var_priority,date = var_date)
        todo_user.save()

    return render(request,'Home.html',{'key_task':var_direct})

def delete(request,task_id):
    task_del = todo_task.objects.get(id = task_id)
    if request.method == 'POST':
        task_del.delete()
        return redirect('/')
    return render(request,'Delete.html')

def update(request,id):
    task_updt = todo_task.objects.get(id = id)
    var_form = TodoForm(request.POST or None, instance = task_updt)
    if var_form.is_valid():
        var_form.save()
        return redirect('/')
    return render(request,'Update.html',{'key_form':var_form,'key_updt':task_updt})
