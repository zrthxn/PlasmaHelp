# Generated by Django 3.0.5 on 2020-04-29 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_modify_hospital_contact_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donorprofile",
            name="date_last_tested_negative",
            field=models.DateField(
                blank=True,
                null=True,
                verbose_name="Date Last Tested Negative for COVID19 ",
            ),
        ),
    ]
