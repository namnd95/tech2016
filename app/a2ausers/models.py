from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class A2AUserManager(models.Manager):
    def create_user(self, username, first_name, last_name, email, password,
                    **kwargs):
        if not email:
            raise ValueError('User must have a valid email address.')

        if not username:
            raise ValueError('User must have a valid username.')

        user = User.objects.create_user(username,
                                        email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        account = self.model(
            user=user,
        )
        account.save()

        return account


class A2AUser(models.Model):
    objects = A2AUserManager()

    user = models.OneToOneField(User, related_name='a2ausers')
    facebook_id = models.CharField(max_length=200, null=True, blank=True)

    @property
    def user__username(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = 'A2A User'
        verbose_name_plural = 'A2A Users'
