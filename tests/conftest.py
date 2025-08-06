import pytest

from src.notification.entity import Notification
from src.notification.enum import NotificationStatusEnum, NotificationTypeEnum
from src.notification.repository import NotificationRepository
from src.notification.service import NotificationService
from src.notification.usecase import NotificationUsecase


@pytest.fixture
def notification_repository() -> NotificationRepository:
    return NotificationRepository


@pytest.fixture
def notification_service() -> NotificationService:
    return NotificationService


@pytest.fixture
def notification_usecase(
    notification_repository: NotificationRepository,
    notification_service: NotificationService,
) -> NotificationUsecase:
    return NotificationUsecase(notification_repository, notification_service)


@pytest.fixture
def notification() -> Notification:
    return Notification(
        trace_id='8b3e56f1-bb2b-47e3-a1c5-7384dc9b98a3',
        message_id='8b3e56f1-bb2b-47e3-a1c5-7384dc9b98a3',
        message_content='Notification content example',
        notification_type=NotificationTypeEnum.EMAIL,
        status=NotificationStatusEnum.RECEIVED,
    )
