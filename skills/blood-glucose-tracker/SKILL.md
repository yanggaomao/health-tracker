---
name: blood-glucose-tracker
description: "Chinese-language finger-stick blood glucose tracking and visualization for Health Tracker. Use when the user records fasting glucose, pre-meal glucose, post-meal glucose, random glucose, bedtime glucose, glucometer readings, mmol/L or mg/dL values, asks whether a reading is normal, or asks to summarize glucose trends and charts."
---

# Blood Glucose Tracker

## Core Behavior

Use Chinese by default. Track finger-stick glucose readings with meal timing and context. This skill supports personal logging and trend review, not diagnosis. Home glucose meter readings can be affected by meter accuracy, strip storage, hand cleanliness, and technique.

Read `references/glucose-ranges.md` when interpreting ranges, thresholds, or chart bands.

## Entry Schema

For each reading, record:

| Field | Guidance |
| --- | --- |
| date | YYYY-MM-DD |
| time | HH:MM if known |
| value | Normalize to mmol/L and optionally mg/dL |
| unit | mmol/L or mg/dL |
| timing | fasting, pre-meal, 1h-post-meal, 2h-post-meal, random, bedtime, unknown |
| meal_context | Meal content, carbs, unusually large meal, snack |
| activity_context | Exercise before/after reading |
| medication_context | Only if user provides; do not infer |
| symptoms | Hypoglycemia symptoms, thirst, dizziness, etc. |
| notes | Assumptions or repeat-test suggestion |

If the unit is missing:

- Values <= 30 are usually mmol/L; assume mmol/L and state the assumption.
- Values > 30 are usually mg/dL; convert to mmol/L and state the assumption.
- Ask for confirmation if the value is close to a clinically important threshold or looks implausible.

Conversion:

- `mmol/L = mg/dL / 18`
- `mg/dL = mmol/L * 18`

## Timing Rules

Normalize common wording:

- "空腹" -> fasting
- "餐前" -> pre-meal
- "饭前" -> pre-meal
- "饭后1小时" / "餐后一小时" -> 1h-post-meal
- "饭后2小时" / "餐后两小时" -> 2h-post-meal
- "随机" / "随便测了一下" -> random
- "睡前" -> bedtime

If the user says "餐后" without time, ask whether it was about 1 hour or 2 hours after the meal. If continuing without an answer, log as post-meal-unknown and avoid strict interpretation.

## Interpreting Readings

Use `references/glucose-ranges.md` for reference ranges and target bands. In normal responses:

- Compare readings to the appropriate timing band.
- Distinguish "general nonpregnant adult reference range" from "diabetes-management target range".
- Avoid diagnosing diabetes from home readings.
- Encourage repeat measurement or professional advice for repeated abnormal readings.

Urgency notes:

- If glucose is below 3.9 mmol/L / 70 mg/dL, flag possible hypoglycemia and advise following established hypoglycemia guidance or seeking help if symptoms are severe.
- If glucose is very high, repeated, or paired with concerning symptoms such as vomiting, confusion, severe weakness, chest pain, or difficulty breathing, advise prompt medical help.

## Visualization

When the user asks for glucose visualization or summary, prefer:

- A time-series dot/line chart with date-time on x-axis and glucose on y-axis.
- Color or shape by timing: fasting/pre-meal/post-meal/random/bedtime.
- Background target bands instead of a single mixed threshold.
- A table grouped by timing category.
- Time-in-range style percentages when enough readings exist.

Suggested simple colors:

- Fasting/pre-meal: blue
- Post-meal: orange
- Random/bedtime: purple
- Below range: red marker
- Above range: amber marker
- Target band: light green or light blue background

Keep the chart clean and readable. Do not overdecorate.

## Summary Output

When the user asks to summarize blood glucose:

1. Show count of readings by timing category.
2. Show average, min, max for fasting/pre-meal/post-meal if enough data exists.
3. Highlight repeated lows or highs.
4. Connect patterns to context the user provided, such as meal composition, exercise, sleep, or illness.
5. State key assumptions and missing data, especially unit or meal timing.

Do not merge blood glucose charts with nutrition or body-weight charts unless the user explicitly asks for a combined dashboard.
