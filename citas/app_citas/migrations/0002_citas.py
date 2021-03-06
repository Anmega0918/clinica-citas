# Generated by Django 3.2.9 on 2021-11-18 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_citas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField(verbose_name=15)),
                ('tipocita', models.CharField(choices=[('URGENCIAS', 'URGENCIAS'), ('CONTROL', 'CONTROL'), ('PRIORITARIA', 'PRIORITARIA'), ('ODONTOLOGICA', 'ODONTOLOGICA'), ('ESPECIALISTA', 'ESPECIALISTA')], default='available', max_length=50)),
                ('fecha', models.DateField()),
                ('horariocita', models.CharField(choices=[('Mañana1', '7AM'), ('Mañana2', '8AM'), ('Mañana3', '9AM'), ('Mañana4', '10AM'), ('Mañana5', '11AM'), ('Tarde1', '1PM'), ('Tarde2', '2PM'), ('Tarde3', '3PM'), ('Tarde4', '4PM'), ('Tarde5', '5PM')], default='available', max_length=50)),
                ('IDpaciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_citas.paciente')),
            ],
        ),
    ]
