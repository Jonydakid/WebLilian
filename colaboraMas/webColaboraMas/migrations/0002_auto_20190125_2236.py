# Generated by Django 2.1.5 on 2019-01-26 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webColaboraMas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('objetivo', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='curso',
            name='objetivo',
        ),
        migrations.AlterField(
            model_name='curso',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webColaboraMas.Categoria'),
        ),
    ]