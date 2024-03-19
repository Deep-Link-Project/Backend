from django.db import models

# Create your models here.


class Member(models.Model):

    full_name = models.CharField(max_length=255,null=False)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.full_name
