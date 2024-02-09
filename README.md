# Web Services
## FastAPI MongoDB CRUD Project

This project aims to create a simple CRUD (Create, Read, Update, Delete) API using FastAPI and MongoDB.

Install project:
```
git clone https://github.com/Burcu8/Web-Services.git
```
```
cd Web-Services
```

**Loading the Requirements:**
```bash
    pip install -r requirements.txt
```

**Setting Environment Variables:**

`.env` file and define the following environment variables:
  ```env
  mongo_client='mongodb://localhost:27017/',
  db_name='film_db_test',
  collection_name='films'
  ```

Run the application:

```
uvicorn main:app --reload
```

Technologies:
* Python 3.8+
* FastAPI
* MongoDB

### API Endpoints
* `GET '/content/'` : Lists all items.
* `GET '/content/{content_id}'` : Displays a specific item.
* `POST '/content/'` : Adds a new item.
* `PUT '/content/{content_id}'` : Updates a specific item.
* `DELETE '/content/{content_id}'` : Deletes a specific item.


### Data Model: 

The project uses the following data model:

```json
{
  "title": "string",
  "year": "string",
  "description": "string",
  "producer": "string",
  "description": "string",
  "genre": "string"
}
