# Generated by Django 5.0.6 on 2024-08-18 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_bank_remove_transaction_game_delete_game_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='game_id',
            field=models.CharField(default=0, max_length=50, verbose_name='Game_ID'),
            preserve_default=False,
        ),
    ]
