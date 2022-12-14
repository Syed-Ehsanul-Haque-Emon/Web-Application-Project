# Generated by Django 3.1.14 on 2022-07-09 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_auto_20220709_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AlterField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=models.CharField(blank=True, max_length=750),
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
