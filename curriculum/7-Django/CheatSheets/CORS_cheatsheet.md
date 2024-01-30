# Django CORS Cheat Sheet

## Installation

To use Django CORS, you need to install the `django-cors-headers` package. You can install it using `pip`:

```bash
pip install django-cors-headers
```

## Configuration

After installing the package, you need to configure it in your Django project settings.

1. Add `'corsheaders'` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    # other apps...
    'corsheaders',
]
```

2. Add `'corsheaders.middleware.CorsMiddleware'` to the `MIDDLEWARE` list:

```python
MIDDLEWARE = [
    # other middleware...
    'corsheaders.middleware.CorsMiddleware',
    # other middleware...
]
```

## Settings

You can customize the CORS behavior in your Django settings by using the following options:

### `CORS_ORIGIN_ALLOW_ALL`

Set this option to `True` if you want to allow all origins (domains) to access your API.

```python
CORS_ORIGIN_ALLOW_ALL = True
```

### `CORS_ALLOW_CREDENTIALS`

Set this option to `True` to allow cookies to be included in cross-origin requests.

```python
CORS_ALLOW_CREDENTIALS = True
```

### `CORS_ALLOWED_ORIGINS`

If `CORS_ORIGIN_ALLOW_ALL` is `False`, you can specify a list of allowed origins (domains) using this option.

```python
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://subdomain.example.com",
]
```

### `CORS_ALLOWED_METHODS`

Specify the HTTP methods (verbs) that are allowed for cross-origin requests.

```python
CORS_ALLOWED_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
```

### `CORS_ALLOWED_HEADERS`

Specify the HTTP headers that are allowed for cross-origin requests.

```python
CORS_ALLOWED_HEADERS = [
    'Accept',
    'Content-Type',
    'Authorization',
]
```

### `CORS_EXPOSE_HEADERS`

Specify the HTTP headers that browsers are allowed to access.

```python
CORS_EXPOSE_HEADERS = [
    'Content-Disposition',
]
```

### `CORS_PREFLIGHT_MAX_AGE`

Specify the maximum time (in seconds) that a preflight request can be cached.

```python
CORS_PREFLIGHT_MAX_AGE = 86400
```

### `CORS_URLS_REGEX`

Set this option if you want to apply CORS headers to specific URL patterns.

```python
CORS_URLS_REGEX = r'^/api/.*$'
```
