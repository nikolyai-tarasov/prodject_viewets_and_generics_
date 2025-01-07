from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from users.models import Payments
from rest_framework.filters import OrderingFilter


class PaymentsCreateAPIView(generics.CreateAPIView):
    pass


class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course','paid_lesson','payment_method',)
    ordering_fields = ('pay_date',)




class PaymentsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Payments.objects.all()


class PaymentsUpdateAPIView(generics.UpdateAPIView):
    queryset = Payments.objects.all()


class PaymentsDestroyAPIView(generics.DestroyAPIView):
    queryset = Payments.objects.all()
