from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from .models import WorkoutPost, Exercise
from .forms import ExerciseForm


class WorkoutList(generic.ListView):
    model = WorkoutPost
    queryset = WorkoutPost.objects.all()
    context_object_name = 'workout'
    template_name = 'index.html'


class ExerciseList(generic.ListView):
    model = Exercise
    queryset = Exercise.objects.all()
    context_object_name = 'exercise'
    template_name = 'workout_detail.html'


class WorkoutDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = WorkoutPost.objects.all()
        workout = get_object_or_404(queryset, slug=slug)
        exercise = Exercise.objects.all()

        return render(request, 'workout_detail.html', {
            "workout": workout,
            "exercise": exercises,
            "exercise_form": ExerciseForm()
        },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = WorkoutPost.objects.all()
        workout = get_object_or_404(queryset, slug=slug)
        exercise = Exercise.objects.all()

        exercise_form = ExerciseForm(data=request.POST)
        if exercise_form.is_valid():
            exercise = exercise_form.save(commit=False)
            exercise.workout = workout
            exercise.save()
        else:
            exercise_form = ExerciseForm()

        return render(request, 'workout_detail.html', {
            "workout": workout,
            "exercise": exercises,
            "exercise_form": ExerciseForm()
        },
        )

