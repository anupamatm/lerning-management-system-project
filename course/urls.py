# courses/urls.py

from django.urls import path
from .views import add_course_to_batch, add_student_to_batch, create_batch, create_course, create_group, create_module, create_material, add_material_to_module, list_batches, list_courses, list_groups, update_batch, update_group

urlpatterns = [
    path('create/', create_course, name='create_course'),
    path('create_module/', create_module, name='create_module'),
    path('add_material_to_module/', add_material_to_module, name='add_material_to_module'),
    path('list/', list_courses, name='list_courses'),
    path('create_batch/', create_batch, name='create_batch'),
    path('update_batch/<int:batch_id>/', update_batch, name='update_batch'),
    path('create_group/', create_group, name='create_group'),
    path('update_group/<int:group_id>/', update_group, name='update_group'),
    path('list_batches/', list_batches, name='list_batches'),
    path('list_groups/', list_groups, name='list_groups'),
    path('add_student_to_batch/<int:batch_id>/', add_student_to_batch, name='add_student_to_batch'),
    path('add_course_to_batch/<int:batch_id>/', add_course_to_batch, name='add_course_to_batch'),
]

