#!/usr/bin/env python3
"""Route a Chinese health log prompt to the most relevant Health Tracker skill.

Usage:
    python scripts/route_health_skill.py "今天空腹血糖5.6"
    python scripts/route_health_skill.py "昨晚羽毛球2小时，外扩腿60个"

This helper is intentionally simple and local. Codex still relies mainly on skill
frontmatter descriptions for automatic invocation; this script documents and
checks the routing rules used by the health-tracker plugin.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class SkillRule:
    skill: str
    reason: str
    keywords: tuple[str, ...]
    patterns: tuple[str, ...] = ()


RULES = (
    SkillRule(
        "blood-glucose-tracker",
        "blood glucose reading, meal-timing glucose, or glucose trend request",
        ("血糖", "空腹血糖", "餐前", "饭前", "餐后", "饭后", "指尖", "血糖仪", "mmol", "mg/dl", "低血糖", "高血糖"),
        (r"\b\d+(\.\d+)?\s*(mmol/?l|mg/?dl)\b",),
    ),
    SkillRule(
        "body-composition-tracker",
        "InBody/body composition, daily weight, target weight, or body metric request",
        ("inbody", "体脂", "骨骼肌", "肌肉量", "体重", "目标体重", "内脏脂肪", "腰臀比", "基础代谢", "bmi", "身体成分"),
        (),
    ),
    SkillRule(
        "exercise-log-coach",
        "workout, exercise, sport, cardio, strength, sets/reps, or training summary request",
        ("运动", "锻炼", "训练", "有氧", "无氧", "力量", "跑步", "椭圆机", "羽毛球", "健身", "外扩腿", "深蹲", "卧推", "硬拉", "组", "次", "分钟", "小时"),
        (r"\d+\s*(分钟|小时|h|min|组|次|个|公里|km)",),
    ),
    SkillRule(
        "daily-nutrition-deficit-tracker",
        "food, protein powder, calories, macros, deficit/surplus, or diet summary request",
        ("吃了", "喝了", "早餐", "午餐", "晚餐", "加餐", "蛋白粉", "热量", "卡路里", "蛋白质", "脂肪", "碳水", "糖分", "盐", "缺口", "盈余", "饮食", "营养"),
        (),
    ),
)


def score_rule(text: str, rule: SkillRule) -> tuple[int, list[str]]:
    lowered = text.lower()
    hits: list[str] = []
    score = 0
    for keyword in rule.keywords:
        if keyword.lower() in lowered:
            hits.append(keyword)
            score += 2
    for pattern in rule.patterns:
        if re.search(pattern, lowered, flags=re.IGNORECASE):
            hits.append(f"pattern:{pattern}")
            score += 1
    return score, hits


def route(text: str) -> dict:
    results = []
    for rule in RULES:
        score, hits = score_rule(text, rule)
        if score:
            results.append(
                {
                    "skill": rule.skill,
                    "score": score,
                    "reason": rule.reason,
                    "matches": hits[:8],
                }
            )
    results.sort(key=lambda item: item["score"], reverse=True)
    primary = None
    if results:
        clear_results = [item for item in results if item["score"] >= 4]
        if len(clear_results) > 1:
            primary = "multiple"
        else:
            primary = results[0]["skill"]
    return {
        "input": text,
        "primary_skill": primary,
        "candidates": results,
        "note": "Use multiple skills if the user logs mixed content, such as meals plus exercise plus glucose.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="User health log or request text")
    args = parser.parse_args()
    print(json.dumps(route(args.text), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
