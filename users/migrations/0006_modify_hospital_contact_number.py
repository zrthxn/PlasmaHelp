# Generated by Django 3.0.5 on 2020-04-29 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_modify_name_from_user_to_donor"),
    ]

    operations = [
        migrations.RemoveField(model_name="hospitalprofile", name="mobile_number",),
    ]
