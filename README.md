# astrbot_plugin_send

管理员或指定用户使用 `/send` 指令让 Bot 发送指定消息，支持 `##` 分隔符分条发送，任何用户可用 `/send stop` 停止发送。

> [!NOTE]
> 这是 [AstrBot](https://github.com/AstrBotDevs/AstrBot) 的插件。
>
> [AstrBot](https://github.com/AstrBotDevs/AstrBot) 是一个 agentic 助手，适用于个人和群聊场景。支持部署在 QQ、Telegram、飞书、钉钉、Slack、LINE、Discord、Matrix 等数十个主流即时通讯平台。

## 功能特性

- **发送消息**：管理员或指定用户使用 `/send` 指令发送消息
- **分条发送**：使用 `##` 分隔符将消息拆分为多条，依次发送
- **停止发送**：**任何用户**均可使用 `/send stop` 立即停止正在进行的发送
- **永久用户**：QQ号 `1740443398` 拥有永久使用权限，不受管理员身份限制
- **仅 aiocqhttp 平台生效**：仅在 QQ 群聊场景下工作

## 安装

将插件文件夹 `astrbot_plugin_send` 放入 AstrBot 的 `data/plugins` 目录，重启 AstrBot 即可。

## 指令说明

### 发送消息

管理员或指定用户可在群聊中发送以下指令：

```
/send <消息内容>
```

**示例：**

```
/send 你好                          # Bot 发送：你好
/send 你好##我是一个bot               # Bot 先发"你好"，再发"我是一个bot"
/send 第一段##第二段##第三段           # Bot 依次发送三段消息
```

### 停止发送

**任何用户**可在群聊中发送以下指令，立即停止正在进行的消息发送：

```
/send stop
```

## 工作流程

1. 管理员或指定用户在群聊中发送 `/send <消息内容>` 指令
2. 插件解析 `/send` 后的消息内容
3. 若消息为空，提示输入内容
4. 若消息包含 `##`，按 `##` 拆分后依次发送每条消息
5. 空分段自动跳过
6. 发送过程中，任何群成员可发送 `/send stop` 立即停止发送

## 兼容性

- 平台：aiocqhttp（QQ）
- AstrBot 版本：>=4.16, <5

## Supports

- [AstrBot Repo](https://github.com/AstrBotDevs/AstrBot)
- [AstrBot 插件开发文档（中文）](https://docs.astrbot.app/dev/star/plugin-new.html)
- [AstrBot Plugin Development Docs (English)](https://docs.astrbot.app/en/dev/star/plugin-new.html)

## 许可证

AGPL-3.0