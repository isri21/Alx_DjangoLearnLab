import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_api.settings')
django.setup()

from posts.models import Post, Comment
from rest_framework.authtoken.models import Token

from datetime import datetime
from django.utils.timezone import now

Comment.objects.all().update(created_at=now())
Comment.objects.all().update(updated_at=now())