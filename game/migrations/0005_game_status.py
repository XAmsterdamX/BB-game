# Generated by Django 2.1 on 2018-08-23 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_remove_game_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.IntegerField(choices=[(0, 'Created'), (1, 'Round 1'), (2, 'Round 2'), (3, 'Round 3'), (4, 'Round 4'), (5, 'Round 5'), (6, 'Round 6'), (7, 'Round 7'), (8, 'Round 8'), (9, 'Completed')], default=0),
        ),
    ]
