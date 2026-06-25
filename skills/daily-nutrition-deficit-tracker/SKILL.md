---
name: daily-nutrition-deficit-tracker
description: "Chinese-language daily diet and activity tracking for first-use personalized nutrition target setup, meal logging, protein powder intake, exercise-adjusted calorie deficit or surplus, macro structure, high-activity tags, and summary tables/charts. Use when the user logs food, snacks, protein powder, steps, watch/bracelet activity calories, workouts, height/weight/work intensity/InBody or body-composition context for diet targets, asks about today's calorie gap or nutrition structure, or says \"总结\" to create a multi-day summary."
---

# Daily Nutrition Deficit Tracker

## Core Behavior

Use Chinese by default. Treat the conversation as a running daily nutrition log unless the user specifies a date range or asks for a standalone calculation.

Record each dated entry with estimated calories, protein, fat, carbohydrate, sugar, salt, activity, counted activity calories, high-activity tag status, and assumptions. If the user gives vague food amounts, estimate conservatively and state the key assumption. Ask a concise clarification only when the missing value changes the result materially, such as an unknown scoop size, unknown body weight for target macros, or unknown maintenance calories.

Keep calculations practical rather than falsely precise. Round daily calories to the nearest 10 kcal and macros to 0.5-1 g unless a label gives exact values.

Do not present this as medical advice. Treat it as an estimation aid for diet tracking and fat-loss planning.

## First-Use Personalization

On first use, or when no personalized daily nutrition targets are known, ask once for a compact profile before setting calorie and macro targets:

- Sex, age, height, current weight, and current goal: fat loss, recomposition, maintenance, or muscle gain.
- Daily work intensity: mostly seated, light walking/standing, standing/manual mixed work, or heavy physical work.
- Regular exercise pattern if known: strength/cardio frequency and typical duration.
- Recent InBody/body-composition data if available: measured BMR, body fat percentage, fat mass, skeletal muscle mass, fat-free mass/lean mass, visceral fat area/level, target weight, and measurement date. Accept a report photo and use `body-composition-tracker` when extraction is needed.

Do not block routine food logging if the user wants to continue immediately. If profile fields are missing, log the food, use clearly marked provisional targets, and ask for only the most important missing fields at the end.

Store the working target profile in the conversation context:

| Field | Guidance |
| --- | --- |
| profile_date | Date the target profile was set or revised |
| sex_age_height_weight | Normalize height to cm and weight to kg |
| goal | fat loss, recomposition, maintenance, muscle gain |
| work_intensity | mostly seated, light active, standing/manual mixed, heavy physical |
| exercise_pattern | Weekly frequency and type, if provided |
| body_composition | InBody/body-composition values and measurement date |
| target_calories | Daily kcal target or range |
| target_protein_g | Daily protein target |
| target_fat_g | Daily fat target |
| target_carbs_g | Daily carbohydrate target |
| assumptions | Missing fields, provisional multipliers, or reason for using measured BMR |

## Protein Powder Labels

Do not assume all protein powders use the previous matcha latte nutrition label. When the user logs protein powder, first check whether the user has already provided or uploaded a nutrition label for that exact product/flavor/version in the current conversation or stored context.

If the matching label is known, reuse it and state the product/flavor/version being applied. Scale directly from the label by serving grams or by the user's scoop size.

If no matching label is known, ask the user to provide the detailed nutrition table before estimating calories and macros. Request at least calories, protein, fat, carbohydrate, sugar, salt/sodium, serving size, and whether the label is per serving or per 100 g. If the user says "one scoop" or "一勺", ask for scoop grams as well.

Do not block the rest of the meal log while waiting for the label. If the user wants to continue immediately, log protein powder as `nutrition_label_pending`, exclude it from precise totals or mark a clearly provisional estimate, and revise the day's totals once the label is provided.

When a label is provided, store a reusable product profile in the conversation context:

| Field | Guidance |
| --- | --- |
| product_name | Brand/product/flavor/version if visible |
| label_basis | per 100 g or per serving |
| serving_size_g | Serving or scoop size in grams |
| calories | kcal |
| protein_g | Protein |
| fat_g | Fat |
| carbs_g | Carbohydrate |
| sugar_g | Sugar, if shown |
| salt_or_sodium | Prefer salt in g; convert sodium to salt only if needed and mark assumption |
| source | Uploaded label, user typed label, or package photo |

## Food Estimation

Prefer nutrition labels, restaurant data, package weights, and cooked weights when the user provides them. Otherwise estimate with common Chinese household portions and say what was assumed.

Track at least calories, protein, fat, carbohydrate, sugar, and salt when possible. Keep sugar and salt out of the main macro-ratio line chart unless the user asks, because they are limits rather than target macro structures.

When the user says "今天吃了..." without a date, use today's date in the user's locale. If the user provides entries across multiple days, keep them separate by date.

## Maintenance Calories and Ideal Structure

Use the user's provided maintenance calories, daily calorie target, or ideal macro targets if available.

If these are missing, run the first-use personalization flow above. If the user wants a provisional answer immediately, calculate with clearly labeled assumptions:

- Prefer a recent plausible InBody measured BMR when available; otherwise estimate BMR with Mifflin-St Jeor when sex, age, height, and weight are known.
- Estimate maintenance from work intensity unless the user provides another baseline: mostly seated `BMR x 1.2`, light walking/standing `BMR x 1.35`, standing/manual mixed work `BMR x 1.45-1.55`, heavy physical work `BMR x 1.65-1.8`.
- Treat ordinary daily walking around 3000-5000 steps as already included in sedentary maintenance.
- For fat loss, set a provisional calorie target as maintenance minus 300-500 kcal or about 15-25% below maintenance unless the user gives a different target. Avoid pushing routine targets far below measured/estimated BMR unless the user explicitly asks or clinician guidance is provided.
- For maintenance, use estimated maintenance. For recomposition, use maintenance to `-300 kcal` depending on body fat and training. For muscle gain, use maintenance plus `150-300 kcal`.
- Set protein from the user's goal and body composition. For fat loss or recomposition, use about `1.6-2.0 g/kg current body weight`; if body fat is high or target weight is known, prefer about `1.8-2.2 g/kg target body weight` or `2.0-2.4 g/kg fat-free mass` so protein is not inflated solely by body fat.
- Set fat target to about `0.6-0.8 g/kg body weight` or target body weight, with a practical floor around `40 g/day` for most adults unless a clinician-provided plan says otherwise.
- Set carbohydrate target from remaining target calories: `(target_kcal - protein_g*4 - fat_g*9) / 4`.
- On high-activity or training days, keep protein similar, keep fat in range, and add most extra calories as carbohydrates unless the user provides another preference.

For summary line charts, calculate each nutrition structure's relative proportion as:

`actual_daily_amount / ideal_daily_amount * 100%`

Use protein, fat, and carbohydrate as the default structure lines. Add calories, sugar, or salt only if the user explicitly wants those lines or has clear targets for them.

## Activity Calories

Include activity in calorie deficit/surplus calculations. Keep display and deficit math separate:

- Raw activity calories are what a watch, bracelet, treadmill, elliptical, or gym machine reports.
- Counted activity calories are the conservative amount used in the deficit calculation.

Use these rules:

- Ordinary daily walking of 3000-5000 steps: count 0 extra kcal, because it is already included in sedentary maintenance.
- Walking around 8000-10000 steps: count extra walking conservatively if no watch activity calories are available.
- Walking at or above 10000 steps: count extra walking if no watch activity calories are available.
- If only steps are available, estimate extra walking above 5000 steps. If body weight is known, use about `0.00045 * body_weight_kg * extra_steps`; otherwise use about `0.03 kcal * extra_steps`, then round conservatively.
- Watch or bracelet activity calories at 400 kcal or more: record the raw value, but use only 60%-70% for fat-loss deficit calculations. Default to 65% when one number is needed.
- Deliberate exercise such as running, elliptical, cycling, swimming, or strength training: record it separately, but use only 70%-80% of the watch/machine value. Default to 75% when one number is needed.

Avoid double counting. If a full-day watch activity value likely includes a workout, prefer the watch value once and apply the 60%-70% factor. Add a separate workout only when the user says the values are separate or the overlap is clearly avoidable.

Calculate daily deficit as:

`deficit_kcal = maintenance_kcal + counted_activity_kcal - intake_kcal`

Use positive wording for results:

- `缺口 350 kcal` when `deficit_kcal` is positive.
- `盈余 180 kcal` when `deficit_kcal` is negative.
- `基本持平` when the absolute value is small, roughly under 50 kcal.

## High-Activity Tag

Use a separate "高活动日" tag only for table display. Do not use the tag's threshold as the counted calorie value.

Apply the tag when the watch or bracelet's raw activity calories are greater than 500 kcal for that day. Use the raw wearable value, not the conservative counted value. If no raw watch/bracelet activity calorie value is provided, do not infer the tag from steps or counted exercise unless the user explicitly asks.

Show the tag where it is visible at a glance in summaries.

## Daily Response Pattern

For a normal daily log entry, respond with a compact update:

- Today's estimated intake so far.
- Protein/fat/carbohydrate structure and obvious imbalance.
- Counted activity calories if activity was provided.
- Current deficit/surplus if maintenance can be estimated.
- One practical note, such as protein still short, fat high, or activity was conservatively counted.

Do not generate the multi-day table/chart until the user says "总结" or explicitly asks for a summary.

## Summary Output

When the user says "总结", summarize all logged days in the current conversation unless the user gives a date range.

Include:

1. A short plain-language overview of the trend.
2. A table with each date clearly visible.
3. A line chart showing nutrition structure as a percentage of ideal structure.
4. A short assumptions note if any major values were estimated.

Prefer an HTML table when color-coding is needed. Use two rows per date when possible:

- Date row: show the date and visible tags such as `高活动日`.
- Data row: show intake, maintenance, raw activity, counted activity, deficit/surplus, protein ratio, fat ratio, carb ratio, and notes.

Color only the deficit/surplus cell:

- Deficit: green; larger deficits use darker green.
- Surplus: red; larger surpluses use darker red.
- Unknown or near-even: neutral gray.

Use these practical heat colors unless a better local style is needed:

| Result | Range | Color |
| --- | --- | --- |
| Deficit | 1-200 kcal | `#e8f5e9` |
| Deficit | 201-400 kcal | `#c8e6c9` |
| Deficit | 401-700 kcal | `#81c784` |
| Deficit | >700 kcal | `#388e3c` with light text |
| Surplus | 1-200 kcal | `#ffebee` |
| Surplus | 201-400 kcal | `#ffcdd2` |
| Surplus | 401-700 kcal | `#ef9a9a` |
| Surplus | >700 kcal | `#e53935` with light text |

Keep the line chart independent from the red/green heat colors. Use blue, orange, and purple by default:

- Protein: `#2563eb`
- Fat: `#f97316`
- Carbohydrate: `#7c3aed`

For chart images where color accuracy matters, or when the user reports that Mermaid/theme colors are wrong, generate a standalone SVG or PNG artifact instead of relying on Mermaid defaults. Set explicit line strokes to the colors above, include a visible legend, label each point with its percentage, and show the rendered image inline when possible. If creating both formats, keep the SVG as the editable source and render/export a PNG for easy viewing.

Label the y-axis as `占每日理想结构比例(%)`. Treat 100% as hitting the target. If generating the chart directly in chat, use a format that can show multiple lines and a legend; if color control is limited, state the intended colors beside the chart. If generating an HTML/SVG artifact, set the line strokes explicitly to the colors above.

Do not let table red/green colors affect line colors or legend colors.
