#This part provides the lists for the choice boxes in the models.py

ABSCHLUSS= [('B.Sc.', 'Bachelor of Science'),
           ('M.Sc.', 'Master of Science'),
           ('B.Edu.', 'Bachelor of Education'),
           ('M.Edu.', 'Master of Education'),
           ('B.A.', 'Bachelor of Arts'),
           ('M.A.', 'Master of Arts'),
           ('LL.B', 'Bachelor of Laws'),
           ('LL.M', 'Master of Laws')
           ]

SPRACHE= [('Deutsch', 'Deutsch'),
         ('Englisch', 'english')
         ]

JAHR= [(2013,2013),
       (2014,2014),
       (2015,2015),
       (2016,2016),
       (2017,2017),
       (2018,2018),
       (2019,2019),
       (2020,2020),
       (2021,2021),
       (2022,2022),
       (2023,2023),
       (2024,2024),
       (2025,2025),
       (2026,2026)
       ]

DAUER= [(30,"30 Minuten"),
        (45,"45 Minuten"),
        (60,"60 Minuten"),
        (90,"90 Minuten"),
        (120,"120 Minuten"),
        (135,'135 Minuten'),
        (180,"180 Minuten"),
        (240, "240 Minuten")
        ]

ANGEBOTSTURNUS= [('FSS', 'FSS'),
                 ('HWS', 'HWS'),
                  ('HWSSWS', 'HWS und SWS'),
                 ('unregelmäßig', 'unregelmäßig')
                 ]
VERANSTALTUNGEN= [('Vorlesung', 'Vorlesung'),
                  ('Übung', 'Übung'),
                  ('Tutorium', 'Tutorium'),
                  ('Seminar', 'Seminar'),
                  ('Arbeitsgruppe', 'Arbeitsgruppe')
                  ]
DARSTELLUNG= [('recht', 'Recht'),
              ('vwl', 'Volkswirtschaftslehre'),
              ('bwl', 'Betriebswirtschaftslehre'),
              ('sowi','Sozialwissenschaften'),
              ('wifo', 'Wirtschaftsinformatik und -mathematik'),
              ('philo', 'Philosophie')
              ]

# This part provides the helper text in the Model class
wifo= '<div style="color:blue; display:inline;">Wirtschaftsinformatik und Wirtschaftsmathematik </div>|'
bwl= '<div style="color:IndianRed; display:inline;">Betriebswirtschaftslehre </div>|'
vwl= '<div style="color:Purple; display:inline;;"> Volkswirtschaftslehre </div>|'
recht= '<div style="color:pink; display:inline;">Rechtswissenschaften </div>|'
sowi= '<div style="color:green; display:inline;">Sozialwissenschaften </div>|'
philo= '<div style="color:orange; display:inline;"> Philosophie </div>'

helper_modul = {
    'md_kuerzel': wifo + bwl + vwl + recht + sowi + philo,
    'md_name': wifo + bwl + vwl + recht + sowi + philo,
    'md_kompetenzziele': wifo + bwl + vwl + recht + sowi + philo,
    'md_ects': wifo + bwl + vwl + recht + philo,
    'md_sprache': wifo + bwl + vwl + recht + philo,
    'md_modulverantwortlich': wifo + bwl + vwl + sowi + philo,
    'md_angebotsturnus': wifo + bwl + vwl + recht + sowi,
    'md_inhalte': wifo + bwl + vwl + sowi + philo,
    'md_medienform': wifo,
    'md_lernformen': wifo + recht + philo,
    'md_abschlussziel': wifo + bwl + philo,
    'md_dauer': wifo + bwl + vwl + recht + sowi,
    'md_gruppengroesse': vwl + sowi,
    'md_kontaktzeit': sowi,
    'md_selbststudium': sowi,
    'md_studienjahr': wifo + recht,
    'md_sws': recht + philo,
    'md_lehrender': wifo,
    'md_voraussetzen': wifo + bwl + vwl + recht + sowi + philo,
    'md_weitere_informationen': wifo + bwl + vwl + recht + philo,
}

helper_veranstaltung = {
    'pm_nr': wifo + bwl + vwl + recht + sowi + philo,
    'v_titel': wifo + recht + sowi + philo,
    'v_typ': bwl + vwl + sowi,
    'md_kuerzel':wifo + bwl + vwl + recht + sowi + philo,
    'v_sws':wifo + vwl + recht + philo,
    'v_aufwand_praesenz': wifo + bwl + vwl + philo,
    'v_aufwand_pruefungsvorbereitung': wifo + vwl + philo,
    'v_aufwand_selbststudium': wifo + bwl + philo,
    'v_ects': sowi + philo,
    'v_semester':sowi + philo,
}

helper_pruefung = {
    'pm_form': wifo + bwl + vwl + recht + sowi + philo,
    'pm_benotung': bwl + sowi + philo,
    'pm_vorraussetzung':  wifo + bwl  + sowi + philo,
    'dauer': wifo + bwl + sowi,
    'pm_anmeldung': '-',
}
