# Generated by Django 5.0.1 on 2024-01-06 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('altura', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('tipo', models.ManyToManyField(related_name='pokemons', to='consultas_app.type')),
            ],
        ),
    ]
