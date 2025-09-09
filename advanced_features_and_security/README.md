# Permissions and Groups in Django

This app demonstrates how to use **Groups** and **Permissions** in Django.

## Custom Permissions

Defined in `Article` model:

- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

## Groups

- **Viewers** → can_view
- **Editors** → can_view, can_create, can_edit
- **Admins** → all permissions

## Setup

1. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
