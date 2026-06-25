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

### 2. Log Meals

Example:

```text
@health-tracker Today I had one banana for breakfast. For lunch I had one McDonald's grilled chicken thigh burger, one medium fries, and half a cup of diet cola. For dinner I had one bowl of rice, one egg, and seven or eight slices of fatty beef.
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
@health-tracker Today I had one scoop of protein powder. Its label says per 100 g: 377 kcal, 71 g protein, 6.1 g fat, 8.2 g carbs, 5.7 g sugar, and 0.45 g salt. One scoop is 30 g.
```

After a label for the same product/flavor/version has already been provided, you can refer to it more casually:

```text
@health-tracker After dinner I had one scoop of the same matcha protein powder as before.
```

### 4. Log Workouts

Example:

```text
@health-tracker Today I did 40 minutes on the elliptical, 60 reps on the hip abduction machine, and played badminton for 2 hours.
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
@health-tracker My morning fasted weight today was 78.6 kg.
```

InBody/body-composition example:

```text
@health-tracker This is my InBody report. The weight shown on the report is wrong; my actual weight should be 79 kg.
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
@health-tracker Today's fasting finger-stick glucose was 5.4 mmol/L.
```

```text
@health-tracker My glucose was 7.2 mmol/L two hours after dinner.
```

The plugin:

- Normalizes values to mmol/L and can convert to mg/dL
- Separates fasting, pre-meal, post-meal, random, and bedtime readings
- Provides general reference-range interpretation
- Flags possible low readings or repeated high readings for attention

## Summaries and Charts

You can ask:

```text
@health-tracker Summarize my diet over the last two days.
```

```text
@health-tracker Summarize my workouts for this month.
```

```text
@health-tracker Draw my body-weight trend.
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
