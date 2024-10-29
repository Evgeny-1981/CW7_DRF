# from datetime import datetime
#
# from celery import shared_task
#
# from habits.models import Habit
# from habits.services import send_telegram_message
#
#
# @shared_task
# def telegram_sender():
#     """Отправка сообщения из бота в Телеграм с напоминанием о привычке"""
#     habits = Habit.objects.all().order_by("time")
#     current_time = datetime.now().time()
#     for habit in habits:
#         if habit.owner.telegram_id and habit.time > current_time:
#             tg_chat_id = habit.owner.telegram_id
#             print(tg_chat_id)
#             message = habit.__str__()
#             send_telegram_message(tg_chat_id, message)
#         else:
#             print("Нет привычеккккк")
from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def telegram_sender():
    """Отправка сообщения из бота в Телеграм с напоминанием о привычке"""

    # Отбираем полезные привычки, срок выполнения которых наступил
    habits = Habit.objects.filter(
        time__lte=timezone.now().time(),
        execution_time__lte=timezone.now().date(),
        is_pleasant_habit=False,
    )

    # Отправляем напоминания в Telegram
    for habit in habits:
        user = habit.owner
        message = f"Я буду {habit.action} в {habit.time} {habit.place}."
        related_habit = habit.associated_habit

        # Дополняем текст уведомления, если у полезной привычки есть связанная привычка или вознаграждение.

        if habit.award:
            message += f" А сразу после этого могу {habit.award}."
        elif related_habit:
            message += f" {related_habit}"

        if user.telegram_id:
            send_telegram_message(user.telegram_id, message)
            print(f"Напоминание отправлено пользователю {user.email}.")
        else:
            print(f"Не удалось отправить напоминание пользователю, так как не указан ID телеграма. {user.email}.")

        # Обновляем дату следующего выполнения привычки
        habit.execution_time = timezone.now().date() + timedelta(days=habit.periodicity)
        habit.save()
        if related_habit:
            related_habit.execution_time = timezone.now().date() + timedelta(
                days=related_habit.periodicity
            )
            related_habit.save()
