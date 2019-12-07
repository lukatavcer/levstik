from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Winner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
    awarded_date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    deleted = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def slug_title(self):
        return "{}-{}".format(self.id, slugify(self.full_name))

    @property
    def url(self):
        return "http://{}/{}/".format(settings.BASE_URL, self.slug_title)
