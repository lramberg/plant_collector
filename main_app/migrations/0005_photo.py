# Generated by Django 2.2 on 2019-06-13 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20190612_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Plant')),
            ],
        ),
    ]
