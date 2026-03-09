import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. Extraccion de datos ---
# Usamos la url directa para no tener problemas de logeo
url = 'https://raw.githubusercontent.com/ingridcristh/challenge2-data-science-LATAM/main/TelecomX_Data.json'

r = requests.get(url)
datos_json = r.json()

# Aplanamos el json para que sea un dataframe manipulable
df = pd.json_normalize(datos_json)

print(f"Datos cargados: {df.shape[0]} filas y {df.shape[1]} columnas.")

# --- 2. Limpesa y Tratamiento (Paso critico) ---
# Convertimos cargos totales a numerico pq a veses vienen como texto vacio
df['account.Charges.Total'] = pd.to_numeric(df['account.Charges.Total'], errors='coerce')

# Borramos los nulos que quedaron despues de la conversion
df = df.dropna(subset=['account.Charges.Total'])
df = df[df['Churn'].str.strip() != '']

# Creamos la columna de Cuentas Diarias que pide el challange
# Formula: $Cuentas\_Diarias = \frac{Mensualidad}{30}$
df['Cuentas_Diarias'] = df['account.Charges.Monthly'] / 30

# Renombrando columnas para que sea mas facil el analisis
nombres_hispanos = {
    'customer.gender': 'Genero',
    'customer.SeniorCitizen': 'Adulto_Mayor',
    'customer.tenure': 'Meses_Contrato',
    'account.Charges.Monthly': 'Mensualidad',
    'account.Charges.Total': 'Total_Pagado',
    'account.Contract': 'Tipo_Contrato',
    'Churn': 'Evasion'
}
df = df.rename(columns=nombres_hispanos)

# --- 3. Graficas y Visualisacion ---
plt.figure(figsize=(15, 6))

# Grafica 1: Cuantos se van
plt.subplot(1, 3, 1)
sns.countplot(data=df, x='Evasion', hue='Evasion', palette='magma', legend=False)
plt.title('Distribusion de Evasion (Churn)')
plt.xlabel('¿Se fue el cliente?')
plt.ylabel('Cantidad de Personas')

# Grafica 2: Evasion por tipo de contrato
plt.subplot(1, 3, 2)
sns.countplot(data=df, x='Tipo_Contrato', hue='Evasion', palette='viridis')
plt.title('Evasion segun el Contrato')
plt.xticks(rotation=45)
plt.xlabel('Tipo de Contrato')

# Grafica 3: Mensualidad vs Evasion
plt.subplot(1, 3, 3)
sns.boxplot(data=df, x='Evasion', y='Mensualidad', palette='coolwarm')
plt.title('Mensualidad vs Churn')
plt.ylabel('Costo Mensual')

plt.tight_layout()
plt.show()

# Resumen estadistico final
print("Analisis descriptivo proccesado:")
print(df[['Meses_Contrato', 'Mensualidad', 'Total_Pagado', 'Cuentas_Diarias']].describe())