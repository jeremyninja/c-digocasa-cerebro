# Data System — Mujer & Finanzas (estudio complementario)

Estudio cualitativo + cuantitativo sobre **mujer dominicana y finanzas** que complementa el pilar 11 (Mujer) del estudio Código Casa.

**Foco temático:**
- Sueños, aspiraciones, proyecto de vida de la mujer dominicana
- Sentimientos y motivaciones frente al dinero
- Patrones de consumo
- Manejo financiero (ahorro, gasto, deuda, inversión, emprendimiento)
- Rol económico en el hogar

---

## ⚠ EXCLUSIÓN CRÍTICA — Banreservas

**Este estudio fue comissioned por Banreservas. Cualquier pregunta, columna, ítem o verbatim que mencione "Banreservas" o evalúe explícitamente productos/servicios del banco NO se puede usar en hallazgos de Código Casa.**

El cazador debe:
1. Antes de citar una cifra: verificar que la pregunta NO mencione "Banreservas" en su enunciado o ítems
2. Antes de citar un verbatim: verificar que la cita NO sea respuesta a una dinámica de Banreservas (ejemplo: "¿qué productos de Banreservas usas?")
3. Si una cifra/verbatim tiene contexto Banreservas, descartarlo y reportarlo en el log de exclusiones del hallazgo

Las cifras y verbatims SI usables son los que hablan de:
- Conducta general (no en relación al banco)
- Aspiraciones financieras (genérico)
- Sentimientos sobre el dinero (genérico)
- Hábitos de ahorro/consumo (genérico)
- Rol en el hogar (genérico)

---

## Estructura de archivos

### `bbdd/` — Bases de datos cuanti

- `BBDD Mujer y finanzas.xlsx` — base madre del estudio cuantitativo (328 KB). Probablemente contiene tabulaciones n=X mujeres dominicanas. **Verificar n total al usar.**
- `Familias Dominicanas por mujer.xlsx` — cross-tabs específicos por tipología de familia
- `Mujer y finanzas.xlsx` — derivado/resumen

**Para usar:** el cazador abre con `openpyxl` o `pandas`, identifica las preguntas no-Banreservas, y cita cifras con base.

### `transcripciones-fw/` — 8 focus groups

Convertidos de .docx a .txt para lectura plana. Cada FG corresponde a un perfil:

| Archivo | Perfil |
|---|---|
| `Grupo-1-MASIVO_JO_VENES.txt` | Masivo / Jóvenes |
| `Grupo-2-MASIVO_JEFAS_DEL_HOGAR.txt` | Masivo / Jefas de hogar |
| `Grupo-3-Masivo-Perfil_Li_deres_2.txt` | Masivo / Roles de liderazgo |
| `Grupo-4-Masivo-Emprendedoras.txt` | Masivo / Emprendedoras |
| `Grupo-5-Preferente-Jefas_de_hogar.txt` | Preferente / Jefas de hogar |
| `Grupo-6-Preferente-Roles_de_Liderazgo.txt` | Preferente / Roles de liderazgo |
| `Grupo-7-Preferente-Emprendedoras.txt` | Preferente / Emprendedoras |
| `Grupo-8-Preferente-Jo_venes.txt` | Preferente / Jóvenes |

**Segmentación:** Masivo = NSE C/D · Preferente = NSE AB/C+ (terminología bancaria dominicana).

**Cuando citar un verbatim, usar el formato:** `(FW · Grupo N · Perfil)` — ejemplo: `(FW · Grupo 2 · Masivo Jefas de Hogar)`.

---

## Cómo se integran estos hallazgos con el pilar Mujer de Código Casa

El cazador debe entregar el set unificado de Pilar Mujer con TODAS las fuentes:

1. **Código Casa (cuanti):** `Data System/derivados-por-pilar/11-mujer.md` — n=305 mujeres
2. **Código Casa (FG):** `Data System/derivados-por-pilar/transcripciones-codigo-casa/fg-03, fg-07, fg-08, fg-09, fg-11`
3. **Finance Women (cuanti):** `Data System Mujer Finanzas/bbdd/*.xlsx` — n por confirmar al abrir el archivo
4. **Finance Women (cuali):** `Data System Mujer Finanzas/transcripciones-fw/*.txt` — 8 FGs

**Cada hallazgo cita su fuente:**
- Cifra de Código Casa: `Q053 · BBDD P1 · Mujeres n=305 · CC`
- Cifra de Finance Women: `P12 · BBDD Mujer y finanzas · Mujeres n=?? · FW`
- Verbatim CC: `(fg-07 · Biparental hijos pequeños)`
- Verbatim FW: `(FW · Grupo 4 · Masivo Emprendedoras)`

**No mezclar bases en un mismo número.** Si tienes una cifra de CC y otra de FW, se reportan separadas, no se promedian.
