class InMemoryRepo:
    def __init__(self):
        self._store = {
        1: {"name": "John Doe", "age": 30},
        2: {"name": "Jane Smith", "age": 28},
        }


    def get(self, user_id):
        return self._store.get(user_id)


    def update(self, user_id, data: dict):
        if user_id in self._store:
            self._store[user_id].update(data)


    def delete(self, user_id):
        if user_id in self._store:
            del self._store[user_id]


repo = InMemoryRepo()