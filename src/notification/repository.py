from uuid import UUID

from src.notification.entity import Notification


class NotificationRepository:
    def __init__(self) -> None:
        self._notifications: dict[UUID, Notification] = {}

    async def create(self, notification: Notification) -> None:
        self._notifications[notification.trace_id] = notification
