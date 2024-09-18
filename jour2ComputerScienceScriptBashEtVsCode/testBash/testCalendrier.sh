#!/usr/bin/bash

MOIS=("Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre")
JOUR=("31", "28", "31", "30", "31", "30", "31", "31", "30", "31","30", "31")

ANNEE=$1

rm -rf $ANNEE
mkdir $ANNEE 

if (ANNEE % 4 == 0); then 
    JOUR[1] = "29"
fi 

echo $MOIS
echo $JOUR

