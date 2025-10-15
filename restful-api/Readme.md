# RESTful API Project

## Introduction

In the evolving world of software development, **efficient communication and data transfer** across systems is critical. This project introduces RESTful APIs — a core tech powering modern web services. REST (Representational State Transfer) defines a scalable, stateless, cacheable architecture, enabling seamless and broad integration for internet applications.

---

## Learning Objectives

- **HTTP/HTTPS Basics**: Understand foundational web protocols, data transfer, security, and method differences.
- **API Consumption with Command Line**: Use command-line tools (e.g., `curl`) to consume APIs.
- **API Consumption with Python**: Fetch and process API data programmatically with Python.
- **API Development with `http.server`**: Build a basic API using Python’s built-in modules.
- **API Development with Flask**: Develop advanced APIs with routing, data management, and scalability using Flask.
- **API Security & Authentication**: Learn how to secure APIs and implement authentication.
- **API Standards & Documentation with OpenAPI**: Understand best practices for maintainable and clear API documentation.

---

## Importance

RESTful APIs are essential for system integration, acting as translators between applications. They facilitate activities including social media data sharing, industrial automation, and more. Developing, consuming, securing, and documenting APIs gives software engineers both deep technical insight and high-level design understanding for smooth digital communication.

---

## REST API Conceptual Diagram
```
+-------+ +-------+ +---------+ +---------+
| | Request | | Process | | Fetch/ | |
| | -----> | | -------> | | Modify | |
| | | | | | -------> | |
| | <----- | | <------- | | | |
| | Response | | Return | | | |
+-------+ +-------+ +---------+ +---------+
Client Web Server API Server Database

```
### Components

- **Client**: Requests the service (browser or app).
- **Web Server**: Receives requests and passes them to the API server.
- **API Server**: Processes requests, executes logic, and determines necessary actions.
- **Database**: Stores data that the API fetches or modifies.

### Typical Request/Response Flow

1. Client sends HTTP/HTTPS request to Web Server.
2. Web Server forwards the request to API Server.
3. API Server processes, interacts with Database.
4. API Server sends response back to Web Server.
5. Web Server returns final HTTP/HTTPS response to the Client.

---

## Tasks Overview

### 0. HTTP/HTTPS Basics

- **Goal**: Differentiate HTTP and HTTPS, understand requests/responses, common methods/status codes.
- **Key Concepts**:
  - HTTP is plain, unsecured; HTTPS uses SSL/TLS for encryption.
  - Structure includes `method`, `path`, `status code`, and `headers`.
- **Common Methods**:
  - `GET`: Retrieve data
  - `POST`: Submit new data
  - `PUT`: Update existing data
  - `DELETE`: Remove data
- **Status Codes**:
  - `200`: Success (OK)
  - `201`: Created
  - `400`: Bad Request
  - `404`: Not Found
  - `500`: Server Error

---

### 1. API Consumption with cURL

- **Install and verify**: `curl --version`
- **GET request**: `curl http://example.com`
- **API consumption**: `curl https://jsonplaceholder.typicode.com/posts`
- **Headers only**: `curl -I https://jsonplaceholder.typicode.com/posts`
- **POST data**: `curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts`
- **Hints**: Use `-I` for headers, `-X` to specify method, `-d` to send data, pipe to `jq` for formatted output.

---

### 2. API Consumption & Processing with Python

- **Use the `requests` library** to GET data, process JSON, and write output to CSV.
- **Functions**:
  - `fetch_and_print_posts()`: Prints status code and post titles.
  - `fetch_and_save_posts()`: Saves post data (`id`, `title`, `body`) to `posts.csv`.

---

### 3. API with Python `http.server`

- **Create server** using `http.server.BaseHTTPRequestHandler`.
- **Endpoints**:
  - `/` : Returns “Hello, this is a simple API!”
  - `/data`: Returns JSON `{"name": "John", "age": 30, "city": "New York"}`
  - `/status`: Returns `OK`
  - Other: 404 Not Found with message.
- **Structure**: Use `send_response`, `send_header`, `end_headers` for response management.

---

### 4. Simple API with Flask

- **Setup**: Install and initiate Flask app.
- **Endpoints**:
  - `/`: "Welcome to the Flask API!"
  - `/data`: Returns list of usernames
  - `/status`: Returns "OK"
  - `/users/<username>`: Returns user's details or 404 if not found
  - `/add_user`: Accepts POST, adds new user, returns 201 confirmation or error:
    - 400: Username missing or invalid JSON
    - 409: Username exists

---

### 5. API Security & Authentication

- **Basic Auth**: Uses hashed passwords (`werkzeug.security`). Protected routes with `@auth.login_required`.
- **JWT Authentication**:
  - `/login`: POST, returns JWT token on success.
  - `/jwt-protected`: GET, requires token.
  - `/admin-only`: GET, accessible to users with `admin` role only.
- **Custom Error Handlers**: Use Flask-JWT-Extended to ensure all auth errors return `401 Unauthorized`.
  - Includes missing, invalid, expired, revoked, or non-fresh tokens.

---

## File Structure

```
restful-api/
├── main.py
├── posts.csv
├── task_02_requests.py
├── task_03_http_server.py
├── task_04_flask.py
├── task_05_basic_security.py
```

---

## References

- [Mozilla Developer Network: HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [curl: Everything curl](https://curl.se)
- [Python Requests Library](https://requests.readthedocs.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/)
- [OpenAPI Specification](https://swagger.io/specification/)

---

## License

This project is for educational purposes as part of Holberton School's **Higher Level Programming** curriculum.
