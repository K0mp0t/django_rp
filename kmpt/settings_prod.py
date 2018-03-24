DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'django_recipes',
        'PASSWORD': 'peterpeter',
        'HOST': 'localhost',
        'PORT': '',
    }
}