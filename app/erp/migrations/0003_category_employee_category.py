# Generated by Django 4.1 on 2022-09-24 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_type_employee_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'categoria',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='category',
            field=models.ManyToManyField(to='erp.category'),
        ),
    ]