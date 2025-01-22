from rest_framework import viewsets, generics
from materials.models import Treatise, Lesson
from materials.paginators import MaterialsPaginator
from materials.permissions import IsManager, IsOwner
from materials.serializer import TreatiseSerializer, LessonSerializer
from rest_framework.permissions import IsAuthenticated
from materials.tasks import mail_update_treatise_info


class TreatiseViewSet(viewsets.ModelViewSet):
    serializer_class = TreatiseSerializer
    queryset = Treatise.objects.all()
    pagination_class = MaterialsPaginator

    def get_permissions(self):

        global permission_classes
        if self.action == 'list':
            permission_classes = [IsAuthenticated]

        elif self.action == 'create':
            permission_classes = [IsAuthenticated, ~IsManager]

        elif self.action == 'update' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsManager | IsOwner]

        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return super().get_queryset()

    def perform_update(self, serializer):
        updated_treatise = serializer.save()
        mail_update_treatise_info.delay(updated_treatise)
        updated_treatise.save()


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
    pagination_class = MaterialsPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsManager|IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsManager | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
