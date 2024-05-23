# courses/serializers.py

from rest_framework import serializers
from .models import Course, Module, Material, ModuleMaterial, Test, Question, Option, Enrollment, ModuleProgress, MaterialProgress, TestResult, AssignmentSubmission,Batch,Group

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

    def create(self, validated_data):
        module = Module.objects.create(**validated_data)
        return module

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
        
    

class ModuleMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleMaterial
        fields = '__all__'

    def create(self, validated_data):
        module_material = ModuleMaterial.objects.create(**validated_data)
        return module_material

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class ModuleProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleProgress
        fields = '__all__'

class MaterialProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialProgress
        fields = '__all__'

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'

class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = '__all__'
