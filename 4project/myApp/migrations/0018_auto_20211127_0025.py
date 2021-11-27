# Generated by Django 2.2.24 on 2021-11-26 15:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0017_auto_20211127_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=4)),
                ('receiver', models.CharField(max_length=4)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myApp.login')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
