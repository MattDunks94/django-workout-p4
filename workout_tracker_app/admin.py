from django.contrib import admin
from .models import WorkoutPost, Exercise, Comment


@admin.register(WorkoutPost)
class WorkoutPostAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ('title',)}
    list_filter = ('created_on', 'updated_on')
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'author']


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):

    list_display = ('name', 'sets', 'reps', 'workout')
    list_filter = ('created_on', 'updated_on')
    search_fields = ['name', 'workout']
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'workoutPost', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)