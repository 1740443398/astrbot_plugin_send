from astrbot.api import logger
from astrbot.api.event import AstrMessageEvent, filter
from astrbot.api.star import Context, Star, register

PLUGIN_NAME = "astrbot_plugin_send"


@register(
    PLUGIN_NAME,
    "YourName",
    "发送指定消息",
    "1.0.0",
    "https://github.com/1740443398/astrbot_plugin_packsend",
)
class SendPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        logger.info(f"[{PLUGIN_NAME}] 插件已初始化")

    @filter.command("send")
    @filter.permission_type(filter.PermissionType.ADMIN)
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

            if not full_msg:
                yield event.plain_result("请输入要发送的消息。")
                return

            parts = full_msg.split("##")
            for part in parts:
                part = part.strip()
                if part:
                    yield event.plain_result(part)

        except Exception as e:
            logger.error(f"[{PLUGIN_NAME}] 指令执行失败: {e}", exc_info=True)
            yield event.plain_result(f"发送失败: {e}")

    async def terminate(self):
        logger.info(f"[{PLUGIN_NAME}] 插件已卸载")
