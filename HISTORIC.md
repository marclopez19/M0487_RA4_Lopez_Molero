# 📜 HISTÒRIC DE DESENVOLUPAMENT

Projecte: Gestor de Grups Musicals  
Mòdul: M0487 - Desenvolupament d'Interfícies  
Alumnes: CognomAlumne1, CognomAlumne2  
Data d'inici: 2025-04-23

---

## ✅ FASE 1 – Configuració inicial i estructura del projecte

**Data:** 2025-04-23  
**Responsable:** CognomAlumne1  
**Canvis realitzats:**
- Creació del fitxer principal `main.py`
- Configuració de la base de dades SQLite (`grups_musica.db`)
- Funció `crear_taula()` implementada

---

## ✅ FASE 2 – Funcions CRUD i Menú

**Data:** 2025-04-23  
**Responsable:** CognomAlumne2  
**Canvis realitzats:**
- Funcions: `afegir_grup()`, `mostrar_grups()`, `eliminar_grup()`, `actualitzar_grup()`
- Menú d’usuari amb opció per a cada acció

---

## ✅ FASE 3 – Refactorització amb `intro_dades()` reutilitzable

**Data:** 2025-04-23  
**Responsable:** CognomAlumne1  
**Canvis realitzats:**
- Creació de la funció `intro_dades()`
- Validació d’entrades amb bucles per:
  - Any d'inici (≥ 1960)
  - Tipus de música (no números)
  - Nombre d'integrants (> 0)
- Substitució dels `input()` directes per crides a `intro_dades()` a `afegir_grup()` i `actualitzar_grup()`

---

## 🔧 FASE 4 – Millores visuals i usabilitat

**Data:** 2025-04-23  
**Responsable:** CognomAlumne2  
**Canvis realitzats:**
- Millora de missatges d’error i confirmació amb emojis
- Ordenació i neteja de codi
- Format més llegible en la sortida de grups

---

## 🔜 PENDENT / PROPERES TASQUES

- Separar el projecte en mòduls (`main.py`, `database.py`, `utils.py`)
- Afegir tests amb `unittest`
- Preparar el `README.md`
- Fer branques a Git i enregistrar commits individuals