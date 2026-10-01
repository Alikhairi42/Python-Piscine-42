from .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    data: list[str] = dark_spell_allowed_ingredients()
    for item in data:
        if item == ingredients:
            return f"{ingredients} - VALID"
        else:
            return f"{ingredients} - INVALID"