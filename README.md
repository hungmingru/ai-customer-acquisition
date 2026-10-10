# AI Customer Acquisition

基于 QQ 群控 + ADB 手机控制 + GPT 文案 + POI 查询的 AI 自动获客系统。

## 架构概览

- QQ消息/群控：自动触达用户/群
- ADB手机控制：自动打开应用、点击、输入、抓取界面
- GPT营销文案：自动生成个性化营销文本
- POI查询：基于地图位置做精准获客
- 任务编排：串联上游能力，构建获客链路

## 快速启动

1. 安装依赖

```bash
pip install -r requirements.txt
```

2. 配置环境变量

```bash
cp .env.example .env
```

3. 启动服务

```bash
python main.py
```

4. 调用接口

```bash
curl -X POST http://127.0.0.1:8000/campaign/run \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "奶茶",
    "city": "深圳",
    "product": "外卖优惠活动"
  }'
```

## 接口说明

### 健康检查

- GET /health

### 执行获客任务

- POST /campaign/run

Body:

```json
{
  "keyword": "奶茶",
  "city": "深圳",
  "product": "外卖优惠活动"
}
```

## 注意事项

- QQ/手机自动化涉及平台规则与授权，需合法合规使用。
- ADB 需要开启开发者模式与 USB 调试。
- 使用任何第三方 API 前，请遵守平台协议和相关法律要求。
