from .serializer import PlanSerializer
from .models import Plan
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView


class PlanList(ListAPIView):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()


class PlanCreate(CreateAPIView):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()

class PlanDestroy(DestroyAPIView):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
# Create your views here.
