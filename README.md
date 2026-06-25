# Health Tracker

A Codex personal health-tracking plugin for Chinese-language logs. It helps record and summarize meals, workouts, body composition, body weight, and finger-stick blood glucose readings.

Think of it as a structured health journal assistant: it turns casual natural-language notes into trackable tables, trends, targets, and practical next-step suggestions. It is not a medical diagnosis tool.

## Feature Overview

| Area | Skill | Use It For |
| --- | --- | --- |
| Nutrition and calorie deficit | `daily-nutrition-deficit-tracker` | Daily meals, protein powder, calories, protein/fat/carbs, exercise-adjusted deficit, nutrition structure summaries |
| Exercise log | `exercise-log-coach` | Cardio, strength training, sports, walking/running, sets/reps/weights, training frequency, monthly workout summaries |
| Body composition and weight | `body-composition-tracker` | InBody/body-composition reports, body weight, body fat percentage, skeletal muscle, visceral fat, BMI, weight trend charts |
| Finger-stick blood glucose | `blood-glucose-tracker` | Fasting/pre-meal/post-meal/random/bedtime glucose, mmol/L or mg/dL values, glucose trend summaries and range-aware interpretation |

## Main Capabilities

- Log Chinese natural-language health notes.
- Recognize relative dates such as "today", "yesterday", and "the day before yesterday" in the user's locale.
- Set individualized daily calorie and macro targets from height, weight, work intensity, exercise habits, and optional InBody/body-composition results.
- Estimate daily intake, protein, fat, carbohydrate, sugar, salt, and calorie deficit/surplus.
- Count wearable, treadmill, elliptical, and other activity calories conservatively to avoid overestimating exercise burn.
- Extract and track InBody/body-composition values such as body fat, skeletal muscle mass, basal metabolic rate, and visceral fat.
- Track finger-stick glucose readings by timing: fasting, pre-meal, post-meal, random, or bedtime.
- Generate summary tables and trend charts. Nutrition-structure charts prefer explicitly colored SVG/PNG output to avoid theme color issues.

## Installation

Clone this repository into your Codex plugins directory:

```bash
git clone https://github.com/yanggaomao/health-tracker.git ~/plugins/health-tracker
```

Then install or enable it as a local Codex plugin. The plugin entrypoint is:

```text
.codex-plugin/plugin.json
```

On Windows, a typical local path is:

```text
C:\Users\<your-username>\plugins\health-tracker
```

## Usage

After enabling the plugin in Codex, you can mention `health-tracker` directly or explicitly invoke one of its skills.

### 1. Set Personalized Nutrition Targets First

On first use, the nutrition module asks for a compact personal profile so it can calculate more appropriate daily calorie and macro targets.

Useful profile fields:

- Sex, age, height, and current weight
- Current goal: fat loss, recomposition, maintenance, or muscle gain
- Daily work intensity: mostly seated, light walking/standing, standing/manual mixed work, or heavy physical work
- Exercise habits: weekly frequency, type, and typical duration
- Optional InBody/body-composition report values: basal metabolic rate, body fat percentage, body fat mass, skeletal muscle mass, visceral fat, and target weight

Example:

```text
@health-tracker I want to set my daily nutrition targets first. Female, 21, 174 cm, 79 kg, goal is fat loss, mostly seated work, strength training twice per week, and I have an InBody report.
```

The plugin is designed for Chinese logs, so a Chinese prompt works naturally:

```text
@health-tracker 我想先设置每日饮食目标。女，21岁，174cm，79kg，目标减脂，工作大部分久坐，每周力量训练2次，有一张InBody报告。
```

### 2. Log Meals

Example:

```text
@health-tracker 今天早餐一根香蕉，中午板烧鸡腿堡一个、中薯一份、无糖可乐半杯，晚餐一碗米饭、鸡蛋一个、肥牛七八片。
```

The plugin estimates:

- Total calories
- Protein, fat, and carbohydrate
- Sugar and salt
- Difference from personalized targets
- Whether the day is likely in deficit, surplus, or near maintenance

### 3. Log Protein Powder

Protein powder is not estimated from a single fixed default label. The first time you log a specific protein powder, provide the package nutrition table or type the label values.

Recommended label details:

- Calories per 100 g or per serving
- Protein
- Fat
- Carbohydrate
- Sugar
- Salt or sodium
- Scoop/serving size in grams
- Product name, flavor, and version

Example:

```text
@health-tracker 今天喝了一勺蛋白粉，这款每100g：377kcal，蛋白质71g，脂肪6.1g，碳水8.2g，糖5.7g，盐0.45g；一勺30g。
```

After a label for the same product/flavor/version has already been provided, you can refer to it more casually:

```text
@health-tracker 晚餐后喝了一勺之前那款抹茶蛋白粉。
```

### 4. Log Workouts

Example:

```text
@health-tracker 今天椭圆机40分钟，外扩腿60个，羽毛球2小时。
```

The plugin organizes:

- Standardized exercise names
- Aerobic, anaerobic, or mixed-sport categories
- Duration, sets, reps, and weights
- Intensity and rough training-load estimates
- Short recovery or training notes

### 5. Log Body Weight and InBody Reports

Body-weight example:

```text
@health-tracker 今天早晨空腹体重78.6kg。
```

InBody/body-composition example:

```text
@health-tracker 这是我的InBody报告，体重显示有误，实际体重是79kg。
```

The plugin prioritizes:

- Body weight
- Skeletal muscle mass
- Body fat mass
- Body fat percentage
- BMI
- Basal metabolic rate
- Visceral fat
- Waist-hip ratio
- Total body water and segmental values

### 6. Log Finger-Stick Blood Glucose

Examples:

```text
@health-tracker 今天空腹指尖血糖5.4。
```

```text
@health-tracker 晚饭后2小时血糖7.2 mmol/L。
```

The plugin:

- Normalizes values to mmol/L and can convert to mg/dL
- Separates fasting, pre-meal, post-meal, random, and bedtime readings
- Provides general reference-range interpretation
- Flags possible low readings or repeated high readings for attention

## Summaries and Charts

You can ask:

```text
@health-tracker 总结最近两日饮食状况。
```

```text
@health-tracker 总结本月运动情况。
```

```text
@health-tracker 画一下我的体重趋势。
```

Nutrition summaries can include daily intake, estimated maintenance, raw activity calories, conservatively counted activity calories, deficit/surplus, and protein/fat/carbohydrate target ratios.

Charts are kept simple and readable. The plugin avoids crowding too many unrelated metrics into one chart.

## Important Notes

- This is a personal logging and estimation tool, not medical advice or diagnosis.
- Food estimates vary with brand, cooking method, weighing method, and portion descriptions.
- InBody and other bioelectrical impedance results can be affected by hydration, sodium intake, menstrual cycle, training, meal timing, and measurement time. Use them mainly for trends.
- Home glucose meters can be affected by strips, hand cleanliness, sampling technique, and meter accuracy. They do not replace laboratory venous blood tests.
- Seek professional medical help for concerning symptoms such as severe hypoglycemia symptoms, very high glucose with symptoms, chest pain, fainting, severe weakness, vomiting, or breathing difficulty.

## Repository Layout

```text
health-tracker/
  .codex-plugin/
    plugin.json
  scripts/
    route_health_skill.py
  skills/
    blood-glucose-tracker/
    body-composition-tracker/
    daily-nutrition-deficit-tracker/
    exercise-log-coach/
```

## License

No license has been added yet. Add a license before using this repository in a broader public or commercial setting.
