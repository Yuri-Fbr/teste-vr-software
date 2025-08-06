from pydantic_settings import BaseSettings, SettingsConfigDict


class BrokerSettings(BaseSettings):
    BROKER_USERNAME: str | None = None
    BROKER_PASSWORD: str | None = None
    BROKER_HOST: str | None = None
    BROKER_PORT: int | None = None

    @property
    def url(self) -> str:
        return f'amqp://{self.BROKER_USERNAME}:{self.BROKER_PASSWORD}@{self.BROKER_HOST}:{self.BROKER_PORT}/'

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='allow')

    @property
    def queue_input_name(self) -> str:
        return 'fila.notificacao.entrada.ivarcarrera'

    @property
    def queue_retry_name(self) -> str:
        return 'fila.notificacao.retry.ivarcarrera'

    @property
    def queue_validation_name(self) -> str:
        return 'fila.notificacao.validacao.ivarcarrera'

    @property
    def queue_dlq_name(self) -> str:
        return 'fila.notificacao.dlq.ivarcarrera'


broker_settings = BrokerSettings()
