{
'name' : "twitter",
'version' : '1.0',
'author' : 'RAYANI ',
'category' : 'ENSAH ERP',
'sequence' :3,
'icon': "twit/static/pic/pic.png",
'description' : """
Module de visualisation des données.
======================================================
Ce module couvre les éléments suivants:
------------------------------------------------------
* Affichage des tweets d'un personnage public
* Affichage des tweets concernant un terme d'actualité
* Affichage des visuels
""",
'website': 'http://www.monsite.ma',
'images' : [''],
'depends' : ['base'],
'data': ['twit_principale_view.xml','twit_terme_view.xml','twit_visuel_view.xml','twit_principale_wkf.xml'],
'update_xml': [ ],
'js': [],
'qweb' : [],
'css':[],
'demo': [],
'test': [],
'installable': True,
'auto_install': False,
}