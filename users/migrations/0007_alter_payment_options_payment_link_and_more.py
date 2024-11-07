# Generated by Django 4.2.2 on 2024-11-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_subscription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'оплата', 'verbose_name_plural': 'оплаты'},
        ),
        migrations.AddField(
            model_name='payment',
            name='link',
            field=models.URLField(blank=True, max_length=400, null=True, verbose_name='ссылка на оплату'),
        ),
        migrations.AddField(
            model_name='payment',
            name='session_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='id сессии'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_amount',
            field=models.PositiveIntegerField(verbose_name='сумма оплаты'),
        ),
    ]