# Generated by Django 2.0.5 on 2018-05-27 08:49

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
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_code', models.IntegerField()),
                ('type', models.IntegerField()),
                ('status', models.IntegerField()),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('transaction_time', models.DateTimeField()),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_code', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('desc', models.CharField(max_length=512)),
            ],
        ),
    ]