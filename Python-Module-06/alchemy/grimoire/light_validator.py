def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    data: list[str] = light_spell_allowed_ingredients()
    for item in data:
        if item == ingredients:
            return f"{ingredients} - VALID"
        else:
            return f"{ingredients} - INVALID"