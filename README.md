# DES Algorithm

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Statut](https://img.shields.io/badge/Statut-En%20développement-yellow.svg)

Implémentation complète de l'algorithme DES (Data Encryption Standard) avec une interface graphique en cours de développement.


## Fonctionnalités Implémentées

### Cryptographie DES
- Chiffrement/déchiffrement 64-bit
- 16 tours de Feistel
- Génération des 16 sous-clés
- Permutations IP/IP⁻¹, E, P
- Substitutions par S-boxes

### Traitement de Texte
- Conversion ASCII/binaire
- Padding automatique (PKCS#7)
- Découpage en blocs de 64 bits

## Travail en Cours

### Interface Graphique (GUI)
🚧 **En développement** :
- Fenêtre principale avec zones de texte
- Boutons de chiffrement/déchiffrement
- Affichage des résultats binaires
- Gestion des erreurs utilisateur

### Fonctionnalités à Venir
- Export des résultats en fichier
- Visualisation des étapes intermémentaires
- Support des modes ECB/CBC

## Utilisation

### Prérequis
- Python 3.8+
- Tkinter (généralement inclus avec Python)

### Installation
```bash
git clone https://github.com/zikoelj/DES_Algorithm.git
cd DES_Algorithm
```

### Caractéristiques de ce README.md :
1. **Badges visuels** pour le statut et la version Python
2. **Structure claire** avec arborescence du projet
3. **Sections détaillées** pour chaque composant
4. **Mise en évidence** des fonctionnalités en développement
5. **Instructions d'installation** et d'utilisation simples
6. **Notes importantes** sur l'état du projet

Pour l'utiliser :
1. Copiez ce contenu dans un fichier `README.md` à la racine de votre projet
2. Personnalisez les liens et informations spécifiques
3. Mettez à jour au fur et à mesure de l'avancement du projet
