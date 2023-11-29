# serializers.py
from rest_framework import serializers
from .models import InvresultAbaAt

class InvresultAbaAtSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvresultAbaAt
        fields = '__all__'  # 或者列出你想要序列化的字段
