Taller 6: Sprint Review, Retrospective y Liberación Segura en Continuous Deployment
Formato: Hands-on + simulación real + decisiones de equipo
Nivel: Profesional
Prerrequisito: Talleres 1, 2 y 3 completados + Pipeline funcionando (auto-deploy + ConfigCat + DoD final)
Objetivo general
Adaptar las ceremonias de Sprint Review y Sprint Retrospective al nuevo ritmo de despliegues continuos, y practicar la liberación segura de valor usando Feature Toggles y el pipeline real.
________________________________________
Materiales necesarios
•	Repo real + GitHub Projects
•	Render (app desplegada)
•	ConfigCat (toggles activos)
•	Scrum + TBD Playbook (versión 3.0)
•	Miro
•	Timer visible
•	Acceso a métricas básicas (si las tienen: tiempo de CI, deploys, etc.)
________________________________________
Agenda optimizada
Apertura y conexión con el nuevo flujo 
“Ya tenemos el pipeline completo: integramos a main, se despliega solo y podemos proteger funcionalidades con toggles.
Hoy vamos a responder una pregunta clave:
¿Cómo cambian el Sprint Review y la Retrospective cuando desplegamos varias veces por semana?”
Pregunta de arranque:
“¿Qué parte del Review o de la Retro actual se siente más ‘antigua’ o poco útil con este nuevo flujo?”
________________________________________
1. Adaptación del Sprint Review al Continuous Deployment 
Objetivo: Convertir el Review en una demostración de valor real en producción (o activable).
1.1 Principios del nuevo Review 
Mostrar la diferencia:
Review clásico	Review en CD + TBD
Demo del incremento del sprint	Demo de lo que ya está (o puede estar) en producción
Todo o nada	Valor incremental + toggles
Feedback al final del sprint	Feedback continuo + validación real
Enfocado en “qué construimos”	Enfocado en “qué valor recibieron los usuarios”
1.2 Simulación de Sprint Review 
Actividad práctica:
1.	El equipo elige 2-3 incrementos reales que ya estén en main (o protegidos por toggle).
2.	Estructura obligatoria de la demo (cada ítem máximo 4-5 min):
o	¿Qué problema de usuario resuelve?
o	¿Está activo para todos o detrás de toggle?
o	Demo en vivo en Render (toggle ON/OFF si aplica)
o	Métrica o evidencia de valor (si existe)
o	Pregunta al stakeholder/PO: “¿Esto genera el valor esperado?”
3.	Roles durante la simulación:
o	Un Developer hace la demo técnica
o	El PO facilita el feedback
o	El resto observa y anota mejoras al formato
Resultado esperado: Formato de Review acordado y probado.
________________________________________
2. Adaptación de la Sprint Retrospective 
Objetivo: Convertir la Retro en una inspección del flujo de valor + salud del pipeline + disciplina TBD.
2.1 Nuevos focos de la Retrospective 
La Retro ahora debe revisar obligatoriamente:
1.	Salud del Pipeline
o	¿Cuántas veces se rompió el CI?
o	¿Cuánto tardó el deploy promedio?
o	¿Hubo rollbacks?
2.	Disciplina TBD
o	¿Cuántas integraciones diarias a main logramos?
o	¿Alguna rama vivió más de 1 día?
o	¿Usamos Feature Toggles correctamente?
3.	Flujo de valor
o	Lead Time (desde que se empieza hasta que está en producción)
o	¿El valor llegó realmente a los usuarios?
2.2 Dinámica de Retrospective 
Formato recomendado ( usar Miro):
Columnas:
•	🟢 Lo que funcionó bien en el flujo
•	🟡 Lo que generó fricción
•	🔴 Lo que rompió el flujo o generó miedo
•	🚀 Acciones de mejora (máximo 3)
Preguntas guía del facilitador:
•	¿Qué nos impidió integrar más veces a main?
•	¿El auto-deploy nos dio más confianza o más miedo?
•	¿Los Feature Toggles nos ayudaron o se volvieron deuda?
•	¿El DoD se respetó realmente?
Regla: Solo se eligen máximo 3 acciones concretas y asignables.
________________________________________
3. Liberación Segura de Valor  
Objetivo: Practicar el ciclo completo de liberación controlada.
Ejercicio práctico en vivo:
1.	Tomar una funcionalidad que esté detrás de Feature Toggle.
2.	Definir juntos la estrategia de liberación:
o	¿A quién se la activamos primero? (interno → % de usuarios → todos)
o	¿Qué métrica vamos a observar?
o	¿Cuál es el criterio para dejarla 100% ON o hacer rollback?
3.	Activar el toggle en ConfigCat (o simularlo).
4.	Verificar en Render que el cambio es visible.
5.	Definir el plan de observación de las próximas 24-48 horas.
Resultado esperado: Primera liberación controlada practicada + acuerdo de cómo se harán las siguientes.
________________________________________
4. Actualización del Playbook y cierre 
1.	Actualizar el Scrum + TBD Playbook con:
o	Formato oficial del nuevo Sprint Review
o	Formato oficial de la nueva Retrospective
o	Política de liberación segura (toggles + observación)
2.	Revisar el checklist de Fase 1 (ya debe estar 100% cerrado).
3.	Ronda final:
“En una frase: ¿Qué cambia en nuestro próximo Review y Retro después de este taller?”
________________________________________
Resultado final esperado del Taller 6
•	Sprint Review adaptado y probado
•	Sprint Retrospective enfocada en flujo + pipeline + TBD
•	Primera práctica de liberación segura con Feature Toggle
•	Playbook actualizado con las nuevas ceremonias
•	Equipo listo para operar en Continuous Deployment rea
Ejemplo a tener en cuenta:
Ejemplo para el Taller 6
Título del caso:
“La funcionalidad de ‘Pagos Express’ ya está en main, pero nadie se atreve a activarla”
________________________________________
Contexto del caso 
El equipo lleva 2 sprints trabajando con el nuevo flujo (auto-deploy + ConfigCat + DoD final).
Situación actual:
•	La historia “Pagos Express con un solo clic” fue sliceada e integrada a main hace 9 días.
•	Está protegida por el Feature Toggle: pagos-express-v1 (actualmente en OFF para el 100% de los usuarios).
•	El código pasó CI, se desplegó automáticamente a Render y cumple el DoD técnico.
•	Sin embargo, en las últimas 2 semanas han ocurrido los siguientes hechos:



Hechos problemáticos:
1.	El Product Owner quiere activar el toggle para el 20% de los usuarios este mismo viernes porque hay presión comercial (campaña de marketing ya lanzada).
2.	El último deploy automático (hace 2 días) falló el health check durante 11 minutos. Se resolvió con un rollback manual.
3.	Hay 3 Feature Toggles antiguos que llevan más de 45 días activos y nadie los ha limpiado.
4.	En el Sprint actual solo se lograron 4 integraciones a main (muy por debajo del objetivo de integración diaria).
5.	Un desarrollador reportó que para terminar “Pagos Express” tuvo que mantener una rama viva 4 días porque el CI estaba rojo por un test flaky.
6.	No existe ninguna métrica clara de conversión o error de pagos que se pueda observar al activar el toggle.
7.	El stakeholder de Negocio ya anunció internamente que “Pagos Express ya está listo”.
 
________________________________________
### Resolución del Caso Práctico (Aplicando la Agenda del Taller)

Para abordar la situación de "Pagos Express", el equipo debe ejecutar las 4 fases del taller en el siguiente orden:

#### 1. Adaptación del Sprint Review (Gestión de Expectativas)
- **Problema a resolver:** El stakeholder anunció que "Pagos Express ya está listo" (Hecho 7) sin entender que faltan validaciones, y hay presión por activarlo (Hecho 1).
- **Acción:** En el Review, usar la *Simulación de Sprint Review* para educar a Negocio.
- **Demo en Vivo:** El equipo muestra en Render la aplicación y explica la diferencia entre "código integrado" y "funcionalidad liberada". Muestran el toggle apagado.
- **Mensaje Clave:** *"La funcionalidad está en producción pero oculta para proteger la experiencia del usuario. No se puede liberar al 20% aún porque carecemos de métricas para medir el éxito o los fallos de los pagos (Hecho 6)."*

#### 2. Adaptación de la Sprint Retrospective (Inspección del Flujo y Pipeline)
- **Problema a resolver:** Baja frecuencia de integración (Hecho 4), ramas longevas por un test flaky (Hecho 5), fallos recientes en deploy (Hecho 2) y deuda técnica en toggles (Hecho 3).
- **Dinámica en Miro (Acciones concretas de mejora):**
  - 🔴 **Lo que rompió el flujo:** El test flaky que mantuvo una rama viva por 4 días y bloqueó integraciones. *Acción de mejora 1:* Reparar o aislar el test flaky con máxima prioridad en el siguiente sprint.
  - 🟡 **Lo que generó fricción:** El rollback manual por el health check de 11 min. *Acción de mejora 2:* Revisar y ajustar los timeouts del health check de Render para que el rollback automático actúe más rápido.
  - 🟡 **Deuda técnica:** 3 Feature Toggles antiguos. *Acción de mejora 3:* Asignar tareas obligatorias en el próximo sprint para limpiar los toggles con más de 45 días en el código.

#### 3. Liberación Segura de Valor (Ejecución Controlada)
- **Problema a resolver:** El PO quiere activar al 20% el viernes, pero no hay observabilidad (Hecho 6).
- **Estrategia de Liberación:**
  1. **Requisito Bloqueante:** Antes del viernes, el equipo *debe* agregar telemetría básica (ej. log de pagos fallidos/exitosos). No se activa el toggle sin esto.
  2. **Definir la observación:** Decidir la métrica que dirá si la campaña está fallando (ej. más de 5 errores de pago en 10 minutos).
  3. **Plan de Activación:** No ir directo al 20%. Activar primero para el equipo interno (QA/Devs), simular pagos y validar que no hay regresiones. Luego, si es estable, habilitar el 20% para la campaña de marketing el viernes, monitoreando de cerca las primeras horas.

#### 4. Actualización del Playbook y Cierre
- **Actualizar Acuerdos:**
  - Agregar al *Playbook* que **ningún feature toggle se activa en producción sin tener su métrica de validación asociada**.
  - Documentar la política de limpieza de toggles (ej. "los toggles no deben durar más de 30 días sin limpiarse").
- **Cierre:** Responder a la pregunta final del taller confirmando que de ahora en adelante el equipo tiene el control y la confianza sobre *cuándo y cómo* liberar código.
