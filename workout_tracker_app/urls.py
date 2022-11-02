from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.WorkoutList.as_view(), name='home'),
    path(
        'create/', login_required(
            views.CreateExercise.as_view()
            ), name='create_exercise'
        ),
    path('exerciselist/', views.ExerciseList.as_view(), name='exercise_list')
]
