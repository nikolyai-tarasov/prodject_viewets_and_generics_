from rest_framework import viewsets, generics
from rest_framework.decorators import permission_classes

from materials.models import Treatise, Lesson
from materials.permissions import IsManager, IsOwner
from materials.serializer import TreatiseSerializer, LessonSerializer
from rest_framework.permissions import IsAuthenticated


class TreatiseViewSet(viewsets.ModelViewSet):
    serializer_class = TreatiseSerializer
    queryset = Treatise.objects.all()

    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [IsAuthenticated]

        elif self.action == 'create':
            permission_classes = [IsAuthenticated, ~IsManager]

        elif self.action == 'update' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsManager | IsOwner]

        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]
            
        return [permission() for permission in permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsManager]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsManager | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsManager | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
