from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee, Store, Visit
from .serializers import *
from datetime import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class StoreListView(APIView):
    def get(self, request):
        phone = self.request.query_params.get('phone')
        queryset = Store.objects.filter(employee__phone=phone)
        serializer_for_queryset = StoreSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)


class StoreDetailView(APIView):
    def get(self, request, pk):
        queryset = Store.objects.filter(id=pk)
        serializer_for_queryset = StoreDetailSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)

class VisitCreateView(APIView):
    def post(self, request):
        serializer = VisitCreateSerializer(data=request.data)
        if serializer.is_valid():
            phone = self.request.query_params.get('phone')
            store_name=serializer.validated_data.get('store')
            store = Store.objects.filter(employee__phone=phone, name=store_name)
            if store:
                serializer.save()
                queryset = Visit.objects.get(id=serializer.data.get('id'))
                response_serializer = VisitSerializer(
                    instance=queryset,
                    many=False
                )
                return Response(response_serializer.data, status=201)
            else: return Response({'Error': 'Пользователь не прендлежит данному ТТ'}, status=400)
        return Response(serializer.errors, status=400)