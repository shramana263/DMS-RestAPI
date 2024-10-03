from rest_framework import serializers
from ..models.Document import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Document
        fields=('file_name','original_name','path','extension','mime_type')
        
    def validate_file(self, value):
        return value