# Generated by Django 4.1.1 on 2022-09-05 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0003_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile_pics/'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=120)),
                ('account', models.ManyToManyField(to='relations.account')),
            ],
        ),
    ]
