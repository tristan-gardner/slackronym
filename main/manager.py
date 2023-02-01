from typing import List

from main.models import Definition


def get_definitions(term: str) -> List[Definition]:
    query_set = Definition.objects.filter(term=term, deleted_at__isnull=True).order_by("created_at")

    return list(query_set)


def create_definition(term: str, definition: str) -> Definition:
    defin = Definition(term=term, definition=definition)
    defin.save()

    return defin


def delete_definitions(term: str) -> None:
    Definition.objects.filter(term=term).delete()


def delete_definition(term: str, definition_number: int) -> bool:
    defs = get_definitions(term)
    if len(defs) < definition_number:
        return False
    else:
        defin = defs[definition_number - 1]
        defin.delete()
        return True
