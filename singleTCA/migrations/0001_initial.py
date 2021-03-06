# Generated by Django 2.2 on 2018-06-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Columns', models.TextField(blank=True, null=True)),
                ('Data', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=12)),
                ('acc_no', models.CharField(max_length=10)),
                ('portfolio', models.CharField(blank=True, default='All', max_length=10)),
                ('ins', models.CharField(blank=True, default='All', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='T_PS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Columns', models.TextField(blank=True, null=True)),
                ('Data', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='V_REV_SP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Columns', models.TextField(blank=True, null=True)),
                ('Data', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
