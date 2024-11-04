from datetime import timedelta
from datetime import datetime
from config import settings
import pytz
from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def telegram_sender():
    """Отправка сообщения из бота в Телеграм с напоминанием о привычке"""

    habits = Habit.objects.all()

    # Формируем сообщение напоминания в Telegram
    for habit in habits:
        user = habit.owner
        time_start = habit.time.replace(second=0, microsecond=0)
        time_now = datetime.now(pytz.timezone(settings.TIME_ZONE)).replace(second=0, microsecond=0)
        if time_start == time_now:
            message = f"Настало время: {habit.action}, место выполнения: {habit.place}."

        # Дополняем текст уведомления, если у полезной привычки есть связанная привычка или вознаграждение.
            if habit.award:
                message += f" После наградите себя: {habit.award}."
            elif habit.associated_habit:
                message += f" После можете выполнить: {habit.associated_habit}"

            # Устанавливаем дату следующей отправки для привычки
            habit.time = datetime.now(pytz.timezone(settings.TIME_ZONE)) + timedelta(days=habit.periodicity)
            habit.save()

            # Выводим сообщение о результате выполнения отправки сообщения
            if user.telegram_id:
                send_telegram_message(user.telegram_id, message)
                print(f"Напоминание отправлено пользователю {user.email}, телеграм id {user.telegram_id}")
            else:
                print(f"Не удалось отправить напоминание пользователю, так как не указан ID телеграма. {user.email}.")
