# Generated by Django 3.0.3 on 2020-03-04 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0009_auto_20200302_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modul',
            name='md_angebotsturnus',
            field=models.CharField(blank=True, choices=[('FSS', 'FSS'), ('HWS', 'HWS')], db_column='MD_Angebotsturnus', max_length=64, null=True, verbose_name='Angebotsturnus'),
        ),
        migrations.AlterField(
            model_name='modul',
            name='md_inhalte',
            field=models.TextField(blank=True, db_column='MD_Inhalte', null=True, verbose_name='Inhalte'),
        ),
        migrations.AlterField(
            model_name='modul',
            name='md_kompetenzziele',
            field=models.TextField(blank=True, db_column='MD_Kompetenzziele', null=True, verbose_name='Kompetenzziele'),
        ),
        migrations.AlterField(
            model_name='modul',
            name='md_lernformen',
            field=models.TextField(blank=True, db_column='MD_Lernformen', null=True, verbose_name='Lernformen'),
        ),
        migrations.AlterField(
            model_name='modul',
            name='md_sprache',
            field=models.CharField(blank=True, choices=[('Deutsch', 'Deutsch'), ('Englisch', 'english')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='modul',
            name='md_weitere_informationen',
            field=models.TextField(blank=True, db_column='MD_Weitere_Informationen', null=True, verbose_name='Weitere Informationen'),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_adresse_email',
            field=models.EmailField(blank=True, db_column='P_Adresse_Email', max_length=127, null=True, verbose_name='E-Mail Adresse'),
        ),
    ]
