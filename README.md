\# 多平台智能客服系统



基于 Nanobot + MCP 协议的多平台智能客服系统，支持 QQ 接入，具备知识库检索、工单管理、跨会话用户记忆等核心功能。



\## 核心功能



\- \*\*多平台接入\*\*：支持 QQ（已完成），飞书/钉钉可扩展

\- \*\*知识库检索\*\*：动态读取 `knowledge\_base/general.md`，支持动态更新

\- \*\*工单管理\*\*：基于 MCP 协议实现完整 CRUD，数据持久化到 SQLite

\- \*\*用户记忆\*\*：跨会话记忆用户偏好，支持多渠道共享

\- \*\*容器化部署\*\*：支持 Docker 一键部署（进行中）



\## 技术栈



\- Agent 框架：Nanobot

\- 大模型：智谱 GLM-4.7-Flash / DeepSeek

\- MCP 协议：自定义工单 Server

\- 部署：Git + Docker



\## 项目结构



```



├── mcp\_servers/          # MCP Server（工单管理）

│   └── ticket\_server.py

├── workspace/

│   ├── skills/           # 技能定义

│   │   ├── ticket/       # 工单技能

│   │   └── knowledge/    # 知识库技能

│   ├── knowledge\_base/   # 知识库文件

│   │   └── general.md

│   └── memory/           # 用户记忆

├── config.json           # 配置文件

├── Dockerfile            # 容器化配置

└── README.md



```



\## 快速启动



\### 1. 安装依赖



```bash

pip install nanobot-ai mcp

```



2\. 配置 API Key



编辑 config.json，填入你的智谱或 DeepSeek API Key。



3\. 启动服务



```bash

nanobot gateway

```



4\. 测试



在 QQ 中向机器人发送消息：



· 你好 → 打招呼

· 怎么重置密码 → 知识库检索

· 提交工单，标题电脑蓝屏 → 创建工单

· 我是谁 → 用户记忆





许可证



MIT



```



\---

