# HISTORIC MARC LOPEZ I CESC MOLERO

PROJECTE: M0487_RA4_Refactorització_Documentació_Git
Mòdul: 0487-Entorns de Desenvolupament
Alumnes: CESC MOLERO  MARC LOPEZ
Data d'inici: 23-04

---

## PRIMERA PART – CREEM LA ESTRUCTURA DEL PROJECTE

**Data:** 2025-04-23  
**Responsable:** MARC LOPEZ CESC MOLERO  
**Responsable:** MARC LOPEZ CESC MOLERO  
**Canvis realitzats:**
- HEM FET ELS ARXIUS GESTOR_GRUPS.PY, GRUPS_MUSICA.DB. README.md, TEST_GRUPS.py

---

## SEGONA PART – MODIFIQUEM ELS ARXIUS GESTOR_GRUPS.py

**Data:** 2025-04-23  
**Responsable:** Marc Lopez
**Canvis realitzats:** Ha implementat el consular grups dintre del arxiu GESTOR_GRUPS.py
- Funcions: actualitzar_grup(nom_grup)

---

## TERCERA PART – CREAR EL ARXIU TEST_GRUPS.PY
## TERCERA PART – CREAR EL ARXIU TEST_GRUPS.PY

**Data:** 2025-04-23  
**Responsable:** MARC LOPEZ CESC MOLERO
**Canvis realitzats:**
- Creació de la classe TestValidacions
- Validació d’entrades amb bucles per:
  - Any d'inici (≥ 1960)
  - Tipus de música (no números)
  - Nombre d'integrants (> 0)
- Substitució dels `input()` directes per crides a `intro_dades()` a `afegir_grup()` i `actualitzar_grup()`

---

## QUARTA PART – Actualitzacio del HISTORIC.md i el README.md

**Data:** 2025-04-23  
**Responsable:** Cesc Molero 
**Canvis realitzats:**
- He creats els dos arxius on poder anar documentar la part historica 


---

## 🔜 PENDENT / PROPERES TASQUES

- Separar el projecte en mòduls (`main.py`, `database.py`, `utils.py`)
- Afegir tests amb `unittest`
- Preparar el `README.md`
- Fer branques a Git i enregistrar commits individuals