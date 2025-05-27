EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'yourgmail@gmail.com'         # Your Gmail address
EMAIL_HOST_PASSWORD = 'your-app-password'       # App password, not your Gmail password!
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER