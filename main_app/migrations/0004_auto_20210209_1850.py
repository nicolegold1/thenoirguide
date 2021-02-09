# Generated by Django 3.1.6 on 2021-02-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='category',
        ),
        migrations.RemoveField(
            model_name='business',
            name='country',
        ),
        migrations.RemoveField(
            model_name='business',
            name='user',
        ),
        migrations.AddField(
            model_name='business',
            name='business_type',
            field=models.CharField(choices=[('REST', 'Restaurant'), ('HAIR', 'Hair Salon'), ('BARB', 'Barber Shop'), ('ESTH', 'Esthetician'), ('NAIL', 'Nail Salon'), ('DERM', 'Dermatologist'), ('APPL', 'Appliance Repair'), ('LAWY', 'Lawyer'), ('EVEN', 'Event Planner'), ('REAL', 'REALTOR'), ('SKIN', 'Skincare'), ('CLOT', 'Clothing')], default='REST', max_length=4),
        ),
        migrations.AddField(
            model_name='business',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
