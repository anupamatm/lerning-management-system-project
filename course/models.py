# courses/models.py

from django.db import models
from authentication.models import CustomUser

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    prerequisites = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=[('Draft', 'Draft'), ('Published', 'Published')])
    
    def __str__(self):
        return self.course_name
    
class Batch(models.Model):
    batch_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('completed', 'Completed'), ('ongoing', 'Ongoing'), ('dropped', 'Dropped')])
    students = models.ManyToManyField(CustomUser, related_name='batches')
    courses = models.ManyToManyField(Course, related_name='batches')

class Group(models.Model):
    group_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    batches = models.ManyToManyField(Batch, related_name='groups')

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    module_name = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField()
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.module_name

class Material(models.Model):
    MATERIAL_TYPE_CHOICES = [
        ('learning_material', 'Learning Material'),
        ('assignment', 'Assignment'),
        ('test', 'Test'),
        ('interview_question', 'Interview Question')
    ]
    material_type = models.CharField(max_length=20, choices=MATERIAL_TYPE_CHOICES)
    material_title = models.CharField(max_length=100)
    material_url = models.URLField()
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.material_title

class ModuleMaterial(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='module_materials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='module_materials')
    material_category = models.CharField(max_length=20, choices=Material.MATERIAL_TYPE_CHOICES)

class Test(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='tests')
    test_title = models.CharField(max_length=100)
    test_description = models.TextField()
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.test_title

class Question(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('multiple_choice', 'Multiple Choice'),
        ('true_false', 'True/False'),
        ('short_answer', 'Short Answer')
    ]
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES)

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=255)
    is_correct = models.BooleanField()

class Enrollment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)

class ModuleProgress(models.Model):
    PROGRESS_STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='module_progresses')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='module_progresses')
    status = models.CharField(max_length=12, choices=PROGRESS_STATUS_CHOICES)
    completion_date = models.DateField(null=True, blank=True)

class MaterialProgress(models.Model):
    PROGRESS_STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='material_progresses')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='material_progresses')
    status = models.CharField(max_length=12, choices=PROGRESS_STATUS_CHOICES)
    completion_date = models.DateField(null=True, blank=True)

class TestResult(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='test_results')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='test_results')
    score = models.IntegerField()
    completion_date = models.DateField()

class AssignmentSubmission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assignment_submissions')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='assignment_submissions')
    submission_url = models.URLField()
    submission_date = models.DateField(auto_now_add=True)
    grade = models.IntegerField(null=True, blank=True)
