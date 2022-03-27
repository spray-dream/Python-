# Generated by Django 3.2.12 on 2022-03-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20220311_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('level', models.SmallIntegerField(choices=[(1, '1级'), (2, '2级'), (3, '3级'), (4, '4级')], default=1, verbose_name='级别')),
                ('status', models.SmallIntegerField(choices=[(1, '已占用'), (2, '未使用')], default=2, verbose_name='状态')),
            ],
        ),
    ]
