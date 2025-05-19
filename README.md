# 📚 ABP - Evidencia 02

## 📌 Descripción del Proyecto

Esta evidencia corresponde al segundo entregable del proyecto de Aprendizaje Basado en Proyectos (ABP2). En esta etapa se desarrolló una solución que incluye la gestión de dispositivos y funcionalidades como el registro de usuarios, autenticación, y el modo de ahorro energético para cámaras de seguridad.

---

## 🧩 Objetivos

- Implementar un sistema de gestión de dispositivos por usuario.
- Permitir el registro y almacenamiento persistente de dispositivos.
- Activar/desactivar el **modo ahorro** específicamente en cámaras de seguridad.
- Guardar la información en archivos `.json` para persistencia de datos.

---

## ⚙️ Funcionalidades Principales

- ✅ Registro de usuarios y dispositivos.
- ✅ Clasificación de dispositivos por tipo (cámara, sensor, etc.).
- ✅ Activación interactiva del modo ahorro por cámara.
- ✅ Guardado y carga automática desde `usuarios.json` y `dispositivos.json`.

---

## 🧪 Evidencia de funcionamiento

### Registro de dispositivo:
```bash
Ingrese el nombre de dispositivo: camara-01
Seleccione el tipo de dispositivo: 1. Cámara de seguridad
Ingrese el modelo de su dispositivo: c300
✅ Dispositivo registrado con éxito.

Seleccione la cámara que desea activar en modo ahorro:
1. camara-01 (modelo: c300)
✅ Modo ahorro activado para la cámara 'camara-01'.

ABP2/
├── usuarios.json
├── dispositivos.json
├── main.py
├── gestion_usuarios.py
├── gestion_dispositivos.py
└── README.md


Evidencia 02
La parte escrita a desarrollar en esta evidencia esta compartida en el siguiente link:
https://docs.google.com/document/d/1r_k15PkXu85iLfIvJsa0PRM4s6fY_1bHJXTiBQJx2iw/edit?tab=t.jkky9ak6yo8aS
