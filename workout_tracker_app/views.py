from django.shortcuts import render
from django.views import generic
from .models import WorkoutPost


class WorkoutList(generic.ListView):
    model = WorkoutPost
    queryset = WorkoutPost.objects.all().order_by('-created_on')
    template_name = "index.html"
