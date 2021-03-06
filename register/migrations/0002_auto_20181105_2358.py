# Generated by Django 2.1.3 on 2018-11-05 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='telefone_cliente',
            fields=[
                ('telefone', models.CharField(max_length=12, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Telefones Clientes',
            },
        ),
        migrations.RenameModel(
            old_name='usuario',
            new_name='cliente',
        ),
        migrations.AddField(
            model_name='telefone_cliente',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.cliente'),
        ),
    ]
