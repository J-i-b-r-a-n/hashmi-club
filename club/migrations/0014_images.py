# Generated by Django 3.2.5 on 2021-09-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0013_alter_matches_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frstimg', models.ImageField(upload_to='club/images/')),
                ('scndimg', models.ImageField(upload_to='club/images')),
            ],
        ),
    ]
