"""Module for sending messages."""
import requests
from requests.exceptions import RequestException


def send_message_to_telegram(message: str, token: str, chat_id: str) -> None:
    """
    Send message to Telegram.

    Args:
        message: Message to send.
        token: Telegram bot token.
        chat_id: Telegram chat id.

    Raises:
        RequestException: If the message could not be sent to Telegram.
    """
    TELEGRAM_URL = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=HTML"
    response = requests.get(TELEGRAM_URL)
    if not response.ok:
        print(response.text)
        raise RequestException("Message could not be sent to Telegram")
