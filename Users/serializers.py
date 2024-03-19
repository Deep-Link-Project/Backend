from rest_framework import serializers
from .models import *

### Home-Account inforamtion feature
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'