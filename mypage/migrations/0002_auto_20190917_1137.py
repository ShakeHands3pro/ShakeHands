# Generated by Django 2.2.5 on 2019-09-17 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='implessions',
            new_name='club_name',
        ),
    ]
