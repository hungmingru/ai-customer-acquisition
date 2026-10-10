import os
from typing import Any

from openai import OpenAI


class CopyWriter:
    def __init__(self, api_key: str | None = None, model: str | None = None):
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def generate_ad_copy(self, target_audience: str, product: str, tone: str = "专业营销") -> str:
        prompt = f"""
        你是一名资深营销文案专家。

        目标受众：{target_audience}
        产品/服务：{product}
        风格：{tone}

        要求：
        1. 语言要有冲击力，适合社交平台和群消息
        2. 直接突出价值、痛点和行动号召
        3. 适合微信/QQ消息场景
        4. 不要过长，控制在 100~200 字
        5. 语气自然、专业、容易转化

        输出中文文案：
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=250,
        )
        return response.choices[0].message.content.strip()

    def personalize_copy(self, base_copy: str, user_profile: dict[str, Any]) -> str:
        prompt = f"""
        下面是一段营销文案，请根据用户画像进行个性化改写，保留主卖点：

        用户画像：{user_profile}
        原文案：{base_copy}

        输出个性化版本，中文，适合消息发送：
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            max_tokens=220,
        )
        return response.choices[0].message.content.strip()
