from uuid import UUID

from pydantic import BaseModel

from src.notification.enum import NotificationTypeEnum


class CreateNotificationInput(BaseModel):
    message_id: UUID | None
    message_content: str
    notification_type: NotificationTypeEnum


class CreateNotificationOutput(BaseModel):
    trace_id: UUID
    message_id: UUID
