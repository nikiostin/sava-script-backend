from rest_framework import serializers
from base.models.Code import Code

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = '__all__'
