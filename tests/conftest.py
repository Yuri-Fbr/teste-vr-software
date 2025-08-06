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
        trace_id='550e8400-e29b-41d4-a716-446655440000',
        message_id='550e8400-e29b-41d4-a716-446655440000',
        message_content='Notification content example',
        notification_type=NotificationTypeEnum.EMAIL,
        status=NotificationStatusEnum.RECEIVED,
    )
