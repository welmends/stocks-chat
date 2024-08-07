# Generated by Django 3.2.7 on 2021-09-12 13:44

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import migrations, transaction


def insert_default_users(apps, schema_editor):
    User = apps.get_model("auth", "User")
    try:
        with transaction.atomic():
            user = User.objects.create(
                username="admin", password=make_password("admin"), is_superuser=True
            )
            user.save()
        with transaction.atomic():
            user = User.objects.create(
                username="stocks-bot", password=make_password("bot-passwd")
            )
            user.save()
        with transaction.atomic():
            user = User.objects.create(username="user", password=make_password("123"))
            user.save()
    except Exception:
        pass


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("dashboard", "0002_message"),
    ]

    operations = [
        migrations.RunPython(insert_default_users),
    ]
