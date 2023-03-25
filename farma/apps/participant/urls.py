from django.urls import path

from apps.participant.views.views import (
    ParticipantCreateApi,
    ParticipantListApi, ParticipantStartApi
)

urlpatterns = [
    path('participant', ParticipantCreateApi.as_view()),
    path('participant/', ParticipantListApi.as_view()),
    path('start/', ParticipantStartApi.as_view())
]