# Generated by Django 2.0.4 on 2018-08-21 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20180820_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(verbose_name='pay rate per hour')),
                ('hours', models.IntegerField(verbose_name='hours')),
                ('post_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post.PostDetail')),
            ],
        ),
    ]
