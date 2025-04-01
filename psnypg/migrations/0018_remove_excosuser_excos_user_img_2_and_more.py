# Generated by Django 5.1.6 on 2025-03-31 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psnypg', '0017_excosuser_excos_user_img_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='excosuser',
            name='excos_user_img_2',
        ),
        migrations.RemoveField(
            model_name='excosuser',
            name='excos_user_img_3',
        ),
        migrations.AddField(
            model_name='psnypgnewsandevent',
            name='psnypg_news_and_event_img_2',
            field=models.ImageField(default=1, upload_to=' news_images_2/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='psnypgnewsandevent',
            name='psnypg_news_and_event_img_3',
            field=models.ImageField(default=1, upload_to=' news_images_3/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='psnypgnewsandevent',
            name='psnypg_news_and_event_img',
            field=models.ImageField(upload_to=' news_images/'),
        ),
    ]
