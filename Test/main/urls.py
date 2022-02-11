from django.urls import path
from  rest_framework import  routers
from .api import  EmployeeViewSet
from . import views


router = routers.DefaultRouter()
#router.register('api/employee', EmployeeViewSet, 'epmloyee')
#router.register('api/store', views.GetStoreListView.as_view())

urlpatterns = [
    path('api/store', views.StoreListView.as_view()),
    path('api/store/<int:pk>', views.StoreDetailView.as_view()),
    path('api/visit', views.VisitCreateView.as_view())
]
