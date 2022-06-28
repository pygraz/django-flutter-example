import datetime

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=100, verbose_name="first name")),
                ("last_name", models.CharField(max_length=100, verbose_name="last name")),
                (
                    "gender",
                    models.IntegerField(
                        choices=[(0, "not known"), (1, "male"), (2, "female"), (9, "not applicable")],
                        default=0,
                        verbose_name="gender",
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(datetime.date(1900, 1, 1))],
                        verbose_name="date of birth",
                    ),
                ),
            ],
            options={
                "verbose_name": "person",
                "verbose_name_plural": "persons",
                "ordering": ("last_name", "first_name", "date_of_birth", "id"),
            },
        ),
    ]
