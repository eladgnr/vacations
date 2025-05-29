# vacations/api_views.py
from rest_framework import viewsets
from .models import Vacation
from .serializers import VacationSerializer


class VacationViewSet(viewsets.ModelViewSet):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer
