from rest_framework import serializers

from materials.models import Treatise, Lesson


class TreatiseSerializer(serializers.ModelSerializer):
     class Meta:
         model = Treatise
         fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
