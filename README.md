# RoomsyDevs — Plataforma de turismo y hospedaje con identidad local

**Grupo 17 — Proyecto Integrador | Tecnicatura Superior en Desarrollo Web y Aplicaciones Digitales**

**Integrantes:**
- Martín Ignacio Bentivoglio
- María Florencia Lorenzati
- Sofía Desiree Martinez
- Griselda Leonor Aguirre
- María Agustina Alonzo

---

## Descripción del proyecto

RoomsyDevs es una plataforma web orientada a fortalecer el turismo de cercanía en la provincia de Córdoba. Conecta turistas con anfitriones locales que ofrecen hospedajes con identidad propia, promoviendo experiencias auténticas y sostenibles. El contacto se realiza directamente entre turista y anfitrión, sin intermediarios.

La plataforma se comercializa como un servicio pago: los anfitriones abonan una cuota mensual para publicar sus hospedajes y acceder a funcionalidades de gestión. El MVP se enfoca en funcionalidades esenciales, con posibilidad de escalar en futuras versiones.

---

## Problema a resolver

Muchos hospedajes familiares o rústicos en Córdoba no tienen presencia digital efectiva, lo que limita su visibilidad y acceso por parte de turistas. Las plataformas tradicionales priorizan opciones comerciales, invisibilizando lo local.

RoomsyDevs busca revertir esta situación con:
- Una plataforma accesible que prioriza la identidad territorial.
- Registro simple para anfitriones.
- Herramientas para que los turistas descubran hospedajes según la ubicación y puedan contactar al anfitrión.

---

## Funcionalidades del MVP

- Registro e inicio de sesión para turistas y anfitriones.
- Validación de formularios con mensajes de errores claros.
- Visualización pública de hospedajes sin necesidad de registro.
- Contacto directo entre turista y anfitrión (formulario o teléfono).
- Envío de formulario por parte del anfitrión para solicitar publicación.
- Validación manual por parte del administrador (funcionalidad no disponible en este sprint)
- Gestión de roles diferenciados (turista, anfitrión, administrador).
- Visualización responsive desde dispositivos móviles.

---

#### Funcionalidades Clave Adicionales

- Página de inicio y vista de detalle: Además de la galería, los usuarios pueden ver una página de bienvenida y una vista detallada de cada hospedaje.
- Gestión del ciclo de vida del hospedaje: Los anfitriones pueden pausar o eliminar sus publicaciones.
- Gestión de la cuenta por el usuario: Los usuarios pueden modificar sus datos personales y eliminar su propia cuenta.
- Gestión de usuarios por el administrador: Los administradores tienen la capacidad de eliminar cuentas de usuario.
- Seguridad de acceso: Se ha implementado un límite de intentos de inicio de sesión para proteger las cuentas.

> **Importante:** No se incluye gestión automatizada de reservas ni pasarela de pagos en el MVP. Las reservas se gestionan directamente entre turista y anfitrión.

---

## Aspectos técnicos

- Funciona exclusivamente en entorno web.
- Es responsive y accesible desde celulares.
- Compatible con navegadores modernos (Chrome, Firefox, Safari, Edge).
- Tecnologías: HTML, CSS, JavaScript, Bootstrap, Python y MySQL.

---

## Funcionalidades futuras (no incluidas en el MVP)
- Guardar hospedajes en favoritos.
- Reseñas de hospedajes.
- Chat interno entre turista y anfitrión.
- Pasarela de pagos para reservas.
- Calendario editable de disponibilidad.
- Panel de métricas para anfitriones.
- Gestión automática de pagos mensuales.
- Cuota de inscripción para publicar hospedajes.
- Aplicación móvil nativa (Android/iOS).


---

## Tipos de usuarios

| Rol           | Actividades principales |
|---------------|-------------------------|
| **Turista**       | Buscar hospedajes, contactar anfitriones |
| **Anfitrión**     | Registrar hospedajes, editar perfil, recibir consultas |
| **Administrador** | Validar registros, asignar roles, gestionar contenido |
| **Otros**         | Emprendedores turísticos, agencias locales, entes de turismo |

---

## Documentación

- [Wiki del proyecto](https://github.com/RoomsyDevs/FullStack/wiki/Documentaci%C3%B3n-y-Enlaces-%C3%9Atiles)  

---

> Documento elaborado bajo metodología ágil (Scrum), siguiendo el estándar IEEE 830.  
> Proyecto académico — Instituto Superior Politécnico Córdoba (ISPC) — Cohorte 2025.
