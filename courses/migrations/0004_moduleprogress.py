# Generated by Django 5.1.4 on 2025-01-15 08:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_modulecontent_file'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.PositiveIntegerField(default=0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progresses', to='courses.module')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module_progresses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Module Progress',
                'verbose_name_plural': 'Module Progresses',
                'unique_together': {('user', 'module')},
            },
        ),
    ]
