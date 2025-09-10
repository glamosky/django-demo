# LibraryBook CRUD (Django + DRF) Midterms

A minimal LibraryBook CRUD application built on top of the cloned class template project from Sir Benjz, with a REST API using Django REST Framework and optional HTML pages for demo.

## Requirements
- Python 3.10+
- Django (installed in your environment)
- Django REST Framework

If using pip:
```
pip install -r requirements.txt
```

## Setup
1. Activate your Python environment (virtualenv/micromamba/etc.)
2. Install dependencies (see above)
3. Apply migrations:
```
python manage.py migrate
```
4. Run the development server:
```
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

## Data Model: `LibraryBook`
- `title`: string
- `author`: string
- `isbn`: unique 13-digit string
- `is_checked_out`: boolean
- `due_date`: datetime, nullable when not checked out

Validation rules:
- `isbn` must be exactly 13 digits **STRICTLY NO DASHES**
- If `is_checked_out` is true, `due_date` is required; otherwise it must be null

## REST API Endpoints
Base: `http://127.0.0.1:8000/api/`

- List books: `GET /books/`
- Create book: `POST /books/`
  - JSON body: `{ "title": "...", "author": "...", "isbn": "9781234567890" }`
- Retrieve: `GET /books/{id}/`
- Update: `PUT /books/{id}/`
- Delete: `DELETE /books/{id}/`

Extra actions:
- Check out: `POST /books/{id}/checkout/` (sets `is_checked_out=true`, `due_date=now+14 days`)
- Return: `POST /books/{id}/return_book/` (sets `is_checked_out=false`, `due_date=null`)
- Available: `GET /books/available/`
- Checked out: `GET /books/checked_out/`

## Web Pages (optional but included)
- Home/List: `/`
- Detail: `/book/<id>/`
- Create: `/book/create/`
- Update: `/book/<id>/update/`
- Delete: `/book/<id>/delete/`

## Admin
You can optionally use the Django admin for managing data:
```
python manage.py createsuperuser
```
Then visit `/admin/`.

## Notes
- This project extends the provided classroom template; no fresh bootstrap required.
- Key files: `student/models.py`, `student/serializers.py`, `student/views.py`, `student/urls.py`, `core/urls.py`.

I had trouble dealing with dead links when opening localhost. I found a workaround:
1. Navigate to your project folder and make sure `manage.py` is there.
    ```
    cd C:\path\to\project-folder
    ```
    You should see like:
    ```
    manage.py
    core/
    student/
    ```
2. Activate your environment.
3. Run the Django Development Server.
    ```
    python manage.py runserver
    ```
    You should see something like:
    ```
    System check identified no issues (0 silenced).
    September 10, 2025 - 15:08:00
    Django version 5.2.5, using settings 'core.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```
4. Click the specified link.



