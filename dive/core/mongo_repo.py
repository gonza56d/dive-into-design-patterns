from pymongo import MongoClient

from dive.core.exceptions import NotFound


class MongoRepo:

    def __init__(self, collection: str) -> None:
        self._client = MongoClient('mongo', 27017)
        self._collection = self._client['dive-mongo-db'][collection]

    def write(self, data: dict) -> None:
        self._collection.insert_one(data)

    def read(self, **filters) -> dict:
        if (result := self._collection.find_one(filters)):
            return result
        raise NotFound()

    def filter(self, **filters) -> list[dict]:
        results = self._collection.find(filters)
        return [r for r in results]
