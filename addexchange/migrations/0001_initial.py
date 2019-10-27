# Generated by Django 2.2.5 on 2019-10-27 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='addressExchange',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=400, verbose_name='交換申請目的')),
                ('approve_boolean', models.BooleanField(blank=True, null=True, verbose_name='承認')),
                ('request_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='申請日時')),
                ('accepted_time', models.DateTimeField(blank=True, null=True, verbose_name='承認日時')),
                ('answerer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answerer', to=settings.AUTH_USER_MODEL)),
                ('questioner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questioner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
