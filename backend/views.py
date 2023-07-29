from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions,generics
from backend.models import Data,Studentreg,Course,Branch,Reference,Billingdata
from backend.serializers import DataSerializer, StudentregSerializer,CourseSerializer,BranchSerializer,ReferenceSerializer,BillingSerializer
from rest_framework.parsers import MultiPartParser
from knox.models import AuthToken
from rest_framework.response import Response
from backend.serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


# Create your views here.


class DataView(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [permissions.AllowAny]  
    
class StudentregView(viewsets.ModelViewSet):
    queryset = Studentreg.objects.all()
    serializer_class = StudentregSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['student_id','batch','branch','course','status','std_name']

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]  

class BranchView(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [permissions.AllowAny]  

class ReferenceView(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = [permissions.AllowAny]

class BillingView(viewsets.ModelViewSet):
    queryset = Billingdata.objects.all()
    serializer_class = BillingSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['student_id','std_name','date','status']

#
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
    
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)