from typing import Optional


def user_entity(item) -> dict:
    return {
        #"id": item["id"],
        "name": str(item["name"]),
        "mark": int(item["mark"])
    }


def users_entity(entity) -> list:
    return [user_entity(item) for item in entity]
