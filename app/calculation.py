from motor.core import AgnosticCollection


def get_best_match(matching_patterns: list[dict[str, str]]) -> dict[str, str]:
    return sorted(matching_patterns, key=lambda pattern: len(pattern), reverse=True)[0]


def is_match(pattern: dict[str, str], form_data: dict[str, str]) -> bool:
    for p_key, p_value in pattern.items():
        if p_key not in ('_id', 'name'):
            f_value = form_data.get(p_key)
            if f_value is None or f_value != p_value:
                return False
    return True


async def find_pattern(coll: AgnosticCollection, form_data: dict[str, str]) -> dict[str, str]:
    matching_patterns = []
    for field_name, field_type in form_data.items():
        cursor = coll.find({field_name: field_type})
        async for pattern in cursor:
            if is_match(pattern, form_data):
                matching_patterns.append(pattern)
    if not matching_patterns:
        return form_data
    name = get_best_match(matching_patterns)['name']
    return {'pattern_name': name}
