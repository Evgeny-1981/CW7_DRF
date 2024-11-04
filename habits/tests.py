from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@yandex.ru")
        self.user.set_password("1238")
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            owner=self.user,
            action="Тестовая привычка 1",
            is_pleasant_habit=True,
            time="2024-11-04T08:00:00Z",
            place="Дом",
            periodicity=1,
        )

    def test_create_habit(self):
        """Создание привычки"""
        url = reverse("habits:habits_create")
        data = {
            "owner": self.user.pk,
            "action": "Тестовая привычка 2",
            "is_pleasant_habit": "True",
            "time": "2024-11-04T08:10:00Z",
            "place": "Дом",
            "periodicity": 1,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)
        self.assertTrue(Habit.objects.all().exists())

    def test_habit_list(self):
        """Вывод списка привычек"""
        url = reverse("habits:habits_list")
        response = self.client.get(url)
        data = response.json()
        print(data)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "action": "Тестовая привычка 1",
                    "associated_habit": None,
                    "award": None,
                    "execution_time": 120,
                    "id": self.habit.pk,
                    "is_pleasant_habit": True,
                    "is_public_habit": True,
                    "owner": self.user.pk,
                    "periodicity": 1,
                    "place": "Дом",
                    'time': '2024-11-04T13:00:00',

                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_retrieve(self):
        """Проверка корректности данных"""
        url = reverse("habits:habits_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["place"], self.habit.place)

    def test_habit_update(self):
        """Проверка обновления привычки"""
        url = reverse("habits:habits_update", args=(self.habit.pk,))
        data = {
            "action": "Тестовая привычка 1 обновлена",
            "periodicity": 1,
        }
        response = self.client.patch(url, data, format="json")
        print(response.status_code)
        print(response.__dict__)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["action"], "Тестовая привычка 1 обновлена")

    def test_habit_delete(self):
        """Проверка удаления привычки"""
        url = reverse("habits:habits_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)
