from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class Platform(Enum):
    FEISHU = "feishu"
    DINGTALK = "dingtalk"
    TELEGRAM = "telegram"


@dataclass
class UnifiedMessage:
    """统一消息格式 - 抹平多平台差异"""

    msg_id: str
    platform: Platform
    user_id: str
    user_name: str
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    reply_to: Optional[str] = None
    attachments: list = field(default_factory=list)

    def to_nanobot_prompt(self) -> str:
        """转换为 Nanobot 可处理的 prompt"""
        context = (
            f"[来源: {self.platform.value}] "
            f"[用户: {self.user_name}({self.user_id})] "
            f"[时间: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}]\n\n"
            f"用户提问: {self.content}"
        )
        if self.reply_to:
            context += f"\n\n(这是对消息 {self.reply_to} 的回复)"
        return context