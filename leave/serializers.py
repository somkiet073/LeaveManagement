from leave.models import LeaveType, Leave
from rest_framework import serializers

class LeaveTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LeaveType
        fields = ('url', 'name', 'status', 'quota')

class LeaveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leave
        fields = ('url', 'leavetype', 'user', 'generated_time', 'start_time', 'end_time', 'period', 'leave_sum', 
        'letter_status', 'approved_by', 'approved_time', 'approved_status', 'checked_by', 'checked_time', 'checked_status', 'reply_note')