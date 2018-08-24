# Generated by Django 2.1 on 2018-08-22 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20180822_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='player_game',
        ),
        migrations.RemoveField(
            model_name='player',
            name='player_user',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='game_instructor',
            new_name='instructor',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='game_scenario',
            new_name='scenario',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]
