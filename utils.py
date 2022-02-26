import json


def data_load():
    """
    читает json файл, выводит список кандидатов
    :return: список кандидатов
    """
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
        return candidates


def get_candidate_id(uid):
    """
    принимает номер кандидата, выбирает его из списка, возвращает данные по кандидата
    :param uid:
    :return: данные кандидата
    """
    candidates = data_load()
    for candidate in candidates:
        if candidate["id"] == uid:
            return candidate


def get_candidate_skill(skill):
    """
    принимает скилл, находит его в списках кандидатов, возвращает
    список кандидатов с данным скилом
    :param skill: скилл
    :return: список данных кондидатов с запрошеным скилом
    """
    candidates = data_load()
    skill_lower = skill.lower()
    skill_candidates = []

    for candidate in candidates:
        if skill_lower in candidate["skills"].lower().split(", "):
            skill_candidates.append(candidate)

    return skill_candidates


print(get_candidate_skill("python"))
