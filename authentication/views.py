# authentication/views.py

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

def get_tokens_for_user(user):
    """
    Generates and returns refresh and access tokens for a given user.
    """
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['POST'])
def admin_login(request):
    """
    Handles login for admin users.
    """
    return user_login(request, user_type='admin')

@api_view(['POST'])
def student_login(request):
    """
    Handles login for student users.
    """
    return user_login(request, user_type='student')

@api_view(['POST'])
def teacher_login(request):
    """
    Handles login for teacher users.
    """
    return user_login(request, user_type='teacher')

def user_login(request, user_type):
    """
    Authenticates the user and returns JWT tokens if the credentials are correct and the user type matches.
    """
    # Get the username and password from the request data
    username = request.data.get('username')
    password = request.data.get('password')
    
    # Authenticate the user
    user = authenticate(request, username=username, password=password)
    
    # Check if authentication was successful and if the user type matches
    if user and user.user_type == user_type:
        # Generate JWT tokens for the user
        tokens = get_tokens_for_user(user)
        return Response(tokens)
    
    # If authentication fails, return an error response
    return Response({'error': 'Invalid credentials or user type'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    """
    Returns the profile information of the authenticated user.
    """
    # Get the authenticated user from the request
    user = request.user
    
    # Prepare the user data to be returned
    user_data = {
        'username': user.username,
        'email': user.email,
        'user_type': user.user_type,
    }
    
    # Return the user data
    return Response(user_data)
