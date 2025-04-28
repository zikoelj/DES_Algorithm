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

Contribution
Les contributions sont les bienvenues pour :

Améliorer l'interface graphique

Optimiser les performances

Ajouter des tests unitaires

Améliorer la documentation

Licence
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.
