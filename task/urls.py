from django.urls import path
from .views import (
    get_all_tasks
)

app_name = 'task'

urlpatterns = [
    path('get-all/', get_all_tasks, name='get_all_tasks'),
]
