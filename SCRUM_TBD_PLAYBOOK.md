# 📘 Scrum + Trunk-Based Development (TBD) Playbook

**Versión:** 2.0 (Actualizado con acuerdos de equipo y flujo continuo)  
**Repositorio:** [https://github.com/nfruiz23-lang/Web](https://github.com/nfruiz23-lang/Web)  
**Estado:** Activo / Normativo  

Este playbook establece los acuerdos operativos, roles, reglas de integración, Definition of Ready (DoR) y Definition of Done (DoD) para trabajar con **Trunk-Based Development (TBD)** y **Continuous Deployment (CD)** en nuestro equipo.

---

## 1. Diagnóstico del Flujo Operativo

- **Flujo de Trabajo:** `Commit Local` ➔ `PR Corto (< 24h)` ➔ `CI Automatizado (Ruff + Pytest)` ➔ `Code Review Rápida (< 2h)` ➔ `Merge a main` ➔ `Docker Build & Push (GHCR)` ➔ `Deploy Continuo`.
- **Fricciones Superadas:**
  1. **Ramas de Larga Duración:** Eliminadas mediante *story slicing* vertical ($\le 24$h por incremento).
  2. **Cuellos de Botella en Code Reviews:** Resueltos mediante acuerdos de SLA de revisión $< 2$ horas para lotes pequeños (< 150 líneas).
  3. **Desacoplamiento Deploy / Release:** Despliegue técnico automatizado e independiente de la liberación comercial mediante **Feature Toggles** (ConfigCat).

---

## 2. Roles Adaptados a TBD + Continuous Deployment

| Rol | Responsabilidad Tradicional | Nueva Responsabilidad en TBD + CD |
| :--- | :--- | :--- |
| **Product Owner (PO)** | Define requisitos en sprints largos; espera a la Review para validar. | • Participa activamente en el **Story Slicing** vertical ($\le 24$h).<br>• Gestiona el ciclo de vida de los **Feature Toggles** (activación gradual en ConfigCat).<br>• Redacta Criterios de Aceptación observables directamente en producción. |
| **Developers** | Desarrollan en ramas aisladas durante días; integran al final del sprint. | • **Ownership colectivo del pipeline:** Si `main` falla (rojo), la prioridad absoluta es repararlo.<br>• Integrar código a `main` al menos **una vez al día** en lotes muy pequeños.<br>• Escribir pruebas unitarias automatizadas junto con el código (CI siempre en verde). |
| **Scrum Master** | Facilita ceremonias tradicionales y mide velocidad. | • Promueve la disciplina de ramas de corta vida ($\le 24$h) y remueve bloqueos de CI/CD.<br>• Vela por el cumplimiento del Definition of Ready (DoR) antes del Sprint Planning. |

---

## 3. Acuerdos de Equipo (Team Agreements)

1. **Revisión de PRs en SLA $< 2$ Horas:** Todo miembro del equipo prioriza la revisión de PRs pequeños sobre el desarrollo activo para mantener el flujo continuo.
2. **Propiedad Colectiva del Pipeline ("Stop the Line"):** Si un commit o merge rompe `main`, todo el equipo detiene tareas secundarias hasta restaurar la rama principal.
3. **Cero Ramas Huérfanas / Larga Duración:** Ninguna rama de trabajo vive más de 24 horas sin fusionarse a `main` o descartarse.
4. **Despliegues Seguros con Feature Toggles:** Toda nueva funcionalidad que pueda afectar la experiencia del usuario final ingresa desactivada (0% rollout) en ConfigCat.
5. **Comunicación en Daily Standup:** La Daily se enfoca en la integración diaria: *¿Qué voy a integrar hoy a main y qué flag protege el cambio?*

---

## 4. Definition of Ready (DoR) para TBD

Una historia de usuario solo ingresa al **Sprint Backlog** si satisface el 100% de los siguientes criterios:

1. **[x] Sliceado Vertical ($\le$ 24 Horas):** Dividida de forma que un desarrollador pueda codificarla, probarla e integrarla a `main` en menos de un día (lotes $< 150-200$ líneas).
2. **[x] Acceptance Criteria Observables:** Condiciones de satisfacción redactadas para verificación en producción (en vivo o mediante toggles).
3. **[x] Estrategia de Feature Toggle Definida:** Identificador técnico del flag en ConfigCat (ej. `ENABLE_MULTIPLICATION`, `ENABLE_DIVISION`) y estado inicial apagado (Rollout 0%).
4. **[x] Cero Dependencias Bloqueantes Externas:** Sin bloqueos técnicos, esquemas de datos inconclusos ni APIs de terceros sin mockear.
5. **[x] Criterios de Prueba Comprendidos:** Claridad total en cómo `pytest` y la validación de entorno confirmarán el éxito del cambio.

---

## 5. Acuerdos de Planificación Orientada a Flujo (Flow Planning)

### Reglas de Ordenación del Sprint Backlog:
1. **Regla del Día 1:** El primer ítem del Sprint Backlog debe tener commit y merge a `main` el **Día 1 del sprint**.
2. **Fases de Integración Segura:**
   - **Día 1-2 (Dark Launch / Core Logic):** Lógica principal, algoritmos y tests unitarios. Flag desactivado (0%). Cero impacto visual.
   - **Días 3-4 (Canary Rollout / UI Connection):** Integración visual en la interfaz y rollout progresivo al 10% para PO/pilotos.
   - **Día 5+ (Feature Completion & Flag Sunset):** Rollout al 100% y tarea agendada para remoción del condicional de toggle.

---

## 6. Reglas de Oro de Integración a Main (TBD Golden Rules)

1. **Vida de rama máxima de 24 horas:** Ningún branch sobrevive más de un día sin merge a `main`.
2. **Main siempre en verde y desplegable:** Si el pipeline de GitHub Actions falla, se arregla o se revierte en $< 10$ minutos.
3. **Validación local obligatoria:** Ejecución local de `ruff check .` y `pytest` previo a realizar push.
4. **Desacoplar Deploy de Release:** Desplegar a producción es continuo; activar el valor al usuario es una decisión de negocio.
5. **Lotes Pequeños (Small Batches):** Commits atómicos de 50 a 150 líneas para evitar conflictos de integración.

---

## 7. Definition of Done (DoD) Consolidado

Un incremento se considera **DONE** cuando:

- [x] Pruebas unitarias automatizadas cubren los caminos principales y de excepción.
- [x] Linter `ruff` ejecutado sin advertencias ni errores.
- [x] Pipeline de CI en GitHub Actions verificado en verde (Jobs de `test` y `build_and_push`).
- [x] Imagen Docker construida y publicada en GitHub Container Registry (`ghcr.io`).
- [x] Feature Toggle configurado y verificado en ConfigCat si la función no es pública aún.
- [x] Criterios de Aceptación validados por el PO en el ambiente desplegado.
- [x] Tarea agendada para limpieza y remoción del toggle una vez lanzado al 100% (Flag Sunsetting).
