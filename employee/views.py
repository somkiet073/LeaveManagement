from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from employee.models import AppoveGroup, Department, Profile, Positions, Prename
from employee.serializers import GroupSerializer, UserSerializer, AppoveGroupSerializer
from employee.serializers import DepartmentSerializer, PositionsSerializer, PrenameSerializer, ProfileSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AppoveGroupViewSet(viewsets.ModelViewSet):
    queryset = AppoveGroup.objects.all()
    serializer_class = AppoveGroupSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PositionsViewSet(viewsets.ModelViewSet):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer

class PrenameViewSet(viewsets.ModelViewSet):
    queryset = Prename.objects.all()
    serializer_class = PrenameSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer