# Generated by Django 4.2.5 on 2023-09-12 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prodct', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=9)),
                ('location', models.CharField(max_length=50)),
                ('the_number', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prodct.product')),
            ],
            options={
                'db_table': 'client',
            },
        ),
    ]