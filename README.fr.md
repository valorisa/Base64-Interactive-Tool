# Base64 Interactive Tool

Version française de la documentation.

Base64 Interactive Tool est un utilitaire léger permettant d'encoder et de
décoder des données en Base64. Écrit en Python pur, il met l'accent sur la
lisibilité, la simplicité, la testabilité et la maintenabilité.

Au-delà de son utilité pratique, ce dépôt constitue également un exemple de
transformation d'un simple script Python en un projet open source moderne et
bien structuré.

---

## Fonctionnalités

- Encodage de texte Unicode en Base64
- Décodage de chaînes Base64
- Mode interactif
- Interface en ligne de commande (CLI)
- Fonctions métier pures
- Hiérarchie d'exceptions dédiée
- Architecture modulaire
- Tests unitaires complets
- Organisation moderne d'un projet Python
- Conçu pour évoluer facilement

---

## Prérequis

- Python 3.11 ou version ultérieure

---

## Installation

Cloner le dépôt :

```bash
git clone https://github.com/valorisa/base64-interactive-tool.git

cd base64-interactive-tool
```

Installation en mode développement :

```bash
python -m pip install -e .
```

---

## Utilisation

### Encoder un texte

```bash
base64-tool encode "bonjour"
```

Résultat :

```text
Ym9uam91cg==
```

### Décoder une chaîne Base64

```bash
base64-tool decode "Ym9uam91cg=="
```

Résultat :

```text
bonjour
```

### Mode interactif

```bash
python -m base64_tool
```

---

## Organisation du projet

```text
base64_tool/
├── __init__.py
├── __main__.py
├── cli.py
├── codec.py
├── exceptions.py
├── interactive.py
└── validator.py

docs/
tests/
```

---

## Architecture

Le projet est volontairement découpé en petits modules, chacun ayant une
responsabilité unique.

| Module | Responsabilité |
| ------- | -------------- |
| `codec.py` | Encodage et décodage Base64 |
| `validator.py` | Validation des entrées |
| `interactive.py` | Interface utilisateur interactive |
| `cli.py` | Interface en ligne de commande |
| `exceptions.py` | Exceptions spécifiques au projet |

---

## Développement

Exécuter l'ensemble des tests :

```bash
python -m pytest
```

Compiler tous les modules :

```bash
python -m compileall base64_tool
```

---

## Principes de conception

Le projet repose sur quelques principes simples.

- Modules de petite taille
- Responsabilité unique
- Fonctions pures
- Exceptions explicites
- Code lisible
- Tests unitaires systématiques
- Évolution progressive
- Maintenance facilitée

---

## Devise du projet

> Assez simple pour être lu d'une traite.
>
> Assez élégant pour donner envie d'être relu.
>
> Assez maintenable pour évoluer pendant des années.

Version originale :

> Simple enough to read in one sitting.
>
> Elegant enough to enjoy reading.
>
> Maintainable enough to evolve for years.

---

## Feuille de route

Les prochaines versions pourront notamment proposer :

- Encodage et décodage de fichiers
- Prise en charge du presse-papiers
- Amélioration de l'ergonomie de la CLI
- Nouveaux formats de sortie
- Mesure de la couverture de tests
- Intégration continue (GitHub Actions)

---

## Contribution

Les contributions sont les bienvenues.

Pour toute évolution importante, merci d'ouvrir une *Issue* afin de discuter
de la proposition avant de soumettre une *Pull Request*.

---

## Licence

Ce projet est distribué sous licence MIT.

Le document principal du projet est rédigé en anglais dans
[`README.md`](README.md). Cette version française est fournie pour faciliter
la lecture des utilisateurs francophones.
