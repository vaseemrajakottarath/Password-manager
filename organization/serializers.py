from rest_framework import serializers
from organizations.models import OrganizationUser

class OrganizationUserSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)

    class Meta:
        model=OrganizationUser
        fields=['id','organization','user']
        