from unittest.mock import AsyncMock

import pytest

from src.notification.entity import Notification
from src.notification.exception import NotificationNotFoundError
from src.notification.repository import NotificationRepository
from src.notification.schema import CreateNotificationInput
from src.notification.service import NotificationService
from src.notification.usecase import NotificationUsecase


async def test_create_notification_usecase(
    notification: Notification,
    notification_usecase: NotificationUsecase,
    notification_repository: NotificationRepository,
    notification_service: NotificationService,
) -> None:
    notification_repository.create = AsyncMock()
    notification_service.send_notification = AsyncMock()
    input_data = CreateNotificationInput(
        message_id=notification.message_id,
        message_content=notification.message_content,
        notification_type=notification.notification_type,
    )
    created_notification = await notification_usecase.create_notification(input_data)

    assert created_notification.trace_id is not None
    assert created_notification.message_id is not None


async def test_find_notification_usecase(
    notification: Notification,
    notification_usecase: NotificationUsecase,
    notification_repository: NotificationRepository,
) -> None:
    notification_repository.find = AsyncMock(return_value=notification)
    result = await notification_usecase.find_notification(notification.trace_id)

    assert result is not None


async def test_find_notification_usecase_not_found(
    notification_usecase: NotificationUsecase,
    notification_repository: NotificationRepository,
) -> None:
    notification_repository.find = AsyncMock(return_value=None)

    with pytest.raises(NotificationNotFoundError) as error:
        await notification_usecase.find_notification('non-existent-id')

    assert str(error.value) == NotificationNotFoundError.message
