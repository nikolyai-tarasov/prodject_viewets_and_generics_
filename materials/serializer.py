from rest_framework import serializers

from materials.models import Treatise, Lesson
from materials.validators import UnsolicitedLinksValidator
from users.models import Subs


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UnsolicitedLinksValidator(field='link_to_video', )]


class TreatiseSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()
    lessons = LessonSerializer('lessons', many=True, read_only=True)

    def get_count_lesson(self, obj):
        return len(Lesson.objects.filter(treatise=obj.id), )

    def get_is_subscribed(self, instance):
        user = self.context.get('request').user
        subscription = Subs.objects.filter(user=user, treatise=instance).exists()
        return subscription

    class Meta:
        model = Treatise
        fields = '__all__'
