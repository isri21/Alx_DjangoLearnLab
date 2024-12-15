import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_api.settings')
django.setup()

from accounts.models import User
from rest_framework.authtoken.models import Token

user = User.objects.get(username="Abebti")
token = Token.objects.get(user=user)

print(type(token.key))