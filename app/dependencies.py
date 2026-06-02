from functools import lru_cache

from langchain_openai import ChatOpenAI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """환경변수 기반 설정.

    .env 파일이 있으면 자동 로드합니다.
    """

    openai_api_key: str             # 기본설정 안하고 기본타입 지정
    model_name: str = "gpt-5-nano"
    port: int = 8000
    request_timeout: float = 30.0

    model_config = SettingsConfigDict(
        env_file=".env",                # .env 어디에서 읽을 것이냐?가 관건
        # env_file_encoding="utf-8",
        # case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    """Settings 싱글톤. 첫 호출 시 1회만 생성됩니다."""
    return Settings()


@lru_cache
def get_llm() -> ChatOpenAI:
    """ChatOpenAI 싱글톤.

    Depends(get_llm)으로 주입받으면 요청마다 객체가 재사용됩니다.
    """
    settings = get_settings()
    return ChatOpenAI(
        model=settings.model_name,
        api_key=settings.openai_api_key,
        timeout=settings.request_timeout,
    )