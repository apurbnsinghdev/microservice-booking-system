from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    cart_db_host: str
    cart_db_port: int
    cart_db_user: str
    cart_db_pass: str
    cart_db_name: str
    jwt_secret: str
    jwt_algorithm: str

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.cart_db_user}:{self.cart_db_pass}"
            f"@{self.cart_db_host}:{self.cart_db_port}/{self.cart_db_name}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        populate_by_name=True,
    )
