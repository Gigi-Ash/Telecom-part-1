# 📊 Proyecto de Análisis: Churn Telecom X

Este repo contiene mi solución para el Challenge de Telecom X. El objetivo principal es entender por qué los clientes se están llendo de la conpañia y qué factores influyen en esa decisión.

## 🛠️ Herramientas Usadas
* **Python** (Lenguaje base)
* **Pandas** (Para toda la parte de manipulación de datos)
* **Matplotlib y Seaborn** (Para hacer las gráficas y que se entienda el análisis)

## 📈 Lo que se hiso en el proyecto
Para que los datos sirvieran para el análisis, se siguieron estos pasos:

1. **Carga de Datos:** Se importaron desde un JSON y se "aplanaron" para que cada información tuviera su propia columna (usando `json_normalize`).
2. **Limpesa de Inconsistencias:** Se corrigieron los formatos de los cargos totales que venian como texto y se quitaron las filas que no tenian información completa.
3. **Cálculo de Cuentas Diarias:** Se creó una nueva métrica para saver cuánto paga un cliente por día.
4. **Análisis Visual:** Se crearon gráficas de barras y cajas para comparar la evasión contra el tipo de contrato y los costos mensuales.

## 💡 Concluciones rápidas
* Los clientes con **contratos mensuales** son los que más rápido abandonan la empresa.
* Hay un punto crítico cuando la **mensualidad pasa de los $70**, donde la gente empieza a buscar otras opciones.
* La **antigüedad** es clave: los clientes que pasan el primer año suelen ser mucho más leales.

---
*Nota: Este proyecto fue realizado como parte de mi formación en análisis de datos y mecatrónica (UPIITA).*
