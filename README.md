# Health Tracker

一个面向中文使用场景的 Codex 个人健康追踪插件，用来记录和总结饮食、运动、体成分/体重和指尖血糖。

它更像一个结构化健康日志助手：帮你把零散的自然语言记录整理成可追踪的表格、趋势、目标和下一步建议。它不提供医学诊断。

## 功能概览

| 模块 | Skill | 适合记录/询问 |
| --- | --- | --- |
| 饮食与热量缺口 | `daily-nutrition-deficit-tracker` | 每日饮食、蛋白粉、热量、蛋白质/脂肪/碳水、运动后热量缺口、营养结构总结 |
| 运动日志 | `exercise-log-coach` | 有氧、力量训练、球类、步行/跑步、组数次数重量、训练频率和月度运动总结 |
| 体成分与体重 | `body-composition-tracker` | InBody/体成分报告、体重、体脂率、骨骼肌、内脏脂肪、BMI、体重趋势图 |
| 指尖血糖 | `blood-glucose-tracker` | 空腹/餐前/餐后/随机/睡前血糖，mmol/L 或 mg/dL，血糖趋势和范围解读 |

## 主要能力

- 用中文记录自然语言健康日志。
- 自动识别日期表达，例如“今天”“昨天”“前天”。
- 根据身高、体重、工作强度、运动习惯和 InBody/体成分结果，为每个人设置不同的每日热量和宏量营养目标。
- 估算每日摄入、蛋白质、脂肪、碳水、糖、盐，以及热量缺口/盈余。
- 对手表、手环、跑步机、椭圆机等活动热量进行保守折算，减少过度高估。
- 记录 InBody/body composition 报告中的体脂、骨骼肌、基础代谢、内脏脂肪等指标。
- 记录指尖血糖，并区分空腹、餐前、餐后、随机、睡前等时点。
- 在总结时生成表格和趋势图；营养结构图会优先使用明确配色的 SVG/PNG，避免主题颜色混乱。

## 安装

把这个仓库克隆到你的 Codex 插件目录，例如：

```bash
git clone https://github.com/yanggaomao/health-tracker.git ~/plugins/health-tracker
```

然后在 Codex 中把它作为本地插件安装或启用。插件入口文件在：

```text
.codex-plugin/plugin.json
```

如果你是在 Windows 上使用，可以克隆到类似路径：

```text
C:\Users\<你的用户名>\plugins\health-tracker
```

## 使用方式

在 Codex 中启用插件后，可以直接提到 `health-tracker`，也可以显式调用某个 skill。

### 1. 首次设置饮食目标

首次使用饮食模块时，插件会询问个人资料，用来计算更合适的每日热量和宏量营养目标：

- 性别、年龄、身高、体重
- 当前目标：减脂、重组、维持或增肌
- 日常工作强度：久坐、轻度走动/站立、站立/体力混合、重体力
- 运动习惯：每周频率、类型和时长
- 可选：InBody/体成分报告，如基础代谢、体脂率、体脂肪量、骨骼肌量、内脏脂肪、目标体重

示例：

```text
@health-tracker 我想先设置每日饮食目标。女，21岁，174cm，79kg，目标减脂，工作大部分久坐，每周力量训练2次，有一张InBody报告。
```

### 2. 记录饮食

```text
@health-tracker 今天早餐一根香蕉，中午板烧鸡腿堡一个、中薯一份、无糖可乐半杯，晚餐一碗米饭、鸡蛋一个、肥牛七八片。
```

插件会估算：

- 总热量
- 蛋白质、脂肪、碳水
- 糖和盐
- 距离个人目标的差距
- 当天可能是缺口、盈余还是基本持平

### 3. 记录蛋白粉

蛋白粉不会默认套用某一款固定营养表。第一次记录某个蛋白粉时，需要提供包装营养表或手打营养信息。

建议提供：

- 每 100g 或每份的热量
- 蛋白质
- 脂肪
- 碳水
- 糖
- 盐或钠
- 每勺/每份克数
- 产品名、口味和版本

示例：

```text
@health-tracker 今天喝了一勺蛋白粉，这款每100g：377kcal，蛋白质71g，脂肪6.1g，碳水8.2g，糖5.7g，盐0.45g；一勺30g。
```

同款产品的营养表已经提供过后，后续可以直接说：

```text
@health-tracker 晚餐后喝了一勺之前那款抹茶蛋白粉。
```

### 4. 记录运动

```text
@health-tracker 今天椭圆机40分钟，外扩腿60个，羽毛球2小时。
```

插件会整理：

- 标准动作名
- 有氧/无氧/混合运动分类
- 时长、组数、次数、重量
- 强度和训练负荷估计
- 简短恢复或训练建议

### 5. 记录体重和 InBody

```text
@health-tracker 今天早晨空腹体重78.6kg。
```

也可以上传或描述 InBody/体成分报告：

```text
@health-tracker 这是我的InBody报告，体重显示有误，实际体重是79kg。
```

插件会优先提取：

- 体重
- 骨骼肌量
- 体脂肪量
- 体脂率
- BMI
- 基础代谢
- 内脏脂肪
- 腰臀比
- 身体水分和分段数据

### 6. 记录指尖血糖

```text
@health-tracker 今天空腹指尖血糖5.4。
```

```text
@health-tracker 晚饭后2小时血糖7.2 mmol/L。
```

插件会：

- 统一单位为 mmol/L，并可换算 mg/dL
- 区分空腹、餐前、餐后、随机、睡前
- 给出一般参考范围下的趋势解读
- 标记低血糖或反复偏高等需要关注的情况

## 总结和图表

可以直接说：

```text
@health-tracker 总结最近两日饮食状况。
```

```text
@health-tracker 总结本月运动情况。
```

```text
@health-tracker 画一下我的体重趋势。
```

饮食总结会包含每日摄入、维持消耗、活动热量、缺口/盈余、蛋白质/脂肪/碳水达标率等。图表会尽量保持清晰，不把太多指标挤在同一张图里。

## 注意事项

- 这是个人记录和估算工具，不是医学建议或诊断工具。
- 食物估算会受品牌、烹调方式、称重方式和份量描述影响。
- InBody 等生物电阻抗结果会受水分、盐分、经期、训练、进食时间和测量时间影响，更适合看趋势。
- 家用血糖仪会受试纸、手部清洁、采血方式和仪器误差影响，不能替代医院静脉血检测。
- 如果出现明显低血糖症状、极高血糖、胸痛、晕厥、严重乏力、呕吐、呼吸困难等情况，请及时寻求专业医疗帮助。

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
