#!/usr/bin/env python3
"""把 data/talents.json 内嵌进 src/template.html，生成 site/index.html（单文件，可直接部署）。"""
import json
import pathlib

root = pathlib.Path(__file__).parent
data = json.loads((root / "data/talents.json").read_text("utf-8"))

# 基本一致性校验：总数必须与各品阶之和、各分组条目数之和一致
n = sum(len(g["entries"]) for s in data["sections"] for g in s["groups"])
assert n == data["meta"]["total"] == sum(data["meta"]["counts"].values()), f"数据条数不一致: {n}"

payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html = (root / "src/template.html").read_text("utf-8").replace("/*__DATA__*/null", payload)
(root / "site").mkdir(exist_ok=True)
(root / "site/index.html").write_text(html, "utf-8")
print(f"OK: {n} 条 -> site/index.html ({len(html)/1024:.1f} KB)")
