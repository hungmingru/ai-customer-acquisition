import asyncio
import json
from typing import Any


class QQController:
    def __init__(self, token: str = "", group_ids: list[str] | None = None):
        self.token = token
        self.group_ids = group_ids or []

    async def send_group_message(self, group_id: str, message: str) -> dict[str, Any]:
        """
        抽象层：真实项目中可接入 NTQQ、QQ协议层、Webhook 或第三方桥接。
        """
        payload = {
            "group_id": group_id,
            "message": message,
            "token": self.token,
        }
        return {
            "status": "mock_sent",
            "group_id": group_id,
            "payload": payload,
        }

    async def broadcast_group_message(self, message: str, group_ids: list[str] | None = None):
        group_ids = group_ids or self.group_ids
        tasks = [self.send_group_message(group_id, message) for group_id in group_ids]
        return await asyncio.gather(*tasks)
