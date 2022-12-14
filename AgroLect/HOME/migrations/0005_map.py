# Generated by Django 4.0.3 on 2022-08-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0004_delete_locations'),
    ]

    operations = [
        migrations.CreateModel(
            name='MAP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RegionName', models.CharField(choices=[('NA', 'North America'), ('AS', 'Asia')], max_length=200)),
                ('country', models.CharField(choices=[('CA', 'Canada'), ('MX', 'Mexico'), ('US', 'United States'), ('RU', 'Russia'), ('IND', 'India'), ('CH', 'China')], max_length=20)),
                ('cities', models.CharField(choices=[('ON', 'Ontario'), ('AB', 'Alberta'), ('TO', 'Toronto'), ('QB', 'Quebec'), ('SN', 'Sinaloa'), ('BC', 'Baja California'), ('OZ', 'Orizabo'), ('CH', 'Chihuahua'), ('OA', 'Oaxaca'), ('AK', 'Arkansas'), ('WN', 'Washington'), ('GRG', 'Georgia'), ('TXS', 'Texas'), ('IW', 'Iowa'), ('KR', 'Krasnodar'), ('RT', 'Rostov'), ('ST', 'Stavropol'), ('SB', 'Siberia'), ('FZ', 'Faizabad'), ('AM', 'Amritsar'), ('KTK', 'Kolkata'), ('AMD', 'Ahmedabad'), ('CHW', 'Chhindwara'), ('GZ', 'Guizhou'), ('GDG', 'Guangdong'), ('XNG', 'Xinjiang'), ('UQI', 'Urumqi')], max_length=20)),
            ],
        ),
    ]
