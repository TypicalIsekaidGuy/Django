# Generated by Django 4.1.4 on 2022-12-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_files_options_alter_files_file_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Messages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Тема письма")),
                ("message", models.TextField(verbose_name="Тема письма")),
                (
                    "file",
                    models.FileField(upload_to="send/%Y/%m/%d/", verbose_name="Файл"),
                ),
            ],
            options={
                "verbose_name": "сообщение",
                "verbose_name_plural": "сообщения",
                "ordering": ("title", "message"),
            },
        ),
        migrations.AlterField(
            model_name="files",
            name="file",
            field=models.FileField(upload_to="upload/%Y/%m/%d/", verbose_name="Файл"),
        ),
    ]