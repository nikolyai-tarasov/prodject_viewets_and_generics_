from django.urls import path
from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import TreatiseViewSet, LessonCreateAPIView, LessonUpdateAPIView, LessonListAPIView, \
    LessonRetrieveAPIView, LessonDestroyAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register('treatise', TreatiseViewSet)
urlpatterns = [
    path('lesson_create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/retrieve/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lesson/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
] + router.urls