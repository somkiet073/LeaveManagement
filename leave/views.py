from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from leave.models import LeaveType, Leave
from leave.serializers import LeaveTypeSerializer, LeaveSerializer

# Create your views here.
def Home(self):
    return HttpResponse("<p>Hello Word</p>")

# Create your views here.
class LeaveTypeViewSet(viewsets.ModelViewSet):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer

class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer