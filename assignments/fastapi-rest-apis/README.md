# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement RESTful API endpoints using FastAPI, including routing, request validation, and JSON responses.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description
Build a FastAPI application with routes to fetch and return data from a simple in-memory store.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Add a `GET /items` endpoint that returns a list of items.
- Add a `GET /items/{item_id}` endpoint that returns a single item by ID.
- Return JSON responses with the correct item data.

### 🛠️ Accept and Validate Request Data

#### Description
Add a route that accepts POST requests and validates incoming request bodies before storing new data.

#### Requirements
Completed program should:

- Define a Pydantic model for item input.
- Add a `POST /items` endpoint that accepts JSON request bodies.
- Validate request data automatically using FastAPI.
- Append new items to the in-memory store and return the created item.

### 🛠️ Handle Errors and Responses

#### Description
Implement error handling and clear response behavior for invalid requests.

#### Requirements
Completed program should:

- Return a `404` error if the requested item ID does not exist.
- Return meaningful error messages in JSON format.
- Use FastAPI's `HTTPException` for error responses.
- Include example usage for each endpoint in the assignment.
