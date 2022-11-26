# Generated by Django 4.1.3 on 2022-11-26 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0003_alter_auto_categoria_alter_auto_disponibilidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compradores',
            name='compradorApellidoMat',
            field=models.CharField(max_length=50, verbose_name='Comprador Apellido Materno'),
        ),
        migrations.AlterField(
            model_name='compradores',
            name='compradorApellidoPat',
            field=models.CharField(max_length=50, verbose_name='Comprador Apellido Paterno'),
        ),
        migrations.AlterField(
            model_name='compradores',
            name='compradorTelefono',
            field=models.IntegerField(verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='vendedores',
            name='vendedorApellidoMat',
            field=models.CharField(max_length=50, verbose_name='Comprador Vendedor Materno'),
        ),
        migrations.AlterField(
            model_name='vendedores',
            name='vendedorApellidoPat',
            field=models.CharField(max_length=50, verbose_name='Comprador Vendedor Paterno'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='compradorrut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto.compradores', verbose_name='Rut Comprador'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='id_detalle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto.detalles', verbose_name='ID Detalle'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='idauto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto.auto', verbose_name='ID Auto'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='vendedorrut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto.vendedores', verbose_name='Rut Vendedor'),
        ),
    ]
