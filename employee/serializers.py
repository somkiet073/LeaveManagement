from django.contrib.auth.models import User, Group
from employee.models import Department, Profile, AppoveGroup, Positions, Prename
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name', 'groups', 'date_joined', 'is_active')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class AppoveGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppoveGroup
        fields = ('url', 'user', 'create_time')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('url', 'name')

class PositionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Positions
        fields = ('url', 'name', 'is_active')

class PrenameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prename
        fields = ('url', 'name', 'is_active')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('url', 'prename', 'user', 'gender', 'department', 'status', 'position')