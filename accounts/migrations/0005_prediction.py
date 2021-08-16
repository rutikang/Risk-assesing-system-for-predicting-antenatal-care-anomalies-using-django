# Generated by Django 3.1.7 on 2021-04-29 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210420_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancies', models.IntegerField(null=True)),
                ('Uterine_size', models.IntegerField(null=True)),
                ('blood_pressure', models.IntegerField(null=True)),
                ('abortion', models.IntegerField(null=True)),
                ('drugs', models.IntegerField(null=True)),
                ('BMI', models.FloatField(null=True)),
                ('diabetes', models.FloatField(null=True)),
            ],
        ),
    ]