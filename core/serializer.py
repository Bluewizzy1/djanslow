from rest_framework.serializers import ModelSerializer
from core.models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customerfields = "__all__"