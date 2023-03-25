from apps.winners.models.models import Winner


class WinnerService:

    def list(self):
        winners = Winner.objects.all()

        return winners