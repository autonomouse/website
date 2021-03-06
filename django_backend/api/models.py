from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.template.defaultfilters import slugify


class TimeStampedBaseModel(models.Model):
    """Base model with timestamp information that is common to many models. """

    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        default=None,
        blank=True,
        null=True,
        help_text="DateTime this model instance was created.")
    updated_at = models.DateTimeField(
        default=timezone.now,
        help_text="DateTime this model instance was last updated.")

    def save(self, *args, **kwargs):
        current_time = timezone.now()
        if self.uuid is None:
            self.created_at = current_time
        self.updated_at = current_time
        return super(TimeStampedBaseModel, self).save(*args, **kwargs)


class Page(TimeStampedBaseModel):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False, )
    name = models.CharField(
        max_length=255,
        default="About",
        unique=True,
        blank=False,
        null=False,
        help_text="Name of page.")
    priority = models.IntegerField(
        default=0,
        blank=False,
        null=False,
        help_text="Reverse order which pages appear in the UI (0 first).")
    slug = models.SlugField(default=None, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Page, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.uuid

    def __str__(self):
        return self.name


class Section(TimeStampedBaseModel):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False, )
    name = models.CharField(
        max_length=255,
        default="Introduction",
        unique=True,
        blank=False,
        null=False,
        help_text="Name of section.")
    priority = models.IntegerField(
        default=0,
        blank=False,
        null=False,
        help_text="Reverse order which sections appear in the UI (0 first).")
    page = models.ForeignKey(
        Page,
        blank=True,
        null=True,
        related_name='sections')

    def __unicode__(self):
        return self.uuid

    def __str__(self):
        return self.name


class Statement(TimeStampedBaseModel):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False, )
    priority = models.IntegerField(
        default=0,
        blank=False,
        null=False,
        help_text="Reverse order which statements appear in the UI (0 first).")
    title = models.CharField(
        max_length=255,
        help_text="Statement title.")
    text = models.TextField(
        default=None,
        blank=True,
        null=True,
        help_text="The text of the statement.")
    section = models.ForeignKey(
        Section,
        blank=True,
        null=True,
        related_name='statements')

    def __unicode__(self):
        return self.uuid

    def __str__(self):
        return self.title
