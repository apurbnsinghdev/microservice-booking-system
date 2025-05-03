from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    catalog_db_host: str = Field(..., alias="CATALOG_DB_HOST")
    catalog_db_port: int = Field(..., alias="CATALOG_DB_PORT")
    catalog_db_user: str = Field(..., alias="CATALOG_DB_USER")
    catalog_db_pass: str = Field(..., alias="CATALOG_DB_PASS")
    catalog_db_name: str = Field(..., alias="CATALOG_DB_NAME")
    jwt_secret: str = Field(..., alias="JWT_SECRET")
    jwt_algorithm: str = Field("HS256", alias="JWT_ALGORITHM")

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.catalog_db_user}:{self.catalog_db_pass}"
            f"@{self.catalog_db_host}:{self.catalog_db_port}/{self.catalog_db_name}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        populate_by_name=True,
    )
