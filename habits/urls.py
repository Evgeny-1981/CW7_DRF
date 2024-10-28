from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitCreateAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
    PublicHabitListAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("habits/create/", HabitCreateAPIView.as_view(), name="habits_create"),
    path("habits/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habits_update"),
    path(
        "habits/<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habits_delete"
    ),
    path("habits/", HabitListAPIView.as_view(), name="habits-list"),
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habits_retrieve"),
    path("habits_public/", PublicHabitListAPIView.as_view(), name="habits_public"),
]