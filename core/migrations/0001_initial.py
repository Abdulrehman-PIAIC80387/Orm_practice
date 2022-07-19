# Generated by Django 3.2.13 on 2022-07-19 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BONUS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bonus_date', models.DateField(null=True)),
                ('Bonus_id', models.IntegerField(blank=True, default=0, null=True, verbose_name='Bonus_id ')),
                ('bonus_amount', models.IntegerField(blank=True, default=0, null=True, verbose_name='bonus_amount ')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_id', models.IntegerField(blank=True, default=0, null=True, verbose_name='worker_id')),
                ('worker_title', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='person_name')),
                ('affected_from', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WORKER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname_name', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='person_name')),
                ('last_name', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='person_name')),
                ('department', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='address')),
                ('worker_id', models.IntegerField(blank=True, default=0, null=True, verbose_name='worker_id')),
                ('salary', models.IntegerField(blank=True, default=0, null=True, verbose_name='Salary')),
                ('joining_date', models.DateField(null=True)),
            ],
        ),
    ]
