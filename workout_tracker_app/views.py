from django.shortcuts import render
from django.views import generic
from .models import WorkoutPost, Exercise


class WorkoutList(generic.ListView):
    model = WorkoutPost
    queryset = WorkoutPost.objects.all()
    context_object_name = 'workout'
    template_name = 'index.html'


class CreateExercise(generic.CreateView):
    model = Exercise
    fields = ['name', 'sets', 'reps', 'weight']
    success_url = 'exercise_list.html'
    template_name = 'exercise_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ExerciseList(generic.ListView):
    model = Exercise
    queryset = Exercise.objects.all()
    context_object_name = 'exercise'
    template_name = 'exercise_list.html'