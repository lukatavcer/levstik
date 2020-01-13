from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat


def max_file_size(image):
    if image.size > settings.MAX_UPLOAD_SIZE:
        raise ValidationError('File too large. Size should not exceed {}.'.format(filesizeformat(settings.MAX_UPLOAD_SIZE)))


def file_path(instance, filename):
    ext = filename.split('.')[-1]
    return 'images/{}.{}'.format(instance.slug_title, ext)


class Winner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateTimeField()
    awarded_date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=file_path, default='images/default_image.jpg', validators=[max_file_size])

    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    deleted = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-awarded_date',)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def slug_title(self):
        return "{}-{}".format(self.id, slugify(self.full_name))

    @property
    def url(self):
        return "http://{}/winner/{}/".format(settings.BASE_URL, self.slug_title)
