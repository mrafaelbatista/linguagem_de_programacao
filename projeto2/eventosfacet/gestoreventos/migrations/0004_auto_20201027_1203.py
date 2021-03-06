# Generated by Django 3.1.2 on 2020-10-27 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestoreventos', '0003_funcionario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Palestrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_palestrante', models.CharField(max_length=150)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('email_palestrante', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='codigo_do_curso',
            new_name='codigo_curso',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='nome_do_curso',
            new_name='nome_curso',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='titulo',
            new_name='nome_evento',
        ),
        migrations.AddField(
            model_name='evento',
            name='curso_organizador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='gestoreventos.curso'),
        ),
        migrations.AddField(
            model_name='evento',
            name='data_final',
            field=models.DateTimeField(default='2020-01-01'),
        ),
        migrations.AddField(
            model_name='evento',
            name='data_inicio',
            field=models.DateTimeField(default='2020-01-01'),
        ),
        migrations.AddField(
            model_name='evento',
            name='organizador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='gestoreventos.funcionario'),
        ),
        migrations.AddField(
            model_name='evento',
            name='palestrantes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='gestoreventos.palestrante'),
        ),
    ]
