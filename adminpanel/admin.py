from django.contrib import admin
from .models import *
# Register your models here.
class ModulAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Darstellungsform des Moduls | Name der Abteilung',   {'fields': ['md_darstellung']}),
        ('Allgemeine Informationen',  {'fields': ['md_kuerzel', 'md_name', 'md_ects', 'md_sprache', 'md_modulverantwortlich', 'md_angebotsturnus']}),
        ('Inhalt und Beschreibung', {'fields': ['md_inhalte', 'md_kompetenzziele', 'md_medienform', 'md_lernformen']}),
        ('Weitere Informationen', {'fields' : ['md_abschlussziel', 'md_dauer', 'md_gruppengroesse', 'md_kontakzeit', 'md_selbststudium', 'md_studienjahr', 'md_sws', 'md_lehrender', 'md_voraussetzen', 'md_weitere_informationen']})
    ]
    list_display = ('md_kuerzel', 'md_name')
    search_fields = ['md_kuerzel', 'md_name']

class VeranstaltungAdmin(admin.ModelAdmin):
    fieldsets =[
        ('Allgemeine Informationen',    {'fields': ['v_titel', 'v_typ',]}),
        ('Modul hinzufügen',    {'fields': ['md_kuerzel',]}),
        ('Prüfungsmodalität hinzufügen',    {'fields': ['pm_nr']}),
        ('Arbeitsaufwand',  {'fields': ['v_sws', 'v_aufwand_praesenz','v_aufwand_pruefungsvorbereitung', 'v_aufwand_selbststudium']}),
        ('Sonstige Informationen', {'fields': ['v_ects', 'v_semester']})
    ]
    list_display = ('v_titel', 'v_typ', 'md_kuerzel')
    search_fields = ('v_titel', 'v_typ','md_kuerzel__md_kuerzel')

class PruefungsmodalitaetAdmin(admin.ModelAdmin):
    list_display = ('pm_nr', 'pm_form', 'pm_benotung', 'dauer')
    search_fields = ('pm_nr', 'pm_form','dauer')

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name und Namenskuerzel', {'fields':   ['p_namenskuerzel', 'p_vorname', 'p_name', 'p_titel']}),
        ('Adresse', {'fields':  ['p_adresse_email', 'p_adresse_buero', 'p_telefon']})
    ]
    list_display = ('p_name', 'p_vorname', 'p_namenskuerzel',)
    search_fields = ('p_name', 'p_vorname', 'p_namenskuerzel')

class ModulkatalogAdmin(admin.ModelAdmin):
    list_display = ('mk_von_studiengang', 'mk_abschluss', 'mk_jahr', 'mk_gueltig_von', 'mk_gueltig_bis')
    search_fields = ('mk_von_studiengang__sg_name', 'mk_jahr')

class BesitztAdmin(admin.ModelAdmin):
    list_display = ('modul', 'modulkatalog', 'typ',)
    search_fields = ('modul__md_kuerzel', 'modulkatalog__mk_von_studiengang__sg_name', 'typ',)

admin.site.register(Fakultaet)
admin.site.register(Studiengang)
admin.site.register(Modulkatalog, ModulkatalogAdmin)
admin.site.register(Modul, ModulAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Zusatzattribute)
admin.site.register(Veranstaltung, VeranstaltungAdmin)
admin.site.register(Pruefungsmodalitaet, PruefungsmodalitaetAdmin)
admin.site.register(Besitzt, BesitztAdmin)

