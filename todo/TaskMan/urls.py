from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import list_task, create_task, update_task, delete_task

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', list_task, name= "list_task"),
    path('new',create_task, name= "create_task"),
    path('update/<int:id>',update_task, name= "update_task"),
    path('delete/<int:id>', delete_task, name= "delete_task"),

]

