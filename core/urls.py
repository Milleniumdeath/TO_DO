
from django.contrib import admin
from django.urls import path

from todo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexViews.as_view(), name='home'),
    path('<int:pk>/', TaskUpdateViews.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),



]
