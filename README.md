# dymola-mat-converter


## Objectif

Cette pipeline Python convertit des fichiers de résultats Dymola (`.mat`) en formats analytiques exploitables :

- **Timeseries** → CSV / Parquet
- **Données statiques / géométrie / paramètres** → JSON

L’objectif est de faciliter l’analyse, la visualisation et l’intégration dans des outils web ou data science.

---

## Architecture de la pipeline

Dymola MAT
├─ Timeseries (len(series) == len(time)) → CSV / Parquet
└─ Static / Parameters / Geometry → JSON

**Modules :**

| Module               | Fonction                                                                |
| -------------------- | ----------------------------------------------------------------------- |
| `dymola_loader.py` | Chargement natif d’un MAT Dymola via DyMat                             |
| `normalizer.py`    | Extraction des variables temporelles et statiques                       |
| `exporter.py`      | Export des timeseries (CSV / Parquet) et des variables statiques (JSON) |
| `pipeline.py`      | Script CLI qui orchestre tout                                           |

---

## Entrée

- Fichier `.mat` Dymola
- Contenant :
  - `time` (vecteur temps)
  - Variables dynamiques (pressions, températures, débits…)
  - Variables statiques / géométriques (dimensions, paramètres, constantes)

---

## Étapes de traitement

1. **Chargement du MAT** via `DymolaMat` (DyMat)
2. **Détection du dataset principal** (plus grand `data_*`)
3. **Extraction des séries temporelles** : variables dont `len(series) == len(time)`
4. **Extraction des variables statiques** : constantes, vecteurs ou matrices
5. **Export des timeseries** : CSV & Parquet
6. **Export des statiques** : JSON

---

## Sorties

Pour un fichier `fichier.mat` :

data/csv/fichier.csv
data/parquet/fichier.parquet
data/json/fichier_static.json

- CSV / Parquet : séries temporelles synchronisées sur `time`
- JSON : variables constantes / paramètres / géométrie

---

## Utilisation

```bash
python src/pipeline.py data/raw/fichier.mat
Le script détecte automatiquement les types de variables.

Création automatique des dossiers data/csv, data/parquet et data/json.

Notes techniques
Les fichiers .mat Dymola peuvent contenir plusieurs datasets ou des fichiers statiques (géométrie / paramètres).

Seules les séries synchronisées sur time sont exportées en CSV / Parquet.

Les autres variables sont stockées en JSON pour éviter toute perte d’information.

Optimisé pour grandes simulations : une seule allocation mémoire pour le DataFrame afin d’éviter les warnings pandas de fragmentation.

```
