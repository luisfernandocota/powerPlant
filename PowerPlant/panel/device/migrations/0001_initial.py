# Generated by Django 2.2.4 on 2022-03-24 01:23

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatusDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'Status devices',
                'db_table': 'status_devices',
            },
        ),
        migrations.CreateModel(
            name='TypeDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameType', models.CharField(max_length=50, verbose_name='Name device')),
            ],
            options={
                'verbose_name': 'Type device',
                'db_table': 'type_devices',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nameDevice', models.CharField(max_length=50, verbose_name='Name device')),
                ('currentPower', models.SmallIntegerField(verbose_name='Current power')),
                ('statusDevice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_statusDevice', to='device.StatusDevice')),
                ('typeDevice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_typeDevice', to='device.TypeDevice')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
                'db_table': 'devices',
            },
        ),
    ]