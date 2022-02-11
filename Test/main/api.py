from .models import  Employee, Store, Visit
from  rest_framework import viewsets, permissions
from .serializers import EmployeeSerializer, StoreSerializer, VisitSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmployeeSerializer