# Generated by Django 3.2.4 on 2021-06-16 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20210616_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='post_tags', to='page.Tag'),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('tags', models.ManyToManyField(related_name='project_tags', to='page.Tag')),
            ],
        ),
    ]
