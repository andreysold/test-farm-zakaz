from apps.winners.views.views import WinnersListApi
from django.urls import path

urlpatterns = [
    path('winners', WinnersListApi.as_view())
]