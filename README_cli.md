Description
===========

A partir du [plugin Qadastre pour QGIS] (https://github.com/3liz/QgisCadastrePlugin), la fonctionalite d'import a ete isolee pour pouvoir l'utiliser independamment de QGIS, afin de scripter des imports de donnees en base via la ligne de commande.

Dependances
===========

Sur un system debian wheezy, les paquets suivants sont necessaires :
```
python-qt4 python-gdal libqt4-sql-psql libqt4-sql-sqlite
```

Il faut cloner le repository :
```
git clone -b import_cli https://github.com/landryb/QgisCadastrePlugin.git
cd QgisCadastrePlugin
```

Configuration
=============

Comme prerequis, il faut avoir cree une base de donnee vide sur un serveur PostGreSQL avec l'extension PostGIS activee (au moins la version 2.0), et renseigner le fichier [https://github.com/landryb/QgisCadastrePlugin/blob/import_cli/config.ini](config.ini) pour permettre a l'import des donnees de viser cette base:
```
[PostgreSQL]
connections\selected=qadastre
connections\qadastre\host=127.0.0.1
connections\qadastre\database=cadastre
connections\qadastre\port=5432
connections\qadastre\username=cadastre
connections\qadastre\password=cadastre
connections\qadastre\schema=public
connections\qadastre\publicOnly=false
connections\qadastre\geometryColumnsOnly=false
connections\qadastre\save=true
```

Ce fichier de configuration a la meme syntaxe/structure que le fichier de configuration de QGIS qui sauvegarde les parametres du plugin cadastre, que vous pouvez trouver dans .config/QGIS/QGIS2.conf sur un systeme unix. Uniquement les sections *cadastre* et *PostgreSQL* sont necessaires pour le fonctionnement de l'import avec la ligne de commande, la section *cadastre* regroupe les parametres que l'on renseigne habituellement dans le plugin: noms des fichiers MAJIC, chemins des repertoires contenant les donnees, millesimes, etc..


Import des donnees
==================
Pour lancer l'import il suffit de lancer cette commande:
```
python do_import.py
```

Le script va lire le fichier *config.ini* dans le repertoire courant, et importer les donnees dans la base ciblee. La sortie ecran est la meme que ce qui serait affiche dans le plugin QGIS.
