# View для API
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.views import APIView
from .models import Service
from .serializer import ServiceSerializer, ServiceFilterSerializer, Service_Type_Serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, extend_schema_view


class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class ServiceDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

@extend_schema_view(
    post=extend_schema(
        summary="Создать сервис",
        description="Эндпоинт для фильтрации можно указывать ниже указынные параметры, если отправить пустым то выведет все обьекты",
        request=ServiceFilterSerializer,
        responses={201: ServiceSerializer}
    )
)
class ServiceFilterView(APIView):
    def post(self, request, *args, **kwargs):
        # Получаем параметры запроса
        min_price = request.data.get('minPrice')
        max_price = request.data.get('maxPrice')
        service_type = request.data.get('service_type', 0)

        # Создаем контекст для сериализатора
        filter_data = {
            'minPrice': min_price,
            'maxPrice': max_price,
            'service_type': service_type
        }

        # Передаем данные в сериализатор
        serializer = ServiceFilterSerializer(data=filter_data)

        # Проверяем, если данные валидны, применяем фильтрацию
        if serializer.is_valid():
            filtered_services = Service.filter_services(min_price=serializer.validated_data['minPrice'],
                                                        max_price=serializer.validated_data['maxPrice'],
                                                        service_type=serializer.validated_data['service_type'])
            service_serializer = ServiceSerializer(filtered_services, many=True)
            return Response(service_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, service_id):
        """
        Получить конкретный сервис по ID
        """
        try:
            service = Service.objects.get(id=service_id)
        except Service.DoesNotExist:
            return Response({'error': 'Service not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceSerializer(service)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Service_Type_ListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = Service_Type_Serializer
