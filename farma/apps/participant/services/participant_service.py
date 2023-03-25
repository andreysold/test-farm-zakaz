from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from apps.participant.models.models import Participant
from apps.winners.models.models import Winner
import random
import requests


class ParticipantService:

    def create_participant(self, first_name, last_name, age=18, city=None):
        try:
            instance = Participant.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                city=city
            )
        except IntegrityError:
            raise ValidationError({"detail": "User already exist."})
        return instance

    def list(self):
        participants = Participant.objects.all()
        return participants

    def win(self):
        client = requests.get("https://www.random.org/integers/", params={
            "num": "1",
            "min": "1",
            "max": "1000",
            "col": "1", "base": "10", "format": "plain",
        })
        win = client.json()

        return win

    def lottery(self, participants_list: set):
        winner_id = random.sample(participants_list, 1)[0]
        win = self.win()

        participant = Participant.objects.get(id=winner_id)
        Winner.objects.create(participant=participant, win=win)

        return participant

    def start_lottery(self):
        if Participant.objects.count() < 2:
            raise ValidationError({"detail": "Small participant count"})
        participant_list = Participant.objects.values_list('id', flat=True)
        winner = self.lottery(participants_list=set(participant_list))

        return winner
