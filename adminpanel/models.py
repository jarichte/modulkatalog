# -*- coding: utf-8 -*-
from django.db import models
from .choiceboxsettings import *


class Person(models.Model):
    p_namenskuerzel = models.CharField("Namenskürzel", db_column='P_Namenskuerzel', primary_key=True, max_length=8)
    p_vorname = models.CharField("Vorname", db_column='P_Vorname', max_length=127, blank=True, null=True)
    p_name = models.CharField("Nachname", db_column='P_Name', max_length=127, blank=True, null=True)
    p_telefon = models.IntegerField("Telefonnummer", db_column='P_Telefon', blank=True, null=True)
    p_adresse_email = models.EmailField("E-Mail Adresse", db_column='P_Adresse_Email', max_length=127, blank=True, null=True)
    p_adresse_buero = models.CharField("Buero Adresse", db_column='P_Adresse_Buero', max_length=127, blank=True, null=True)
    p_titel = models.CharField("Namenszusatz", db_column='P_Titel', max_length=30, blank=True, null=True)

    class Meta:
        verbose_name_plural='Personen'
        managed = True
        db_table = 'person'
    def __str__(self):
        return str(self.p_namenskuerzel)

class Fakultaet(models.Model):
    fk_name = models.CharField("Name der Fakultät", db_column='FK_Name', primary_key=True, max_length=255)

    class Meta:
        verbose_name_plural ='Fakultäten'
        managed = True
        db_table = 'fakultaet'
    def __str__(self):
        return self.fk_name

class Studiengang(models.Model):
    sg_name = models.CharField("Studiengangsname", db_column='SG_Name', primary_key=True, max_length=255)
    gehoert_zu = models.ForeignKey(Fakultaet, models.DO_NOTHING, db_column='gehoert_zu')

    class Meta:
        verbose_name_plural ='Studiengänge'
        managed = True
        db_table = 'studiengang'
    def __str__(self):
        return self.sg_name

class Modul(models.Model):
    md_kuerzel = models.CharField("Modulkürzel", db_column='MD_Kuerzel', primary_key=True, max_length=20, help_text=helper_modul['md_kuerzel'])
    md_abschlussziel = models.CharField("Abschlussziel", db_column='MD_Abschlussziel', max_length=64, blank=True, null=True, help_text=helper_modul['md_abschlussziel'])
    md_name = models.CharField("Name des Moduls", db_column='MD_Name', max_length=127, blank=True, null=True, help_text=helper_modul['md_name'])
    md_angebotsturnus = models.CharField("Angebotsturnus", db_column='MD_Angebotsturnus', max_length=64,choices=ANGEBOTSTURNUS, blank=True, null=True, help_text=helper_modul['md_angebotsturnus'])
    md_dauer = models.FloatField("Dauer", db_column='MD_Dauer', blank=True, null=True, help_text=helper_modul['md_dauer'])
    md_ects = models.IntegerField("ECTS", db_column='MD_ECTS', blank=True, null=True, help_text=helper_modul['md_ects'])
    md_gruppengroesse = models.IntegerField("Gruppengröße", db_column='MD_Gruppengroesse', blank=True, null=True, help_text=helper_modul['md_gruppengroesse'])
    md_inhalte = models.TextField("Inhalte", db_column='MD_Inhalte', blank=True, null=True, help_text=helper_modul['md_inhalte'])
    md_kompetenzziele = models.TextField("Kompetenzziele", db_column='MD_Kompetenzziele', blank=True, null=True, help_text=helper_modul['md_kompetenzziele'])
    md_kontakzeit = models.IntegerField("Kontaktzeit", db_column='MD_Kontakzeit', blank=True, null=True,help_text=helper_modul['md_kontaktzeit'])
    md_lernformen = models.TextField("Lernformen", db_column='MD_Lernformen', blank=True, null=True, help_text=helper_modul['md_lernformen'])
    md_medienform = models.CharField("Medienform", db_column='MD_Medienform', max_length=256, blank=True, null=True, help_text=helper_modul['md_medienform'])
    md_selbststudium = models.IntegerField("Selbststudium", db_column='MD_Selbststudium', blank=True, null=True, help_text=helper_modul['md_selbststudium'])
    md_sprache = models.CharField("Sprache", max_length=30, choices=SPRACHE, blank=True, null=True, help_text=helper_modul['md_sprache'])
    md_studienjahr = models.IntegerField("Studienjahr", db_column='MD_Studienjahr', blank=True, null=True, help_text=helper_modul['md_studienjahr'])
    md_sws = models.IntegerField("Semesterwochenstunden",db_column='MD_SWS', blank=True, null=True, help_text=helper_modul['md_sws'])
    md_weitere_informationen = models.TextField("Weitere Informationen", db_column='MD_Weitere_Informationen', blank=True, null=True, help_text=helper_modul['md_weitere_informationen'])
    md_modulverantwortlich = models.ManyToManyField(Person, db_table="modulverantwortlicher", related_name="modulverantwortlicher", blank=True,help_text=helper_modul['md_modulverantwortlich'])
    md_lehrender = models.ManyToManyField(Person, db_table="lehrender", related_name="lehrender", blank=True, help_text=helper_modul['md_lehrender'])
    md_voraussetzen = models.ManyToManyField('self', related_name='nachfolger', symmetrical=False, blank=True, help_text=helper_modul['md_voraussetzen'])
    md_darstellung = models.CharField('Darstellungsform des Moduls', choices=DARSTELLUNG, max_length=30, null=True, blank=True,)

    class Meta:
        verbose_name_plural ='Module'
        managed = True
        db_table = 'modul'

    def __str__(self):
        return self.md_kuerzel

    def calcSWS(self):
        sws=0
        for veranstaltung in self.veranstaltung_set.all():
            try:
                sws += veranstaltung.v_sws
            except TypeError:
                sws += 0
        return sws

    def calcECTS(self):
        ects=0
        for veranstaltung in self.veranstaltung_set.all():
            try:
                ects += veranstaltung.v_ects
            except TypeError:
                ects +=0
        return ects

    def calcAufwand(self):
        aufwand= 0
        for veranstaltung in self.veranstaltung_set.all():
            try:
                aufwand += veranstaltung.v_aufwand_praesenz
            except TypeError:
                aufwand+= 0
            try:
                aufwand += veranstaltung.v_aufwand_selbststudium
            except TypeError:
                aufwand += 0
            try:
                aufwand += veranstaltung.v_aufwand_pruefungsvorbereitung
            except TypeError:
                aufwand +=0
        return aufwand

    # only for the philosophy modulcatalogue for template processing purpose
    def getRowSpan(self):
        return self.veranstaltung_set.all().count() * 8 + 1

    def getBesitzt(self):
        return Besitzt.objects.filter(modul=self)

class Modulkatalog(models.Model):
    mk_von_studiengang = models.ForeignKey('Studiengang', models.DO_NOTHING, db_column='MK_von_Studiengang')
    mk_abschluss = models.CharField("Studienabschluss", max_length=40, choices=ABSCHLUSS, null=True)
    mk_jahr = models.IntegerField("Jahr",choices=JAHR, db_column='MK_Jahr', blank=True, null=True)
    mk_vorwort = models.TextField("Vorwort", db_column='MK_Vorwort', max_length=2048, blank=True, null=True)
    mk_nachwort = models.TextField("Nachwort", db_column='MK_Nachwort', max_length=2048, blank=True, null=True)
    mk_gueltig_von = models.DateField("Gültig von", db_column='MK_Gueltig_von', blank=True, null=True)
    mk_gueltig_bis = models.DateField("Gültig bis", db_column='MK_Gueltig_bis', blank=True, null=True)
    mk_module = models.ManyToManyField(Modul, through='besitzt', blank=True)

    class Meta:
        verbose_name_plural ='Modulkataloge'
        managed = True
        db_table = 'modulkatalog'
    def __str__(self):
        return str(self.mk_von_studiengang) + ' (' + str(self.mk_jahr) + ')'


class Zusatzattribute(models.Model):
    zt_name = models.CharField('Attributname', db_column='ZT_Name', primary_key=True, max_length=30)
    zt_wert = models.CharField('Attributwert', db_column='ZT_Wert', max_length=256, blank=True, null=True)
    md_kuerzel = models.ForeignKey(Modul, on_delete=models.SET_NULL, db_column='MD_Kuerzel', blank=True, null=True)

    class Meta:
        verbose_name_plural ='Zusatzattribute'
        managed = True
        db_table = 'zusatzattribute'
    def __str__(self):
        return self.zt_name


class Pruefungsmodalitaet(models.Model):
    pm_nr = models.AutoField("Prüfungsnummer", db_column='PM_Nr', primary_key=True)
    pm_form = models.CharField("Prüfungsform", db_column='PM_Form', max_length=40, blank=True, null=True, help_text=helper_pruefung['pm_form'])
    pm_benotung = models.CharField("Benotung", db_column='PM_Benotung', max_length=30, blank=True, null=True, help_text=helper_pruefung['pm_benotung'])
    pm_vorraussetzung = models.TextField("Prüfungsvorraussetzungen", db_column='PM_Vorraussetzung', blank=True, null=True, help_text=helper_pruefung['pm_vorraussetzung'])
    dauer = models.IntegerField("Prüfungsdauer",choices=DAUER, db_column='Dauer', blank=True, null=True, help_text=helper_pruefung['dauer'])
    pm_anmeldung = models.TextField("Informationen zur Anmeldung", blank=True, null=True, help_text=helper_pruefung['pm_anmeldung'])

    class Meta:
        verbose_name_plural ='Prüfungsmodalitaeten'
        managed = True
        db_table = 'pruefungsmodalitaet'
    def __str__(self):
        return str(self.pm_nr)


class Veranstaltung(models.Model):
    v_nr = models.AutoField(db_column='V_Nr', primary_key=True,)
    pm_nr = models.ForeignKey(Pruefungsmodalitaet, on_delete=models.SET_NULL, db_column='PM_Nr', blank=True, null=True, help_text=helper_veranstaltung['pm_nr'])
    v_titel = models.CharField("Titel der Veranstaltung", db_column='V_Titel', max_length=200, blank=True, null=True, help_text=helper_veranstaltung['v_titel'])
    v_typ = models.CharField("Typ der Veranstaltung", db_column='V_Typ', max_length=20, blank=True, null=True, choices=VERANSTALTUNGEN, help_text=helper_veranstaltung['v_typ'])
    md_kuerzel = models.ForeignKey(Modul, models.DO_NOTHING, db_column='MD_Kuerzel', blank=True, null=True, help_text=helper_veranstaltung['md_kuerzel'])
    v_sws = models.IntegerField("Semesterwochenstunden", db_column='V_SWS', blank=True, null=True, help_text=helper_veranstaltung['v_sws'])
    v_aufwand_praesenz = models.IntegerField("Aufwand für Präsenz", db_column='V_Aufwand_Praesenz', blank=True, null=True, help_text=helper_veranstaltung['v_aufwand_praesenz'])
    v_aufwand_pruefungsvorbereitung = models.IntegerField("Aufwand für Prüfungsvorbereitung", db_column='V_Aufwand_Pruefungsvorbereitung', blank=True, null=True, help_text=helper_veranstaltung['v_aufwand_pruefungsvorbereitung'])
    v_aufwand_selbststudium = models.IntegerField("Aufwand fuer Selbststudium", db_column='V_Aufwand_Selbststudium', blank=True, null=True, help_text=helper_veranstaltung['v_aufwand_selbststudium'])
    v_ects = models.IntegerField("ECTS", db_column='V_ECTS', blank=True, null=True, help_text=helper_veranstaltung['v_ects'])
    v_semester = models.IntegerField("Semesterangebot", db_column='V_Semester', blank=True, null=True, help_text=helper_veranstaltung['v_semester'])

    class Meta:
        verbose_name_plural ='Veranstaltungen'
        managed = True
        db_table = 'veranstaltung'
    def __str__(self):
        return str(self.v_titel) + " " + str(self.v_typ)

    def getPruefung(self):
        if(self.pm_nr):
            return Pruefungsmodalitaet.objects.get(pk=int(self.pm_nr.pm_nr))
        else:
            return None


class Besitzt(models.Model):
    modul = models.ForeignKey(Modul, on_delete=models.CASCADE, blank=True)
    modulkatalog = models.ForeignKey(Modulkatalog, on_delete=models.CASCADE, blank=True)
    typ = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural ='Zuordnung von Modulen zu den Modulkatalogen'
        managed = True
        db_table = 'besitzt'
    def __str__(self):
        return str(self.modul) + " " + str(self.modulkatalog) + " " + str(self.typ)