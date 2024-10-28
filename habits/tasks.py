from datetime import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def telegram_sender():
    """Отправка сообщения из бота в Телеграм с напоминанием о привычке"""
    habits = Habit.objects.all().order_by("time")
    print(habits)
    current_time = datetime.now().time()
    print(current_time)
    for habit in habits:
        print(habit)
        if habit.owner.telegram_id and habit.time > current_time:
            print("Все есть")
            tg_chat_id = habit.owner.telegram_id
            message = habit.__str__()
            send_telegram_message(tg_chat_id, message)
        else:
            print("Нет привычек")
