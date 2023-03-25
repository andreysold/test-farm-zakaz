from django.db import models


class Participant(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    age = models.IntegerField(null=True)
    city = models.CharField(null=True, max_length=256)

    class Meta:
        db_table = "participant"
        unique_together = ('first_name', 'last_name',)
