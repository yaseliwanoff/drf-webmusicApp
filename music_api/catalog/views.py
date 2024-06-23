from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from catalog.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This is API endpoint allow users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
