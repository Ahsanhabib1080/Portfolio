from django.db import models
# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.contrib.admin.actions import delete_selected

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    # BElOW LINE OF CODE RETURNS THE TITLE OF THIS OBJECT TO DJANGO ADMIN.
    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        super().delete()
