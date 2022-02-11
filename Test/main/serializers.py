from  rest_framework import  serializers
from  .models import Employee, Store, Visit
from  datetime import  datetime

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name')


class StoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('id', 'date')


class VisitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'