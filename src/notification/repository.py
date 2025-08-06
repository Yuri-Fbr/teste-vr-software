from uuid import UUID

from src.notification.entity import Notification


class NotificationRepository:
    def __init__(self) -> None:
        self._notifications: dict[UUID, Notification] = {}

    async def create(self, notification: Notification) -> None:
        self._notifications[notification.trace_id] = notification

    async def find(self, trace_id: UUID) -> Notification | None:
        return self._notifications.get(trace_id)
