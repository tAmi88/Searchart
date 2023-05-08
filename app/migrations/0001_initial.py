# Generated by Django 4.2.1 on 2023-05-08 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subsector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsector_name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_sectors', to='app.sector')),
            ],
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator_name', models.CharField(max_length=150)),
                ('content', models.CharField(blank=True, max_length=150, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('sub_sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indicators', to='app.subsector')),
            ],
        ),
    ]
