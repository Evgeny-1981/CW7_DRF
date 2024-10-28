import requests

from config.settings import BOT_TOKEN, TELEGRAM_URL


def send_telegram_message(tg_chat_id, message):
    """Отправляет сообщение в Телеграм через бота"""
    parameters = {"chat_id": tg_chat_id, "text": message}
    print(parameters)
    r = requests.get(f"{TELEGRAM_URL}{BOT_TOKEN}/sendMessage", params=parameters)
    print(f"{TELEGRAM_URL}{BOT_TOKEN}")

    if r.status_code == 200:
        print("Сообщение отправлено")
    else:
        print("Ошибка отправки")

