# Generated by Django 4.2.3 on 2023-08-08 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clgapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clgapp.addcourse'),
        ),
    ]
