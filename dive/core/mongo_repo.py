from pymongo import MongoClient

from dive.core.exceptions import NotFound


class MongoRepo:

    def __init__(self, collection: str) -> None:
        self._client = MongoClient('mongo', 27017)
        self._collection = self._client['dive-mongo-db'][collection]

    def write(self, data: dict) -> None:
        try:
            self.read(owner_name=data['owner_name'])
        except NotFound:
            self._collection.insert_one(data)

    def read(self, **filters) -> dict:
        if (result := self._collection.find_one(filters)):
            del result['_id']
            return result
        raise NotFound()

    def filter(self, **filters) -> list[dict]:
        results = self._collection.find(filters)
        result = []
        for r in results:
            del r['_id']
            result.append(results)
        return result

    def delete(self, **filters) -> None:
        self._collection.delete_one(filters)

    def update(self, filter: dict, new_values: dict) -> None:
        self._collection.update_one(filter, {'$set': new_values})
