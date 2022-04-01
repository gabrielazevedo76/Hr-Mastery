# Generated by Django 4.0.3 on 2022-03-31 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms', models.BooleanField(default=False, verbose_name='took responsability')),
                ('message', models.TextField()),
                ('person', models.CharField(choices=[('Candidate', 'Candidate'), ('Employee', 'Employee')], max_length=50)),
                ('option', models.CharField(choices=[('Others', 'Others'), ('My password does not work', 'My password does not work'), ('I lost my account', 'I lost my account'), ('Update resume', 'Update resume')], max_length=50)),
                ('email', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('situation', models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done')], default='Pending', max_length=50, null=True)),
            ],
        ),
    ]