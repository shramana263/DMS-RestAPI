from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.DocumentSerializer import DocumentSerializer
from ..models.Document import Document
  # Import your Document model

# @login_required
class DocumentUploadView(APIView):
    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']

            # Save the file to your desired location (e.g., media directory)
            file_path = 'D:/dms_images/django'  # Replace with your desired path
            file_name = file.name  # Get the original file name
            file_extension = file.name.split('.')[-1]  # Extract the file extension

            # Create a new Document instance
            document = Document(
                file_name=file_name,
                original_name=file_name,
                path=file_path + file_name,
                extension=file_extension,
                mime_type=file.content_type,
                user=request.user  # Assuming you have authentication in place
            )
            document.save()

            # Save the file to the specified path
            with open(document.path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)

            return Response({'message': 'Document uploaded successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)