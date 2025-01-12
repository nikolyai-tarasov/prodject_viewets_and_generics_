from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import PaymentsCreateAPIView, PaymentsListAPIView, PaymentsUpdateAPIView, PaymentsRetrieveAPIView, \
    PaymentsDestroyAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('payments_create/', PaymentsCreateAPIView.as_view(), name='lesson_create'),
    path('payments_list/', PaymentsListAPIView.as_view(), name='lesson_list'),
    path('payments/update/<int:pk>/', PaymentsUpdateAPIView.as_view(), name='lesson_update'),
    path('payments/retrieve/<int:pk>/', PaymentsRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('payments_destroy/', PaymentsDestroyAPIView.as_view(), name='lesson_destroy'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
