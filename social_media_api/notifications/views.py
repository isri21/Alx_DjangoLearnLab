from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def notifications(request):
	user = request.user
	notifications = Notification.objects.filter(recipient=user, is_read=False)
	serialized = NotificationSerializer(notifications, many=True)

	return Response(serialized.data)