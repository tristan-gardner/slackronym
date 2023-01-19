from typing import List

from main.models import Definition


def get_definitions(term: str) -> List[Definition]:
    query_set = Definition.objects.filter(term=term).order_by("created_at")

    return list(query_set)


def create_definition(term: str, definition: str) -> Definition:
    defin = Definition(term=term, definition=definition)
    defin.save()

    return defin
