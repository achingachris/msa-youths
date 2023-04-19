from rest_framework import serializers, generics
from .models import Nominee, NominationCategory

class NominationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NominationCategory
        fields = '__all__'

class NomineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nominee
        fields = '__all__'
