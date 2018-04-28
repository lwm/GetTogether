# Generated by Django 2.0 on 2018-04-21 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0026_add_user_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.CharField(default='-', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default='-', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.City', verbose_name='Home city'),
        ),
    ]
