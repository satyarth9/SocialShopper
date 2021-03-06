# Generated by Django 3.1.4 on 2021-06-30 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopping_status', models.CharField(choices=[('PR', 'Proposed'), ('AC', 'Active'), ('CO', 'Completed')], default='PR', max_length=2)),
                ('total_amount', models.FloatField()),
                ('venue', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('shopper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.appuser')),
            ],
        ),
    ]
