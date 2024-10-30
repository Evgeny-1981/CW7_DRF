from datetime import timedelta
from datetime import datetime
from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def telegram_sender():
    """Отправка сообщения из бота в Телеграм с напоминанием о привычке"""

    # Отбираем полезные привычки, время выполнения которых наступило
    associated_habit = dict(value).get(self.field)
    time_now = datetime.now()
    habits = Habit.objects.all()
    time_start = time_now - timedelta(minutes=1)
    time_end = time_now + timedelta(minutes=1)

    # Формируем сообщение напоминания в Telegram
    for habit in habits:
        user = habit.owner
        if time_start.time() <= habit.time <= time_end.time():
            message = f"Настало время выполнить - {habit.action} в {habit.place}."
            related_habit = habit.associated_habit

        # Дополняем текст уведомления, если у полезной привычки есть связанная привычка или вознаграждение.

            if habit.award:
                message += f" После наградите себя -  {habit.award}."
            elif habit.associated_habit:
                message += f" После можете выполнить - {habit.associated_habit}"

            # Выводим сообщение о результате выполнения отправки сообщения
            if user.telegram_id:
                send_telegram_message(user.telegram_id, message)
                print(f"Напоминание отправлено пользователю {user.email}.")
            else:
                print(f"Не удалось отправить напоминание пользователю, так как не указан ID телеграма. {user.email}.")
