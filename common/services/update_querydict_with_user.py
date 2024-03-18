# typing
from users.models import User
from django.http import QueryDict


def update_querydict_with_user(querydict: QueryDict, user: User, field: str) -> QueryDict:
    updated_querydict = querydict.copy()
    updated_querydict[field] = user

    return updated_querydict
