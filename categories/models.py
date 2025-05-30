from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
