# Generated by Django 4.1.1 on 2022-09-28 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unity', '0002_alter_customeremail_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeremail',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]