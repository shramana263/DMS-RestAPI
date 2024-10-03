from django.urls import path, include

from .views.Auth import RegisterView, LoginView
from .views.Document import DocumentUploadView


urlpatterns = [
    path('register',RegisterView.as_view(), name='register'),
    path('login',LoginView.as_view(),name='login'),
    path('upload', DocumentUploadView.as_view(), name='uploaddocument'),
]

