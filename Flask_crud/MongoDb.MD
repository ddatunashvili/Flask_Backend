
# Pymongo methods

## 1 **Create (Insert)**

- **`insert_one(document)`**: Inserts a single document into a collection.

  ```python
  result = mongo.db.collection_name.insert_one({'name': 'John Doe', 'email': 'john@example.com'})
  print('Inserted document id:', result.inserted_id)
  ```

- **`insert_many(documents)`**: Inserts multiple documents into a collection.

  ```python
  result = mongo.db.collection_name.insert_many([
      {'name': 'Jane Doe', 'email': 'jane@example.com'},
      {'name': 'Alice Smith', 'email': 'alice@example.com'}
  ])
  print('Inserted document ids:', result.inserted_ids)
  ```

## 2 **Read (Query)**

- **`find(query)`**: Retrieves all documents matching a query Returns a cursor.

  ```python
  cursor = mongo.db.collection_name.find({'name': 'John Doe'})
  for document in cursor:
      print(document)
  ```

- **`find_one(query)`**: Retrieves a single document matching a query.

  ```python
  document = mongo.db.collection_name.find_one({'name': 'John Doe'})
  print(document)
  ```

- **`find_one_and_update(filter, update, return_document=ReturnDocument.AFTER)`**: Finds a document, updates it, and returns the updated document.

  ```python
  from pymongo import ReturnDocument
  updated_document = mongo.db.collection_name.find_one_and_update(
      {'name': 'John Doe'},
      {'$set': {'email': 'john.doe@example.com'}},
      return_document=ReturnDocument.AFTER
  )
  print(updated_document)
  ```

## 3 **Update**

- **`update_one(filter, update)`**: Updates a single document that matches the filter.

  ```python
  result = mongo.db.collection_name.update_one(
      {'name': 'John Doe'},
      {'$set': {'email': 'john.doe@example.com'}}
  )
  print('Matched count:', result.matched_count)
  print('Modified count:', result.modified_count)
  ```

- **`update_many(filter, update)`**: Updates multiple documents that match the filter.

  ```python
  result = mongo.db.collection_name.update_many(
      {'status': 'pending'},
      {'$set': {'status': 'completed'}}
  )
  print('Matched count:', result.matched_count)
  print('Modified count:', result.modified_count)
  ```

## 4 **Delete**

- **`delete_one(filter)`**: Deletes a single document that matches the filter.

  ```python
  result = mongo.db.collection_name.delete_one({'name': 'John Doe'})
  print('Deleted count:', result.deleted_count)
  ```

- **`delete_many(filter)`**: Deletes multiple documents that match the filter.

  ```python
  result = mongo.db.collection_name.delete_many({'status': 'expired'})
  print('Deleted count:', result.deleted_count)
  ```

## 5 **Other Useful Methods**

- **`count_documents(filter)`**: Counts the number of documents matching the filter.

  ```python
  count = mongo.db.collection_name.count_documents({'status': 'active'})
  print('Document count:', count)
  ```

- **`aggregate(pipeline)`**: Performs aggregation operations (e.g., grouping, filtering).

  ```python
  pipeline = [
      {'$match': {'status': 'active'}},
      {'$group': {'_id': '$category', 'total': {'$sum': 1}}}
  ]
  results = mongo.db.collection_name.aggregate(pipeline)
  for result in results:
      print(result)
  ```

These methods cover most common CRUD operations and data manipulations you'll perform with MongoDB in your Flask application.
