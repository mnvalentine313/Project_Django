# Generated by Django 2.2.7 on 2019-11-06 21:46

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('youtubify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]