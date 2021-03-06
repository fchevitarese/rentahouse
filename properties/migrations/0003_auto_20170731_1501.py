# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20170729_0213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Propriedades', 'verbose_name_plural': 'Propriedades'},
        ),
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='property',
            name='complement',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='property',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='property',
            name='neighborhood',
            field=models.CharField(max_length=50, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='property',
            name='state',
            field=models.CharField(choices=[('MG', 'Minas Gerais'), ('SP', 'São Paulo'), ('RJ', 'Rio de Janeiro')], max_length=2, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='property',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Rua'),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Breve descrição'),
        ),
        migrations.AlterField(
            model_name='property',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='property',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor do aluguel'),
        ),
        migrations.AlterField(
            model_name='propertypics',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='media/properties', verbose_name='Foto'),
        ),
    ]
