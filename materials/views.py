from rest_framework import viewsets, generics

from materials.models import Treatise, Lesson
from materials.serializer import TreatiseSerializer, LessonSerializer


class TreatiseViewSet(viewsets.ModelViewSet):
    serializer_class = TreatiseSerializer
    queryset = Treatise.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


