# Generated by Django 5.0.4 on 2024-04-15 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo da Tarefa')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('status', models.BooleanField(choices=[('O', 'Open'), ('C', 'Closed')], default='O', help_text='O para Open, C para Closed', verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
