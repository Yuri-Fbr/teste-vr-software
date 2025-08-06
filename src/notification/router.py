from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.notification.repository import NotificationRepository
from src.notification.schema import CreateNotificationInput, CreateNotificationOutput
from src.notification.service import NotificationService
from src.notification.usecase import NotificationUsecase
from src.settings.broker import broker_settings

router = APIRouter(prefix='/notifications', tags=['Notifications'])


def notification_usecase_factory() -> NotificationUsecase:
    notification_repository = NotificationRepository()
    notification_service = NotificationService(
        url=broker_settings.url, queue_name=broker_settings.queue_input_name
    )
    return NotificationUsecase(notification_repository, notification_service)


@router.post('', status_code=status.HTTP_202_ACCEPTED)
async def create_notification(
    input_data: CreateNotificationInput,
    usecase: Annotated[NotificationUsecase, Depends(notification_usecase_factory)],
) -> CreateNotificationOutput:
    return await usecase.create_notification(input_data=input_data)
