from django.shortcuts import render
from django.views import generic
from .models import WorkoutPost


class WorkoutList(generic.ListView):
    model = WorkoutPost
    queryset = WorkoutPost.objects.all()
    context_object_name = 'workout'
    template_name = 'index.html'
    paginate_by = 2
