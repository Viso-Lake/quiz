# Generated by Django 5.0.4 on 2024-04-24 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_admin_options_alter_answer_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Обратная связь', 'verbose_name_plural': 'Обратная связь'},
        ),
    ]
