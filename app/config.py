import os
from dataclasses import dataclass, field
from typing import List

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    app_name: str = "AI Customer Acquisition"
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"

    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    amap_key: str = os.getenv("AMAP_KEY", "")
    baidu_key: str = os.getenv("BAIDU_KEY", "")

    qq_platform_token: str = os.getenv("QQ_PLATFORM_TOKEN", "")
    qq_group_ids: List[str] = field(
        default_factory=lambda: [item.strip() for item in (os.getenv("QQ_GROUP_IDS", "") or "").split(",") if item.strip()]
    )

    adb_serial: str = os.getenv("ADB_SERIAL", "")
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    allowed_origins: List[str] = field(
        default_factory=lambda: [item.strip() for item in (os.getenv("ALLOWED_ORIGINS", "*") or "*").split(",") if item.strip()]
    )


settings = Settings()
