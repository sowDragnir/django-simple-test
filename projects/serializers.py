from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('tittle','technology', 'description','start_date', 'created_at', 'end_date')
    read_only_fields = ('created_at',)
