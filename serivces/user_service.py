# services/user_service.py
from repos.in_memory import repo


def get_user_summary(user_id: int):
    user = repo.get(user_id)
    if not user:
        return f"User {user_id} not found"
    
    user_data = {
        "user_id": user_id,
        "name": user['name'],
        "age": user['age']
    }
    
    return user_data;     


def update_user_name(user_id: int, new_name: str) -> str:
    if repo.get(user_id) is None:
        return f"User {user_id} not found"
    repo.update(user_id, {"name": new_name})
    return f"User {user_id} updated to {new_name}"


def delete_user(user_id: int) -> str:
    if repo.get(user_id) is None:
        return f"User {user_id} not found"
    repo.delete(user_id)
    return f"User {user_id} deleted"