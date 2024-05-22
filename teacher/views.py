# teacher/views.py

from django.core.mail import send_mail
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher
from .serializers import CreateTeacherSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_teacher(request):
    if request.user.user_type != 'admin':
        return Response({'error': 'Only admins can create teachers.'}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = CreateTeacherSerializer(data=request.data)
    if serializer.is_valid():
        teacher = serializer.save()
        password = request.data['password']
        # password = teacher.password
        send_mail(
            'anupamaunni612@gmail.com',
            f'Username: {teacher.user.username}\nPassword: {password}',
            'from@example.com',
            [teacher.user.email],
            fail_silently=False,
        )
        return Response({'success': 'Teacher created and credentials sent via email.'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
