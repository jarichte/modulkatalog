# Generated by Django 3.0.3 on 2020-02-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0003_auto_20200226_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fakultaet',
            options={'managed': True, 'verbose_name_plural': 'Fakultäten'},
        ),
        migrations.AlterModelOptions(
            name='studiengang',
            options={'managed': True, 'verbose_name_plural': 'Studiengänge'},
        ),
        migrations.AlterField(
            model_name='fakultaet',
            name='fk_name',
            field=models.CharField(db_column='FK_Name', max_length=255, primary_key=True, serialize=False, verbose_name='Name der Fakultät'),
        ),
        migrations.AlterField(
            model_name='modul',
            name='md_gruppengroesse',
            field=models.IntegerField(blank=True, db_column='MD_Gruppengroesse', null=True, verbose_name='Gruppengröße'),
        ),
        migrations.AlterField(
            model_name='modul',
            name='md_kuerzel',
            field=models.CharField(db_column='MD_Kuerzel', max_length=20, primary_key=True, serialize=False, verbose_name='Modulkürzel'),
        ),
        migrations.AlterField(
            model_name='modul',
            name='md_lehrender',
            field=models.ManyToManyField(blank=True, db_table='lehrender', related_name='lehrender', to='adminpanel.Person'),
        ),
        migrations.AlterField(
            model_name='modul',
            name='md_modulverantwortlich',
            field=models.ManyToManyField(blank=True, db_table='modulverantwortlicher', related_name='modulverantwortlicher', to='adminpanel.Person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_namenskuerzel',
            field=models.CharField(db_column='P_Namenskuerzel', max_length=8, primary_key=True, serialize=False, verbose_name='Namenskürzel'),
        ),
    ]