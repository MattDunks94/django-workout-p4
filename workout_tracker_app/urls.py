from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.WorkoutList.as_view(), name='home'),
    path('<slug:slug>', views.WorkoutDetail.as_view(), name='workout_detail'),
    path(
        '<slug:slug>/add', views.AddExerciseForm.as_view(), name='add_exercise'
        ),
]
