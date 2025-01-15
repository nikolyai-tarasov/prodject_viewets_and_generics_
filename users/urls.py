from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import PaymentsCreateAPIView, PaymentsListAPIView, PaymentsUpdateAPIView, PaymentsRetrieveAPIView, \
    PaymentsDestroyAPIView, UserCreateAPIView, UserUpdateAPIView, UserRetrieveAPIView, UserDestroyAPIView, \
    SubsAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('payments_create/', PaymentsCreateAPIView.as_view(), name='lesson_create'),
    path('payments_list/', PaymentsListAPIView.as_view(), name='lesson_list'),
    path('payments/update/<int:pk>/', PaymentsUpdateAPIView.as_view(), name='lesson_update'),
    path('payments/retrieve/<int:pk>/', PaymentsRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('payments_destroy/<int:pk>/', PaymentsDestroyAPIView.as_view(), name='lesson_destroy'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('user/create/', UserCreateAPIView.as_view(), name='user_create'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user/retrieve/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('user/destroy/<int:pk>/', UserDestroyAPIView.as_view(), name='user_destroy'),
    path('subs/', SubsAPIView.as_view(), name='subs'),


]
