from uuid import UUID

from src.notification.enum import NotificationStatusEnum, NotificationTypeEnum


class Notification:
    def __init__(
        self,
        trace_id: UUID,
        message_id: UUID,
        message_content: str,
        notification_type: NotificationTypeEnum,
        status: NotificationStatusEnum,
    ) -> None:
        self.trace_id = trace_id
        self.message_id = message_id
        self.message_content = message_content
        self.notification_type = notification_type
        self.status = status

    def to_dict(self) -> dict:
        return {
            'trace_id': self.trace_id,
            'message_id': self.message_id,
            'message_content': self.message_content,
            'notification_type': self.notification_type,
        }
