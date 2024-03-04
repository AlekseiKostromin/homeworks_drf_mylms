# Generated by Django 4.2.10 on 2024-03-04 04:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='course_previews/', verbose_name='превью')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('price', models.IntegerField(default=0, verbose_name='стоимость курса')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='последнее обновление')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='lesson_previews/', verbose_name='превью')),
                ('video_link', models.URLField(blank=True, null=True, verbose_name='ссылка на видео')),
                ('price', models.IntegerField(default=0, verbose_name='стоимость урока')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='последнее обновление')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]
