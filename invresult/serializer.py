# serializers.py
from rest_framework import serializers

class GenericInvresultSerializer(serializers.ModelSerializer):
    class Meta:
        model = None  # 将在实例化时指定
        fields = '__all__'  # 或者列出你想要序列化的字段
