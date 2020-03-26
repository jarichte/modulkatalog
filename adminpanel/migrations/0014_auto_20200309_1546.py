# Generated by Django 3.0.3 on 2020-03-09 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0013_auto_20200306_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='pruefungsmodalitaet',
            name='pm_anmeldung',
            field=models.TextField(blank=True, null=True, verbose_name='Informationen zur Anmeldung'),
        ),
        migrations.AlterField(
            model_name='veranstaltung',
            name='v_typ',
            field=models.CharField(blank=True, choices=[('Vorlesung', 'Vorlesung'), ('Übung', 'Übung'), ('Seminar', 'Seminar'), ('Arbeitsgruppe', 'Arbeitsgruppe')], db_column='V_Typ', max_length=20, null=True, verbose_name='Typ der Veranstaltung'),
        ),
    ]
