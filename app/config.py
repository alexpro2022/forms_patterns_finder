from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    date_formats: tuple[str, str] = ('%d.%m.%Y', '%Y-%m-%d')
    regex_phone_number: str = r'^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$'
    regex_email: str = r'^\w+\.*\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'
    database_name: str = 'patterns_db'
    collection_name: str = 'patterns_coll'

    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', extra='ignore'
    )

    @property
    def database_url(self) -> str:
        return (f'{self.db_name}://{self.db_user}:{self.db_password}@'
                f'{self.db_host}:{self.db_port}')


config = Settings()
