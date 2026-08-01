# Base64 Interactive Tool

Un outil CLI minimaliste et zero-dependance en Python pour encoder et décoder du texte en Base64.

## Spécifications & Limites

- **Texte UTF-8 uniquement** : Cet outil ne prend pas en charge les fichiers ou flux binaires (images, archives).
- **Mode Pipe / Redirection** : En flux non-interactif, l'entrée est **encodée par défaut**. Passer `-d` ou `--decode` pour forcer le décodage.
- **Mode Terminal (TTY)** :
  - Sans argument : Affiche un menu interactif (1/2/q).
  - Avec argument (`-e` ou `-d`) : Saute le menu et demande directement la chaîne à traiter.
- **Validation stricte** : Toute option inconnue ou combinaison contradictoire (`-e` et `-d`) renvoie une erreur sur `stderr` (exit status 2).

## Exemples d'utilisation

```bash
# 1. Mode menu interactif TTY
python base64_tool.py

# 2. Mode interactif direct (saute le menu)
python base64_tool.py -d

# 3. Pipe Unix (Encodage par défaut)
echo "Hello World" | python base64_tool.py

# 4. Pipe Unix (Décodage)
echo "SGVsbG8gV29ybGQ=" | python base64_tool.py -d

# 5. Lancement de la suite de tests unitaires
python -m unittest discover

