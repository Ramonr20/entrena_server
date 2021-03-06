# Generated by Django 2.2.5 on 2020-03-09 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_nodo', models.CharField(max_length=100, verbose_name='Tipo de nodo')),
            ],
            options={
                'ordering': ['tipo_nodo'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_hab', models.CharField(max_length=100, unique=True, verbose_name='Nombre habitación')),
            ],
            options={
                'ordering': ['nombre_hab'],
            },
        ),
        migrations.CreateModel(
            name='Room_Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrena.Node')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrena.Room')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Reg_Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voltaje', models.FloatField(default=0.0, verbose_name='Voltaje')),
                ('corriente', models.FloatField(default=0.0, verbose_name='Corriente')),
                ('fac_de_pot', models.FloatField(default=0.0, verbose_name='factor de potencia')),
                ('pot_activa', models.FloatField(default=0.0, verbose_name='Potencia activa')),
                ('pot_real', models.FloatField(default=0.0, verbose_name='Potencia real')),
                ('pot_aparente', models.FloatField(default=0.0, verbose_name='Potencia aparente')),
                ('flag', models.BooleanField(default=True, verbose_name='Estado')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('room_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrena.Room_Node')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='node',
            name='rooms',
            field=models.ManyToManyField(through='entrena.Room_Node', to='entrena.Room'),
        ),
    ]
