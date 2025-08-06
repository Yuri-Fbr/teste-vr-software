from uuid import UUID, uuid4

from src.notification.entity import Notification
from src.notification.enum import NotificationStatusEnum
from src.notification.exception import NotificationNotFoundError
from src.notification.repository import NotificationRepository
from src.notification.schema import (
    CreateNotificationInput,
    CreateNotificationOutput,
    NotificationOutput,
)
from src.notification.service import NotificationService


class NotificationUsecase:
    def __init__(
        self,
        notification_repository: NotificationRepository,
        notification_service: NotificationService,
    ) -> None:
        self.notification_repository = notification_repository
        self.notification_service = notification_service

    async def create_notification(
        self, input_data: CreateNotificationInput
    ) -> CreateNotificationOutput:
        trace_id = uuid4()
        message_id = input_data.message_id or uuid4()
        message_content = input_data.message_content
        notification_type = input_data.notification_type
        status = NotificationStatusEnum.RECEIVED

        notification = Notification(
            trace_id=trace_id,
            message_id=message_id,
            message_content=message_content,
            notification_type=notification_type,
            status=status,
        )
        await self.notification_repository.create(notification)
        await self.notification_service.send_notification(notification)
        return CreateNotificationOutput(
            trace_id=notification.trace_id, message_id=notification.message_id
        )

    async def find_notification(self, trace_id: UUID) -> NotificationOutput:
        notification = await self.notification_repository.find(trace_id)
        if notification is None:
            raise NotificationNotFoundError
        return NotificationOutput(
            trace_id=notification.trace_id,
            message_id=notification.message_id,
            message_content=notification.message_content,
            notification_type=notification.notification_type,
            status=notification.status,
        )
