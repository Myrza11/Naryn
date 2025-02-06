from django.urls import path
from services.views import ServiceListAPIView, ServiceUpdateAPIView, ServiceCreateAPIView, ServiceDeleteAPIView, ServiceFilterView, ServiceDetailView, Service_Type_ListAPIView



urlpatterns = [
    path('listservice/', ServiceListAPIView.as_view()),
    path('updateservice/<int:pk>/', ServiceUpdateAPIView.as_view()),
    path('craeteservice/<int:pk>/', ServiceCreateAPIView.as_view()),
    path('deleteservice/<int:pk>/', ServiceDeleteAPIView.as_view()),
    path('filterservice/', ServiceFilterView.as_view()),
    path('services/<int:service_id>/', ServiceDetailView.as_view()),
    path('listservice/', ServiceListAPIView.as_view()),
    path('list_service_type/', Service_Type_ListAPIView.as_view())

]