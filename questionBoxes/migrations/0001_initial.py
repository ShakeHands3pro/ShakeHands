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
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advice', models.TextField(verbose_name='回答')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='回答日')),
            ],
        ),
        migrations.CreateModel(
            name='QIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField(verbose_name='質問')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('status', models.CharField(choices=[('1', '回答待ち'), ('2', '回答済'), ('3', '非表示')], default=1, max_length=1, verbose_name='ステータス')),
                ('answerer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replyer', to=settings.AUTH_USER_MODEL)),
                ('index', models.ManyToManyField(to='questionBoxes.QIndex')),
                ('questionner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionBoxes.Answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='questionBoxes.Question'),
        ),
    ]
