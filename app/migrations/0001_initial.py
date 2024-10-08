# Generated by Django 4.0.5 on 2022-06-21 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mess',
            fields=[
                ('mess_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('cutprice', models.IntegerField()),
                ('mapurl', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='images')),
                ('address', models.TextField(blank=True, null=True)),
                ('dish1', models.CharField(blank=True, max_length=100)),
                ('dish2', models.CharField(blank=True, max_length=100)),
                ('dish3', models.CharField(blank=True, max_length=100)),
                ('dish4', models.CharField(blank=True, max_length=100)),
                ('dish5', models.CharField(blank=True, max_length=100)),
                ('dish6', models.CharField(blank=True, max_length=100)),
                ('dish7', models.CharField(blank=True, max_length=100)),
                ('is_veg', models.BooleanField(default=True)),
                ('owner', models.CharField(blank=True, max_length=122)),
                ('contact_owener', models.CharField(blank=True, max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
