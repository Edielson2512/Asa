# Generated by Django 3.1.6 on 2023-05-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0018_auto_20230523_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('O', 'Outro'), ('M', 'Masculino'), ('F', 'Feminino'), ('I', 'Infantil'), ('A', 'Acessórios')], default='O', max_length=1),
        ),
    ]