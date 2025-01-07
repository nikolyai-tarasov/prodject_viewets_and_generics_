from rest_framework import serializers

from materials.models import Treatise, Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class TreatiseSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()
    lessons = LessonSerializer('lessons', many=True)

    class Meta:
        model = Treatise
        fields = '__all__'

    def get_count_lesson(self, obj):
        return len(Lesson.objects.filter(treatise=obj.id))


