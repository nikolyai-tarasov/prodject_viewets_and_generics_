from rest_framework import serializers
from users.models import Payments, User, Subs



class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subs
        fields = '__all__'
