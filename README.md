# URL Shortening Service (Django REST Framework)

A simple RESTful API built with **Django REST Framework** for shortening long URLs.  
It allows you to create unique short codes for URLs, retrieve original URLs, update and delete shortened links, and track access statistics.

https://roadmap.sh/projects/url-shortening-service

---

## 🚀 Features
- **Create** short codes for long URLs  
- **Retrieve** the original URL from a short code  
- **Update** an existing short URL  
- **Delete** a short URL  
- **Track** and retrieve access count for each short URL  


---
## 📌 API Endpoints

| Method | Endpoint                  | Description |
|--------|---------------------------|-------------|
| POST   | `/`                        | Create a new short URL |
| GET    | `/`                        | List all short URLs |
| GET    | `/<id>/`                   | Retrieve a short URL by ID |
| PUT    | `/<id>/`                   | Update a short URL by ID |
| PATCH  | `/<id>/`                   | Partially update a short URL by ID |
| DELETE | `/<id>/`                   | Delete a short URL by ID |
| GET    | `/retrieve/<short_code>`   | Retrieve the original URL without incrementing access count |
| GET    | `/detail/<short_code>`     | Retrieve the original URL and increment access count |
| DELETE | `/delete/<short_code>`     | Delete a short URL by short code |
