from abc import ABC, abstractmethod


# Message Types (can stay simple like this)
class MessageType:
    MARKETING = "MARKETING"
    TRANSACTIONAL = "TRANSACTIONAL"
    ALERTS = "ALERTS"


# Message class (separate responsibility)
class Message:
    def __init__(self, content: str, message_type: str):
        self.content = content
        self.message_type = message_type


# Abstract Notification class
class Notification(ABC):
    @abstractmethod
    def send(self, message: Message):
        pass


class EmailNotification(Notification):
    def send(self, message: Message):
        print(f"[EMAIL - {message.message_type}] {message.content}")


class SMSNotification(Notification):
    def send(self, message: Message):
        print(f"[SMS - {message.message_type}] {message.content}")


class PushNotification(Notification):
    def send(self, message: Message):
        print(f"[PUSH - {message.message_type}] {message.content}")


if __name__ == "__main__":
    # Create messages
    marketing_msg = Message(
        "This is a marketing message.",
        MessageType.MARKETING
    )

    transactional_msg = Message(
        "This is a transactional message.",
        MessageType.TRANSACTIONAL
    )

    alert_msg = Message(
        "This is an alert message.",
        MessageType.ALERTS
    )

    # Create notification channels
    email_notification = EmailNotification()
    sms_notification = SMSNotification()
    push_notification = PushNotification()

    # Send notifications
    email_notification.send(marketing_msg)
    sms_notification.send(transactional_msg)
    push_notification.send(alert_msg)
