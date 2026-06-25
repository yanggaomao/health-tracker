---
name: body-composition-tracker
description: "Chinese-language body composition and body weight tracking for Health Tracker. Use when the user uploads InBody or body-composition reports, reports daily body weight, target weight, body fat, skeletal muscle, visceral fat, BMI, waist-hip ratio, or asks to compare body metrics over time or generate weight/body-composition trend charts."
---

# Body Composition Tracker

## Core Behavior

Use Chinese by default. Track two related streams:

1. InBody/body-composition report records.
2. Daily body weight records.

Treat bioelectrical impedance results as trend estimates, not precise medical measurements. Mention that hydration, sodium, menstrual cycle, training, food timing, and measurement time can affect InBody values.

## InBody Intake

When the user uploads or describes an InBody report, extract and record the report date and all visible numeric fields. If the date is missing, ask once; if the user wants to continue, use the upload/log date and mark it as assumed.

Prioritize these fields when visible:

| Field | Notes |
| --- | --- |
| weight | kg |
| skeletal_muscle_mass | 骨骼肌量, kg |
| body_fat_mass | 体脂肪量, kg |
| body_fat_percent | 体脂率, % |
| BMI | kg/m2 |
| visceral_fat_level | 内脏脂肪等级 |
| basal_metabolic_rate | 基础代谢, kcal |
| waist_hip_ratio | 腰臀比 |
| total_body_water | 身体水分 |
| segmental_lean | 分段肌肉/瘦体重 |
| segmental_fat | 分段脂肪 |
| InBody score | if shown |

If a photo is blurry or a field is uncertain, mark it as uncertain instead of guessing.

## InBody Analysis

For a first report, provide:

- A concise snapshot: weight, body fat %, skeletal muscle mass, fat mass, visceral fat level, BMR.
- One interpretation of current structure, such as fat-loss priority, muscle-maintenance priority, or recomposition.
- One or two action-oriented notes that connect to diet and exercise modules without giving medical advice.

For a later report, compare against the previous comparable InBody record:

- Weight delta.
- Body fat mass and body fat percentage delta.
- Skeletal muscle mass delta.
- Visceral fat level delta.
- BMR delta if available.
- Whether changes look like fat loss, muscle gain/loss, water fluctuation, or mixed change.

Prefer trend language over judgmental language.

## Daily Weight

Daily body weight belongs to this skill. Record each entry by date:

| Field | Guidance |
| --- | --- |
| date | YYYY-MM-DD |
| weight_kg | Normalize to kg |
| timing | morning fasted, after meal, evening, unknown |
| notes | period, high sodium meal, travel, workout soreness, etc. |

If the user gives jin/斤, convert to kg by dividing by 2. If the unit is missing and the number is likely body weight in China, ask or infer kg/jin based on plausibility and state the assumption.

## Weight Trend Chart

When the user asks for weight trend, body trend, or summary:

- Generate a clean weight curve with date on x-axis and body weight on y-axis.
- Add a clearly marked target-weight reference line if the target weight is known.
- If no target is known, ask once; if no answer, generate the chart without a target line.
- Use simple attractive colors: main weight line in blue or teal, 7-day average in purple or green, target line as a dashed neutral/red line.
- Keep the chart simple and not flashy. Avoid decorative clutter.
- If enough data exists, include a 7-day moving average to reduce daily water noise.

For InBody trend charts, use separate lines or small tables for body fat %, skeletal muscle mass, and fat mass. Do not mix too many metrics into one crowded chart.

## Summary Output

When summarizing body composition:

1. Show a table of InBody records and key deltas.
2. Show a daily weight table or chart.
3. Explain whether the trend supports the user's stated goal.
4. Note possible confounders such as hydration or measurement timing.
5. Suggest one practical next measurement habit, such as same time of day and similar pre-test conditions.

If the user reports alarming symptoms, very rapid unexplained weight change, or medically concerning values, advise consulting a clinician.
