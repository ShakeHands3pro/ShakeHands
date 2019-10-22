
# Generated by Django 2.2.5 on 2019-10-15 10:05

# # Generated by Django 2.2.5 on 2019-10-08 10:08
# >>>>>>> 83a2beec9e2f79b0e45cfb30f53c5934cbb130da

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='industry',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('industry_classification', models.CharField(max_length=50, verbose_name='業界分類')),
                ('industry', models.CharField(blank=True, max_length=50, verbose_name='業界')),
            ],
        ),
        migrations.CreateModel(
            name='occupation',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('occupation', models.CharField(max_length=50, verbose_name='職種')),
            ],
        ),
        migrations.CreateModel(
            name='openQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_text', models.TextField(verbose_name='Q')),
            ],
        ),
        migrations.CreateModel(
            name='prospectiveEmployer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50, verbose_name='社名')),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypage.industry', verbose_name='業界')),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypage.occupation', verbose_name='職種')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='openQ_ans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.TextField(max_length=1000, verbose_name='回答')),
                ('post_date', models.DateTimeField(auto_now=True, verbose_name='最終更新日')),
                ('openQ', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mypage.openQ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='myfriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='jobHunting_startTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=50, null=True, verbose_name='時期')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='jobHunting_requestment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace', models.CharField(blank=True, max_length=255, null=True, verbose_name='希望勤務地')),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypage.industry', verbose_name='希望業界')),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypage.occupation', verbose_name='希望職種')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='jobHunting_policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy', models.TextField(max_length=300, null=True, verbose_name='就活の軸')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='internshipRecommendation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50, verbose_name='社名')),
                ('season', models.CharField(max_length=50, verbose_name='時期')),
                ('period', models.CharField(max_length=50, verbose_name='期間')),
                ('overView', models.TextField(max_length=500, verbose_name='内容')),
                ('implessions', models.TextField(blank=True, max_length=300, null=True, verbose_name='感想')),
                ('post_date', models.DateTimeField(auto_now=True, verbose_name='最終更新日')),
                ('industry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mypage.industry', verbose_name='業界')),
                ('occupation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mypage.occupation', verbose_name='職種')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(blank=True, max_length=60, verbose_name='団体名')),
                ('post_date', models.DateTimeField(auto_now=True, verbose_name='最終更新日')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
