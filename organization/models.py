from django.db import models
from organizations.models import Organization
from django.contrib.auth.models import Permission

# Create your models here.
class OrganizationPermissionManager(models.Manager):

    def add_user(self, organization_name, user):
        org, created = Organization.objects.get_or_create(name=organization_name)
        org.add_user(user, is_admin=False)
        return org, created

    def remove_user(self, organization_name, user):
        org, created = Organization.objects.get_or_create(name=organization_name)
        org.users.remove(user)
        return org, created



class OrganizationPermission(models.Model):
    organization = models.OneToOneField(
        Organization, on_delete=models.CASCADE, related_name='org_perm', null=False, primary_key=True, verbose_name='Organization'
    )

    permissions = models.ManyToManyField(
        Permission, verbose_name='Permissions'
    )

    objects = OrganizationPermissionManager()

    class Meta:
        verbose_name = 'Organization permission'
        verbose_name_plural = 'Organization permissions'
