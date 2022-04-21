from rest_framework import viewsets
from django.shortcuts import render
from organizations.models import OrganizationUser
from .permissions import ModelPermissions
from .serializers import OrganizationUserSerializer

# Create your views here.

class OrganizationUserViewSet(viewsets.ModelViewSet):

    perms_map = {
        'POST': 'organizations.view_organizationuser',
    }

    permission_classes = [ModelPermissions]
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserSerializer


