# 微信公众号资讯汇总系统

[![AI Digest](https://github.com/aphroditee666/ResearchFromWechat/actions/workflows/digest.yml/badge.svg)](https://github.com/aphroditee666/ResearchFromWechat/actions/workflows/digest.yml)

从微信公众号等 RSS 源抓取 AI 相关文章，AI 分类并生成摘要，输出 Markdown。通过 GitHub Actions 每周一/三上午 10:00 自动运行。

## 安装

```bash
pip install -r requirements.txt
```

## 获取公众号 RSS 源（WeWe RSS）

`config.yaml` 中的公众号 RSS 地址由 [WeWe RSS](https://github.com/cooderl/wewe-rss) 生成，已通过 Docker 部署在本地。

### 启动 WeWe RSS 服务

```bash
# WSL 中启动 Docker 守护进程
wsl -u root bash -c 'dockerd &'

# 启动 WeWe RSS
wsl -u root bash -c 'cd /opt/wewe-rss-deploy && docker compose up -d'
```

### 添加订阅

1. 打开 **http://localhost:4000/dash**
2. **账号管理** → 添加账号 → 微信扫码登录（不要勾选"24小时后自动退出"）
3. **公众号源** → 添加 → 粘贴公众号文章分享链接

> 添加频率不要过高，否则会被封控 24 小时。

### 获取 RSS 地址

订阅后在公众号列表中找到对应 `feed_id`，RSS 地址格式：

```
http://localhost:4000/feeds/<feed_id>.rss      # RSS 格式
http://localhost:4000/feeds/<feed_id>.atom     # Atom 格式
http://localhost:4000/feeds/<feed_id>.json     # JSON 格式
http://localhost:4000/feeds/all.atom            # 全部订阅聚合
```

将生成的 RSS 地址填入 `config.yaml` 中对应公众号的 `url` 字段即可。

### 管理命令

```bash
# 查看运行状态
wsl -u root bash -c 'cd /opt/wewe-rss-deploy && docker compose ps'

# 重启服务
wsl -u root bash -c 'cd /opt/wewe-rss-deploy && docker compose restart'

# 停止服务
wsl -u root bash -c 'cd /opt/wewe-rss-deploy && docker compose down'
```

## 配置

编辑 `config.yaml` 添加 RSS 源和 API 配置。

## 运行

```bash
# 单次运行（默认配置）
python main.py --once

# 指定配置文件
python main.py --once --config config/ci.yaml

# 定时调度模式（按 config 中 schedule 配置运行）
python main.py
```
