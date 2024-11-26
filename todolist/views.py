from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Task, Tag
from todolist.forms import TaskForm, TagForm


class TaskListView(generic.ListView):
    model = Task
    template_name = "todolist/task_list.html"
    context_object_name = "tasks"
    ordering = ["is_done", "-created_at"]


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist/task_create.html"
    success_url = reverse_lazy("todolist:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist/task_update.html"
    success_url = reverse_lazy("todolist:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todolist/task_delete.html"
    success_url = reverse_lazy("todolist:home")


class TaskToggleStatusView(generic.View):
    @staticmethod
    def post(request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("todolist:home")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todolist/tag_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todolist/tag_create.html"
    success_url = reverse_lazy("todolist:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todolist/tag_update.html"
    success_url = reverse_lazy("todolist:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todolist/tag_delete.html"
    success_url = reverse_lazy("todolist:tag_list")
