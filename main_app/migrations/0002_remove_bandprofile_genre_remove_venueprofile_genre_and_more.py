# Generated by Django 4.1.7 on 2023-03-11 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bandprofile',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='venueprofile',
            name='genre',
        ),
        migrations.AddField(
            model_name='fanprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bandprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.IntegerField(choices=[(0, 'Admin'), (1, 'Fan'), (2, 'Band'), (3, 'Venue')], default=1, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='venueprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=20)),
                ('bands', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bandprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=20)),
                ('bands', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bandprofile')),
            ],
        ),
    ]