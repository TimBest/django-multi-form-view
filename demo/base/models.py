from django.db import models


class Photo(models.Model):
    ANIMAL = 'A'
    PLANT = 'P'
    OTHER = 'O'
    UNKNOWN = 'U'
    TAG_CHOICES = (
        (ANIMAL, 'Animal'),
        (PLANT, 'Plant'),
        (OTHER, 'Other'),
        (UNKNOWN, 'Unknown'),
    )

    image = models.ImageField()
    tag = models.CharField(max_length=1, choices=TAG_CHOICES, default=UNKNOWN)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Record(models.Model):
    photo = models.ForeignKey(Photo)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
