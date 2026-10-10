# AI Customer Acquisition Platform

AI Customer Acquisition Platform 是一个基于 AI + 自动化脚本 + 地图搜索 + 营销文案生成的获客系统。它旨在帮助运营人员快速筛选线索、生成高转化文案、自动触达目标客户，并通过后台监控获客效果。

该项目当前处于早期原型/内部工具阶段，适合用于技术验证、营销自动化实验和 SaaS 产品原型开发。

## 功能概览

- POI/位置搜索：结合地图 API，筛选目标商圈、商户、门店和潜在客户区域
- AI 营销文案：使用大模型生成营销文案，支持文案个性化
- QQ / 群消息触达：提供消息发送接口抽象层，支持后续接入真实 QQ 消息协议或第三方平台
- ADB 手机自动化：支持 Android 手机的 UI 操作、点击和文本输入抽象
- 任务编排：支持活动任务管理、定时任务、队列处理和重试逻辑
- 运营监控：支持活动进度、ROI、发送效果、失败日志统计
- 后台管理：支持任务创建、用户管理、权限角色和运营报表

## 技术���构

- 后端：FastAPI
- 数据库：SQLAlchemy + SQLite/PostgreSQL
- 消息队列：Redis + RQ
- AI 能力：OpenAI / 自定义 LLM 接口
- 地图 API：高德 / 百度
- 自动化：Android ADB
- 前端：Vue 3 + Vite（后台管理界面）
- 实时监控：WebSocket + Dashboard

## 项目结构

```text
ai-customer-acquisition/
├── app/
│   ├── api.py
│   ├── admin_api.py
│   ├── auth.py
│   ├── bootstrap.py
│   ├── config.py
│   ├── copywriter.py
│   ├── dashboard.py
│   ├── database.py
│   ├── executor.py
│   ├── job_service.py
│   ├── monitoring.py
│   ├── monitoring_api.py
│   ├── models.py
│   ├── phone_controller.py
│   ├── poi_search.py
│   ├── qq_controller.py
│   ├── queue.py
│   ├── redis_client.py
│   ├── schemas.py
│   ├── services.py
│   ├── tasks.py
│   ├── ws.py
│   └── report_service.py
├── frontend-admin/
│   ├── src
│   ├── package.json
│   └── vite.config.js
├── main.py
├── requirements.txt
├── .env.example
├── README.md
├── redis.conf
├── docker-compose.yml
└── .gitignore
```

## 安装要求

- Python 3.10+
- Node.js 18+
- Redis
- Android 设备（如启用 ADB 自动化）
- OpenAI API Key
- 地图 API Key（高德/百度）

## 环境变量

复制示例文件：

```bash
cp .env.example .env
```

示例内容：

```env
DEBUG=false

OPENAI_API_KEY=your_openai_key
OPENAI_MODEL=gpt-4o-mini

AMAP_KEY=your_amap_key
BAIDU_KEY=your_baidu_key

QQ_PLATFORM_TOKEN=your_qq_token
QQ_GROUP_IDS=group1,group2,group3

ADB_SERIAL=
REDIS_URL=redis://localhost:6379/0
ALLOWED_ORIGINS=*
DATABASE_URL=sqlite:///./campaign.db
JWT_SECRET_KEY=super-secret-key-change-me
```

## 启动步骤

### 1. 安装后端依赖

```bash
pip install -r requirements.txt
```

### 2. 启动 Redis

```bash
redis-server
```

### 3. 启动后台 worker

```bash
python -m app.worker
```

### 4. 启动后端服务

```bash
python main.py
```

### 5. 启动前端后台

```bash
cd frontend-admin
npm install
npm run dev
```

### 6. 默认管理员账号

默认账号如下：

- 用户名：admin
- 密码：admin123

登录地址：

```text
http://127.0.0.1:5173
```

后端 API：

```text
http://127.0.0.1:8000
```

## 常用接口

### 创建活动

```bash
curl -X POST http://127.0.0.1:8000/campaigns \
  -H "Content-Type: application/json" \
  -d '{
    "name":"门店获客测试",
    "keyword":"奶茶",
    "city":"深圳",
    "product":"外卖优惠活动"
  }'
```

### 触发活动任务

```bash
curl -X POST http://127.0.0.1:8000/campaigns/1/run
```

### 查询任务状态

```bash
curl http://127.0.0.1:8000/jobs/{job_id}
```

### 查看总览

```bash
curl http://127.0.0.1:8000/monitor/overview
```

### 查看报表

```bash
curl http://127.0.0.1:8000/monitor/report
```

## 功能说明

### 1. AI 文案生成
自动生成营销文案，适合社交平台和私域营销场景，支持不同风格和不同客户群体的个性化改写。

### 2. 地图检索
通过 POI 搜索找到目标区域、商圈、门店或潜在客户集中区，减少随机获客成本。

### 3. 自动化触达
支持 QQ 群消息、手机自动化操作和后续接入真实渠道，适合批量营销场景。

### 4. 任务与监控
所有营销动作都可以被记录为任务，支持重试、日志、失败追踪和 ROI 统计。

## 合规提醒

本项目涉及自动化营销、自动消息发送和户外/地图定位能力，使用前请务必遵守以下要求：

- 遵守平台协议与用户隐私法律
- 不得在未授权场景下发送营销内容
- 对客户数据进行最小化采集
- 对消息发送设置频率限制
- 加强审核和人工干预机制

对于真实的 QQ、微信、短信、电话等通道接入，建议提前做企业授权、权限审批和合规审查。

## 当前状态

当前版本是：

- 原型版/实验版
- 适合技术验证
- 可扩展为 SaaS 产品基础架构
- 适合业务团队内部测试与迭代

未来重点方向包括：

- 真实渠道接入
- 用户画像和 CRM
- 自动化转化统计
- 多租户平台
- 运营报表导出
- AI 营销推荐系统

## 贡献说明

欢迎对以下方向做贡献：

- 更稳定的消息通道接入
- UI/UX 优化
- 报表分析能力
- 错误处理和重试机制
- 安全审计和权限设计

## 许可证

本项目当前用于内部开发和技术原型验证，具体许可证请根据团队要求补充。
