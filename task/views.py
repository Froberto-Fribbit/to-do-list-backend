from django.shortcuts import render
from django.http import JsonResponse
from .models import Task


def get_all_tasks(request):
  tasks = []
  for task in Task.objects.all():
    tasks.append({
        "id": task.pk,
        "content_text": task.content_text,
    })
  return JsonResponse(data={"data": tasks}, safe=False)


def mark_task_as_done(request):
  pass


def delete_task(request):
  pass
