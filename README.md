# 后天天赋 · 全词条

《我要当老祖》先遣服图鉴「后天天赋」全部 193 条词条的手机端速查页（深色鎏金图鉴风）。

- 搜索：按词条名或效果，支持多个关键词（空格分隔），跨全部分类
- 筛选：品阶（凡 / 良 / 优）+ 分类内分组
- 数据来源：先遣服 2610302002，未实装验证；保留原文，并标注已确认的配置差异（①②③）

## 本地预览

```bash
python3 build.py          # 生成 site/index.html
open site/index.html
```

## 目录

| 路径 | 说明 |
|---|---|
| `data/talents.json` | 词条数据（唯一数据源） |
| `src/template.html` | 页面模板 |
| `build.py` | 把数据内嵌进模板，输出单文件 `site/index.html` |
| `.github/workflows/pages.yml` | 推送 `main` 后自动构建并部署到 GitHub Pages |

## 部署

仓库 Settings → Pages → Source 选择 **GitHub Actions**，之后每次推送到 `main` 会自动发布。
