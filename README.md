# A Boilerplate Example for a Dockerized Django/ReactJS web application with Postgres database

## This is an example project using the following technologies:
* Docker with Docker Compose
* Django REST APIs
* ReactJS
* Webpack module bundler and Hot Reloading (Hot Reloader 3)

# Setup Local Environment

1. Create .env file
 
###### Here's a Sample
```
 SECRET_KEY='#_r+1boq=zxhknws&0-8l)fi77tp#%if+ii%$ek6h86_iv3q%&'
 DEBUG=true
 DJANGO_SETTINGS_MODULE=django_config.settings.local
 ALLOWED_HOSTS= 127.0.0.1 0.0.0.0
 DATABASE_URL=postgres://django:1234@postgres:5432/boilerplate
 DJANGO_ADMIN_URL=^admin/
 
 MAILGUN_API_KEY=[mailgun-api-key]
 MAILGUN_DEFAULT_FROM_EMAIL=[email]
 
 
 POSTGRES_PASSWORD=1234
 POSTGRES_USER=django
 POSTGRES_DB=boilerplate
 
 EMAIL_PORT=1025
 EMAIL_HOST=localhost
 EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
 DEFAULT_FROM_EMAIL=admin@gmail.com
```

2. npm install
3. make docker-build-dev
4. make docker-up-dev

#### Visit http://localhost:8000
 
## Babel
Javascript has versions named ECMAScript (ES). Allows us to have a clean, maintainable code using the latest JS specifications without needing to worry about browser support.

## Webpack

## Why Django + React

1. Turn your site into a single page web app. Faster.
2. Use the same codebase for iOS and Android (with React Native)
3. Manage complicated state more easily
4. React is Backend Agnostic

Boilerplate adapted from:

https://gist.github.com/genomics-geek/98929a9e7ba9602fed7bfa4a5a1c5c4e#file-step08-md




