from django.contrib import admin
from .models import *
# Register your models here.

class VeranstaltungAdmin(admin.ModelAdmin):
    fieldsets =[
        ('Allgemeine Informationen',    {'fields': ['v_titel', 'v_typ',]}),
        ('Prüfungsmodalität hinzufügen',    {'fields': ['pm_nr']}),
        ('Arbeitsaufwand',  {'fields': ['v_sws', 'v_aufwand_praesenz','v_aufwand_pruefungsvorbereitung', 'v_aufwand_selbststudium']}),
        ('Sonstige Informationen', {'fields': ['v_ects', 'v_semester']})
    ]
    def get_fieldsets(self, request, obj=None):
        if request.user.groups.filter(name='Recht').exists():
            return[
                (None, {'fields': ['v_titel',]}),
                ('Prüfungsmodalität hinzufügen', {'fields': ['pm_nr']}),
                (None, {'fields': ['v_sws']}),
            ]
        elif request.user.groups.filter(name='Vwl').exists():
            return[
                ('Allgemeine Informationen', {'fields': ['v_typ', ]}),
                ('Prüfungsmodalität hinzufügen', {'fields': ['pm_nr']}),
                ('Arbeitsaufwand', {'fields': ['v_sws', 'v_aufwand_praesenz', 'v_aufwand_pruefungsvorbereitung']})
            ]
        elif request.user.groups.filter(name='Bwl').exists():
            return[
                ('Allgemeine Informationen', {'fields': ['v_typ', ]}),
                ('Prüfungsmodalität hinzufügen', {'fields': ['pm_nr']}),
                ('Arbeitsaufwand', {'fields': ['v_aufwand_praesenz', 'v_aufwand_selbststudium']}),
            ]
        elif request.user.groups.filter(name='Wifo_Wima').exists():
            return[
                ('Allgemeine Informationen', {'fields': ['v_titel',]}),
                ('Prüfungsmodalität hinzufügen', {'fields': ['pm_nr']}),
                ('Arbeitsaufwand', {'fields': ['v_sws', 'v_aufwand_praesenz', 'v_aufwand_pruefungsvorbereitung', 'v_aufwand_selbststudium']}),
            ]
        elif request.user.groups.filter(name='Philo').exists():
            return[
                ('Allgemeine Informationen', {'fields': ['v_titel']}),
                ('Prüfungsmodalität hinzufügen', {'fields': ['pm_nr']}),
                ('Arbeitsaufwand', {'fields': ['v_sws', 'v_aufwand_praesenz', 'v_aufwand_pruefungsvorbereitung',
                                               'v_aufwand_selbststudium']}),
                ('Sonstige Informationen', {'fields': ['v_ects', 'v_semester']})
            ]
        elif request.user.groups.filter(name='Sowi').exists():
            return[
                ('Allgemeine Informationen', {'fields': ['v_titel', 'v_typ', ]}),
                ('Prüfungsmodalität hinzufügen', {'fields': ['pm_nr']}),
                ('Sonstige Informationen', {'fields': ['v_ects', 'v_semester']})
            ]
        else:
            return super(VeranstaltungAdmin, self).get_fieldsets(request, obj)
    list_display = ('v_titel', 'v_typ', 'md_kuerzel')
    search_fields = ('v_titel', 'v_typ', 'md_kuerzel__md_kuerzel')


class VeranstaltungStacked(admin.StackedInline):
    model=Veranstaltung
    extra = 1
    fieldsets = [
    (None, {'fields': ['v_titel', 'v_typ', ]}),
    (None, {'fields': ['pm_nr']}),
    (None, {'fields': ['v_sws', 'v_aufwand_praesenz', 'v_aufwand_pruefungsvorbereitung', 'v_aufwand_selbststudium']}),
    (None, {'fields': ['v_ects', 'v_semester']})
    ]

    def get_fieldsets(self, request, obj=None):
        if request.user.groups.filter(name='Recht').exists():
            return[
                (None, {'fields': ['v_titel']}),
                (None, {'fields': ['pm_nr']}),
                (None, {'fields': ['v_sws']}),
            ]
        elif request.user.groups.filter(name='Vwl').exists():
            return[
                (None, {'fields': ['v_typ', ]}),
                (None, {'fields': ['pm_nr']}),
                (None, {'fields': ['v_sws', 'v_aufwand_praesenz', 'v_aufwand_pruefungsvorbereitung']})
            ]
        elif request.user.groups.filter(name='Bwl').exists():
            return[
                (None, {'fields': ['v_typ', ]}),
                (None, {'fields': ['pm_nr']}),
                (None, {'fields': ['v_aufwand_praesenz', 'v_aufwand_selbststudium']}),
            ]
        elif request.user.groups.filter(name='Wifo_Wima').exists():
            return[
                (None, {'fields': ['v_titel',]}),
                (None, {'fields': ['pm_nr']}),
                (None, {'fields': ['v_sws', 'v_aufwand_praesenz', 'v_aufwand_pruefungsvorbereitung', 'v_aufwand_selbststudium']}),
            ]
        elif request.user.groups.filter(name='Philo').exists():
            return[
                (None, {'fields': ['v_titel']}),
                (None, {'fields': ['pm_nr']}),
                (None, {'fields': ['v_sws', 'v_aufwand_praesenz', 'v_aufwand_pruefungsvorbereitung',
                                               'v_aufwand_selbststudium']}),
                (None, {'fields': ['v_ects', 'v_semester']})
            ]
        elif request.user.groups.filter(name='Sowi').exists():
            return[
                (None, {'fields': ['v_titel', 'v_typ', ]}),
                (None, {'fields': ['pm_nr']}),
                (None, {'fields': ['v_ects', 'v_semester']})
            ]
        else:
            return super(VeranstaltungStacked, self).get_fieldsets(request, obj)

class BesitztStacked(admin.StackedInline):
    model = Besitzt
    extra = 1

class ZusatzattributeStacked(admin.StackedInline):
    model = Zusatzattribute
    extra = 1

class ModulAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Darstellungsform des Moduls | Name der Abteilung',   {'fields': ['md_darstellung']}),
        ('Allgemeine Informationen',  {'fields': ['md_kuerzel', 'md_name', 'md_ects', 'md_sprache', 'md_modulverantwortlich', 'md_angebotsturnus']}),
        ('Inhalt und Beschreibung', {'fields': ['md_inhalte', 'md_kompetenzziele', 'md_medienform', 'md_lernformen']}),
        ('Weitere Informationen', {'fields' : ['md_abschlussziel', 'md_dauer', 'md_gruppengroesse', 'md_kontakzeit', 'md_selbststudium', 'md_studienjahr', 'md_sws', 'md_lehrender', 'md_voraussetzen', 'md_weitere_informationen']})
    ]
    list_display = ('md_kuerzel', 'md_name')
    search_fields = ['md_kuerzel', 'md_name']
    inlines = [VeranstaltungStacked, BesitztStacked, ZusatzattributeStacked]

    def get_fieldsets(self, request, obj=None):
        if request.user.groups.filter(name='Recht').exists():
            return [('Darstellungsform des Moduls | Name der Abteilung',   {'fields': ['md_darstellung']}),
                    ('Allgemeine Informationen',  {'fields': ['md_kuerzel', 'md_name', 'md_ects', 'md_sprache', 'md_angebotsturnus']}),
                    ('Inhalt und Beschreibung', {'fields': ['md_kompetenzziele', 'md_lernformen']}),
                    ('Weitere Informationen', {'fields' : ['md_dauer', 'md_studienjahr', 'md_sws', 'md_voraussetzen', 'md_weitere_informationen']})

                    ]
        elif request.user.groups.filter(name='Vwl').exists():
            return [
                ('Darstellungsform des Moduls | Name der Abteilung', {'fields': ['md_darstellung']}),
                ('Allgemeine Informationen', { 'fields': ['md_kuerzel', 'md_name', 'md_ects', 'md_sprache', 'md_modulverantwortlich', 'md_angebotsturnus']}),
                ('Inhalt und Beschreibung', {'fields': ['md_inhalte', 'md_kompetenzziele',]}),
                ('Weitere Informationen', {'fields': ['md_dauer', 'md_gruppengroesse', 'md_voraussetzen', 'md_weitere_informationen']})

            ]
        elif request.user.groups.filter(name="Bwl").exists():
            return [
                ('Darstellungsform des Moduls | Name der Abteilung', {'fields': ['md_darstellung']}),
                ('Allgemeine Informationen', {'fields': ['md_kuerzel', 'md_name', 'md_ects', 'md_sprache', 'md_modulverantwortlich', 'md_angebotsturnus']}),
                ('Inhalt und Beschreibung', {'fields': ['md_inhalte', 'md_kompetenzziele']}),
                ('Weitere Informationen', {'fields': ['md_abschlussziel', 'md_dauer', 'md_voraussetzen', 'md_weitere_informationen']})

            ]
        elif request.user.groups.filter(name="Philo").exists():
            return [
                ('Darstellungsform des Moduls | Name der Abteilung', {'fields': ['md_darstellung']}),
                ('Allgemeine Informationen', {'fields': ['md_kuerzel', 'md_name', 'md_ects', 'md_sprache', 'md_modulverantwortlich',]}),
                ('Inhalt und Beschreibung',{'fields': ['md_inhalte', 'md_kompetenzziele', 'md_lernformen']}),
                ('Weitere Informationen', {'fields': ['md_abschlussziel', 'md_sws', 'md_voraussetzen','md_weitere_informationen']})

            ]

        elif request.user.groups.filter(name="Sowi").exists():
            return[
                ('Darstellungsform des Moduls | Name der Abteilung', {'fields': ['md_darstellung']}),
                ('Allgemeine Informationen', {'fields': ['md_kuerzel', 'md_name', 'md_modulverantwortlich','md_angebotsturnus']}),
                ('Inhalt und Beschreibung', {'fields': ['md_inhalte', 'md_kompetenzziele']}),
                ('Weitere Informationen', {'fields': ['md_dauer', 'md_gruppengroesse', 'md_kontakzeit', 'md_selbststudium','md_voraussetzen',]})
            ]

        elif request.user.groups.filter(name="Wifo_Wima").exists():
            return[
                ('Darstellungsform des Moduls | Name der Abteilung', {'fields': ['md_darstellung']}),
                ('Allgemeine Informationen', {'fields': ['md_kuerzel', 'md_name', 'md_ects', 'md_sprache', 'md_modulverantwortlich', 'md_angebotsturnus']}),
                ('Inhalt und Beschreibung', {'fields': ['md_inhalte', 'md_kompetenzziele', 'md_medienform', 'md_lernformen']}),
                ('Weitere Informationen', {'fields': ['md_abschlussziel', 'md_dauer', 'md_studienjahr', 'md_sws', 'md_lehrender', 'md_voraussetzen', 'md_weitere_informationen']})
            ]
        else:
            return super(ModulAdmin, self).get_fieldsets(request, obj)

class PruefungsmodalitaetAdmin(admin.ModelAdmin):
    list_display = ('pm_nr', 'pm_form', 'pm_benotung', 'dauer')
    search_fields = ('pm_nr', 'pm_form','dauer')

    def get_fields(self, request, obj=None):
        if request.user.groups.filter(name='Recht').exists():
            return ('pm_form', )
        elif request.user.groups.filter(name='Vwl').exists():
            return ('pm_form', )
        elif request.user.groups.filter(name='Bwl').exists():
            return ('pm_form','pm_benotung', 'pm_vorraussetzung', 'dauer')
        elif request.user.groups.filter(name='Sowi').exists():
            return ('pm_form', 'pm_benotung', 'pm_vorraussetzung', 'dauer')
        elif request.user.groups.filter(name='Wifo_Wima').exists():
            return ('pm_form', 'pm_vorraussetzung', 'dauer')
        elif request.user.groups.filter(name='Philo').exists():
            return ('pm_form', 'pm_benotung', 'pm_vorraussetzung')
        else:
            return ('pm_form', 'pm_benotung', 'pm_vorraussetzung', 'dauer', 'pm_anmeldung')

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name und Namenskuerzel', {'fields':   ['p_namenskuerzel', 'p_name', 'p_vorname', 'p_titel']}),
        ('Adresse', {'fields':  ['p_adresse_email', 'p_adresse_buero', 'p_telefon']})
    ]
    list_display = ('p_name', 'p_vorname', 'p_namenskuerzel',)
    search_fields = ('p_name', 'p_vorname', 'p_namenskuerzel')

class ModulkatalogAdmin(admin.ModelAdmin):
    list_display = ('mk_von_studiengang', 'mk_abschluss', 'mk_jahr', 'mk_gueltig_von', 'mk_gueltig_bis')
    search_fields = ('mk_von_studiengang__sg_name', 'mk_jahr')

    def get_queryset(self, request):
        qs = super(ModulkatalogAdmin, self).get_queryset(request)
        if request.user.groups.filter(name='Wifo_Wima').exists():
            return qs.filter(mk_von_studiengang__gehoert_zu__fk_name = 'Fakultaet fuer Wirtschaftsinformatik und Wirtschaftsmathematik')
        elif request.user.groups.filter(name='Vwl').exists():
            return qs.filter(mk_von_studiengang__gehoert_zu__fk_name = 'Fakultaet fuer Rechtswissenschaften und Volkswirtschaftslehre')
        if request.user.groups.filter(name='Recht').exists():
            return qs.filter(mk_von_studiengang__gehoert_zu__fk_name = 'Fakultaet fuer Rechtswissenschaften und Volkswirtschaftslehre')
        if request.user.groups.filter(name='Bwl').exists():
            return qs.filter(mk_von_studiengang__gehoert_zu__fk_name = 'Fakultaet fuer Betriebswirtschaftslehre')
        if request.user.groups.filter(name='Sowi').exists():
            return qs.filter(mk_von_studiengang__gehoert_zu__fk_name = 'Fakultaet fuer Sozialwissenschaften')
        if request.user.groups.filter(name='Philo').exists():
            return qs.filter(mk_von_studiengang__gehoert_zu__fk_name = 'Philosophische Fakultaet')
        else:
            return qs

class BesitztAdmin(admin.ModelAdmin):
    list_display = ('modul', 'modulkatalog', 'typ',)
    search_fields = ('modul__md_kuerzel', 'modulkatalog__mk_von_studiengang__sg_name', 'typ',)

    def get_queryset(self, request):
        qs = super(BesitztAdmin, self).get_queryset(request)
        if request.user.groups.filter(name='Wifo_Wima').exists():
            return qs.filter(modulkatalog__mk_von_studiengang__gehoert_zu__fk_name='Fakultaet fuer Wirtschaftsinformatik und Wirtschaftsmathematik')
        elif request.user.groups.filter(name='Vwl').exists():
            return qs.filter(modulkatalog__mk_von_studiengang__gehoert_zu__fk_name='Fakultaet fuer Rechtswissenschaften und Volkswirtschaftslehre')
        elif request.user.groups.filter(name='Recht').exists():
            return qs.filter(modulkatalog__mk_von_studiengang__gehoert_zu__fk_name='Fakultaet fuer Rechtswissenschaften und Volkswirtschaftslehre')
        elif request.user.groups.filter(name='Bwl').exists():
            return qs.filter(modulkatalog__mk_von_studiengang__gehoert_zu__fk_name='Fakultaet fuer Betriebswirtschaftslehre')
        elif request.user.groups.filter(name='Philo').exists():
            return qs.filter(modulkatalog__mk_von_studiengang__gehoert_zu__fk_name='Philosophische Fakultaet')
        elif request.user.groups.filter(name='Sowi').exists():
            return qs.filter(modulkatalog__mk_von_studiengang__gehoert_zu__fk_name='Fakultaet fuer Sozialwissenschaften')
        else:
            return qs

admin.site.register(Fakultaet)
admin.site.register(Studiengang)
admin.site.register(Modulkatalog, ModulkatalogAdmin)
admin.site.register(Modul, ModulAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Zusatzattribute)
admin.site.register(Veranstaltung, VeranstaltungAdmin)
admin.site.register(Pruefungsmodalitaet, PruefungsmodalitaetAdmin)
admin.site.register(Besitzt, BesitztAdmin)
