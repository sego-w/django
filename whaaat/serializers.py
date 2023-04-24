from rest_framework import serializers
from whaaat.models import File
# remember to import the File model

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
class SaveFileSerializer(serializers.Serializer):
    
    class Meta:
        model = File
        fields = "__all__"