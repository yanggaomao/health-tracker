# Health Tracker

Personal Codex plugin for Chinese-language health tracking.

## What It Includes

- Daily nutrition logging, calorie deficit/surplus estimates, macro structure summaries, and personalized first-use calorie/macro target setup.
- Exercise logging and workout pattern summaries.
- InBody/body-composition and daily body-weight tracking.
- Finger-stick blood glucose logging and range-aware summaries.

## Plugin Structure

```text
health-tracker/
  .codex-plugin/plugin.json
  scripts/route_health_skill.py
  skills/
    blood-glucose-tracker/
    body-composition-tracker/
    daily-nutrition-deficit-tracker/
    exercise-log-coach/
```

## Notes

This plugin is for personal tracking and estimation, not medical diagnosis. Bioelectrical impedance, home glucose meters, wearable activity calories, and food estimates can all vary with measurement conditions and assumptions.

Protein powder estimates require a matching uploaded or typed nutrition label before precise calories and macros are applied.
