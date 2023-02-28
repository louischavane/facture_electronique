# Facture Electronique

Ce projet présente une API utilisant le module open-source [factur-x](https://github.com/akretion/factur-x) et renvoyer les données structurée sous format JSON. 

## Resources 
- XML format BASIC de la norme factur-X [ici](https://github.com/invoice-x/factur-x-ng/blob/master/facturx/flavors/factur-x/xml/samples/basic.xml)

## Documentation API 

### Analyser une facture

`POST /analyze`

*parametres*
|Parametre|Type|Description|
|:----:|:----:|:----:|
|file|Fichier|Facture X à analyser|
