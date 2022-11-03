# Generated by Django 4.1 on 2022-11-03 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatbox', '0007_alter_inputmodel_text_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputmodel',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]