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
        exercises = workout.exercise.order_by('created_on')

        return render(request, 'workout_detail.html', {
            "workout": workout,
            "exercise": exercises,
        },
        )


class AddExerciseForm(generic.FormView):
    def add_exercise_form():
        form_class = ExerciseForm
        return render(request, 'add_exercise.html', {
            "exercise_form": ExerciseForm
        })
    