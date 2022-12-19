from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('submit_marks/',views.mark_form, name='form'),
    path('view_marks/',views.mark_view, name='view'),
    path('edit/<int:id>', views.markedit, name="edit"),
    path('delete/<int:id>', views.delete, name="del"),
    path('update/<int:id>', views.update, name="update"),
    path('view_student/',views.view_student, name="view_single")
]
