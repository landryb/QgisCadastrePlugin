Description
===========

A partir du [plugin Qadastre pour QGIS] (https://github.com/3liz/QgisCadastrePlugin), la fonctionalité d'import a été isolée pour pouvoir l'utiliser indépendamment de QGIS, afin de scripter des imports de données en base via la ligne de commande.

Dépendances
===========

Sur un système debian stretch, les paquets suivants sont nécessaires ( a prendre depuis le dépot `qgis-ltr` de https://www.qgis.org/fr/site/forusers/alldownloads.html) :
```
python3-qgis

```

Il faut cloner le repository :
```
git clone -b import_cli https://github.com/landryb/QgisCadastrePlugin.git
cd QgisCadastrePlugin
```

Configuration
=============

Comme prérequis, il faut avoir crée une base de donnee vide sur un serveur PostGreSQL avec l'extension PostGIS activée (au moins la version 2.0), et renseigner le fichier [https://github.com/landryb/QgisCadastrePlugin/blob/import_cli/config.ini](config.ini) pour permettre à l'import des données de viser cette base:
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

Ce fichier de configuration à la même syntaxe/structure que le fichier de configuration de QGIS qui sauvegarde les paramètres du plugin cadastre, que vous pouvez trouver dans .config/QGIS/QGIS2.conf sur un système unix. Uniquement les sections *cadastre* et *PostgreSQL* sont nécessaires pour le fonctionnement de l'import avec la ligne de commande, la section *cadastre* regroupe les paramètres que l'on renseigne habituellement dans le plugin: noms des fichiers MAJIC, chemins des répertoires contenant les données, millésimes, etc..


Import des données
==================
Pour lancer l'import il suffit de lancer cette commande:
```
python3 do_import.py
```

Le script va lire le fichier *config.ini* dans le répertoire courant, et importer les données dans la base ciblée. La sortie écran est la même que ce qui serait affiché dans le plugin QGIS.
