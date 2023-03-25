from rest_framework.generics import GenericAPIView

from apps.winners.models.models import Winner
from apps.winners.serializers.serializers import WinnersSerializer
from rest_framework.response import Response

from apps.winners.servicies.winner_services import WinnerService


class WinnersListApi(GenericAPIView):
    serializer_class = WinnersSerializer

    def get(self, request):
        service = WinnerService()
        winner_list = service.list()

        serializer = self.get_serializer(winner_list, many=True)
        return Response(serializer.data)


