# Generated by Django 4.1.5 on 2023-01-19 20:25

import datetime
import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Definition",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(default=datetime.datetime.now)),
                ("updated_at", models.DateTimeField(default=datetime.datetime.now)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("term", models.CharField(max_length=128)),
                ("definition", models.TextField()),
                ("temp", models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                "db_table": "definition",
            },
        ),
        migrations.AddIndex(
            model_name="definition",
            index=models.Index(fields=["term"], name="definition_term_bbbf2a_idx"),
        ),
    ]
