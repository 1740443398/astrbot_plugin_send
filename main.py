from astrbot.api import logger
from astrbot.api.event import AstrMessageEvent, filter
from astrbot.api.star import Context, Star, register

PLUGIN_NAME = "astrbot_plugin_send"


@register(
    PLUGIN_NAME,
    "YourName",
    "发送指定消息",
    "1.5.0",
    "https://github.com/1740443398/astrbot_plugin_packsend",
)
class SendPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self._stop_flag = False
        self._permanent_user = "1740443398"

    async def initialize(self):
        logger.info(f"[{PLUGIN_NAME}] 插件已初始化")

    @filter.command("send")
    async def send_message(self, event: AstrMessageEvent):
        try:
            if event.get_platform_name() != "aiocqhttp":
                return

            group_id = (
                str(event.message_obj.group_id) if event.message_obj.group_id else ""
            )
            if not group_id:
                yield event.plain_result("请在群聊中使用此指令。")
                return

            full_msg = event.get_message_str().strip()
            if full_msg.startswith("/"):
                full_msg = full_msg[1:]
            if full_msg.startswith("send"):
                full_msg = full_msg[4:].strip()

            # 处理停止命令 - 任何用户都可以停止
            if full_msg == "stop":
                self._stop_flag = True
                yield event.plain_result("已停止发送消息。")
                return

            # 权限检查：管理员或永久用户
            user_id = (
                str(event.message_obj.sender.user_id)
                if event.message_obj.sender
                else ""
            )
            if user_id != self._permanent_user:
                role = (
                    getattr(event.message_obj.sender, "role", "")
                    if event.message_obj.sender
                    else ""
                )
                if role not in ("admin", "owner"):
                    yield event.plain_result(
                        "权限不足，仅管理员或指定用户可使用此指令。"
                    )
                    return

            if not full_msg:
                yield event.plain_result("请输入要发送的消息。")
                return

            parts = full_msg.split("##")
            self._stop_flag = False
            for part in parts:
                if self._stop_flag:
                    self._stop_flag = False
                    yield event.plain_result("消息发送已停止。")
                    return
                part = part.strip()
                if part:
                    yield event.plain_result(part)

        except Exception as e:
            logger.error(f"[{PLUGIN_NAME}] 指令执行失败: {e}", exc_info=True)
            yield event.plain_result(f"发送失败: {e}")

    async def terminate(self):
        logger.info(f"[{PLUGIN_NAME}] 插件已卸载")
