# Generated by Django 3.1.1 on 2021-01-29 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ktApp', '0004_phonehotel_phonehut_phoneinstructor_phoneponywalla_phoneskilender_phoneskishop'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='rating',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='hut',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='hut',
            name='rating',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.CreateModel(
            name='AccomodationHut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_rooms', models.IntegerField()),
                ('c_occupied', models.IntegerField()),
                ('fid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ktApp.hut')),
            ],
        ),
        migrations.CreateModel(
            name='AccomodationHotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_rooms', models.IntegerField()),
                ('c_occupied', models.IntegerField()),
                ('fid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ktApp.hotel')),
            ],
        ),
    ]
