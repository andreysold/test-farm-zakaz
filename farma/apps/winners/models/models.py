from django.db import models

from apps.participant.models.models import Participant


class Winner(models.Model):
    win = models.IntegerField()
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

    class Meta:
        db_table = "winners"
