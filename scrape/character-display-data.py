import json

with open("character.json", "r", encoding="utf-8") as f:
    lol = json.load(f)

stats = lol.get("Stats", {})

stat_codes = {
    "Impact": 12201,
    "CRIT Rate": 20101,
    "Base ATK": 12101,
    "Base Energy Regen": 30501,
    "CRIT DMG": 21101,
    "Anomaly Proficiency": 31201,
    "Anomaly Mastery": 31401,
    "PEN Ratio": 23101,
    "HP": 11101
}

def calc_stat(level: int, stats: dict, data: dict,field: str, field_growth:str) -> int:
    if field=="Attack":
        code=12101
    elif  field=="HpMax":
        code=11101
    next_level = level + 1 if level != 6 else 6
    core_bonus=get_bonus(next_level,code,data)
    char_level = level * 10
    base_atk = stats.get(field, 0)
    atk_growth = stats.get(field_growth, 0) / 10000
    growth_part = atk_growth * (char_level - 1)
    level_bonus = data.get("Level", {}).get(str(next_level), {}).get(field, 0)

    
    core_bonus,max_level=get_bonus(next_level,code,data)
    print(f"Max Level: {max_level}, Character Level: {char_level}")

    if max_level<=char_level :
        total=base_atk + growth_part + level_bonus+core_bonus
    else:
        total=base_atk + growth_part + level_bonus

    return total


def get_bonus(lvl, code, data):
    lvl_key = str(lvl)

    extra_levels = data.get("ExtraLevel", {})
    entry = extra_levels[lvl_key]
    max_level = entry.get("MaxLevel")
    extras = entry.get("Extra", {})

    code_str = str(code)
    value = extras[code_str].get("Value")
    return value, max_level

def get_first_extra(level: int, data: dict):
    lvl_key = str(level)

    extra_levels = data.get("ExtraLevel", {})
    entry = extra_levels.get(lvl_key)
    if not entry:
        return None

    extras = entry.get("Extra", {})
    if not extras:
        return None

    first_key = next(iter(extras), None)
    if not first_key:
        return None
    code=extras[first_key]["Prop"]
    value=extras[first_key]["Value"]
    
    return code,value 







# max_level = 6

# print("\nHP Growth by Level:")
# for lvl in range(1, max_level + 1):
#     hp = calc_stat(lvl, stats, lol,"Attack","AttackGrowth")
#     char_lvl=lvl*10
#     print(f"Level {lvl}: HP = {int(hp)} Char= {char_lvl} ")


# with open("character-stats.json", "w", encoding="utf-8") as f:
#     json.dump(stats, f, indent=2, ensure_ascii=False)
get_first_extra(1,lol)
