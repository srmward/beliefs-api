# Generated by Django 2.0.1 on 2018-01-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=500)),
                ('veracity', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'propositions',
                'ordering': ('id',),
            },
        ),
    ]
