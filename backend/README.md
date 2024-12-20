# Backend for django-flutter-example

## First time setup

1. Install Python 3.12+
2. Install [poetry](https://python-poetry.org/)
3. Install the dependencies:
   ```bash
   poetry install
   ```
4. Switch to the poetry environment:
   ```bash
   poetry shell
   ```
5. Create the database and fill it with demo data:
   ```bash
   sh scripts/reset_local_database.sh
   ```

## Session setup

1. Switch to the poetry environment:
   ```bash
   poetry shell
   ```
2. Run the server on port 8077:
   ```bash
   python manage.py runserver 8077
   ```

## Backend links

- [Admin site](http://localhost:8077/admin/); when asked to log in, use user
  `admin` with password `deMo.123` (as specified in `settings.py)`.
- [API overview](http://localhost:8077/)
- [Person overview (interactive)](http://localhost:8077/persons/) (Need to log
  in first using admin site)
- [Person overview (plain JSON)](http://localhost:8077/persons/?format=json)
  (Need to log in first using admin site)
