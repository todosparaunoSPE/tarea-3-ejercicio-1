# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 12:24:10 2024

@author: jperezr
"""

import streamlit as st
import pandas as pd
from scipy import stats
from scipy.stats import t

# Datos de producción
data = {
    'Matutino': [22.42, 18.36, 21.46, 19.2, 23.4, 27.38, 23.46],
    'Vespertino': [23.51, 20.62, 26.47, 19.75, 20.3, 17.84, 26.34]
}

# Convertir los datos a un DataFrame
df = pd.DataFrame(data)

# Título de la aplicación
st.title('Comparación de Producción entre Turnos')

# Sección de ayuda
st.sidebar.header('Ayuda')
st.sidebar.write("""
**Descripción de la aplicación:**

Esta aplicación realiza una prueba t para muestras pareadas para comparar la producción de un filamento especial para lámparas incandescentes en dos turnos de trabajo: matutino y vespertino. La prueba se lleva a cabo para determinar si hay una diferencia significativa en la producción entre estos dos turnos.

**Enunciado del Ejercicio:**

Una planta fabricante de un filamento especial para lámparas incandescentes labora dos turnos de ocho horas (matutino y vespertino) con los niveles de producción en metros que se citan en la tabla a continuación:

| Matutino | Vespertino |
|----------|------------|
| 22.42    | 23.51      |
| 18.36    | 20.62      |
| 21.46    | 26.47      |
| 19.20    | 19.75      |
| 23.40    | 20.30      |
| 27.38    | 17.84      |
| 23.46    | 26.34      |

La gerencia de control de calidad está interesada en conocer si hay una diferencia en la producción entre turnos, por lo que propone efectuar un estudio comparativo simple con un nivel de confianza del 90%.

**Hipótesis:**

- **Hipótesis Nula (Ho):** No hay diferencia significativa en la producción media entre los turnos matutino y vespertino.
  
  \( H_0: \mu_{\text{matutino}} = \mu_{\text{vespertino}} \)

- **Hipótesis Alternativa (Ha):** Hay una diferencia significativa en la producción media entre los turnos matutino y vespertino.
  
  \( H_a: \mu_{\text{matutino}} \neq \mu_{\text{vespertino}} \)

**Método:**

1. Realizamos una prueba t para muestras pareadas.
2. Calculamos el valor crítico de t para un nivel de confianza del 90%.
3. Comparamos la estadística t calculada con el valor crítico para tomar una decisión sobre la hipótesis nula.
""")

# Mostrar los datos
st.write("**Datos de producción:**")
st.dataframe(df)

# Realizar la prueba t para muestras pareadas
t_statistic, p_value = stats.ttest_rel(df['Matutino'], df['Vespertino'])

# Calcular el valor crítico de t para un nivel de confianza del 90% (t(0.05, 6))
# Grados de libertad = n - 1 = 7 - 1 = 6
alpha = 0.10
df_libertad = len(df) - 1
t_critical = t.ppf(1 - alpha / 2, df_libertad)

# Mostrar los resultados
st.write("**Resultados de la Prueba t para muestras pareadas:**")
st.write(f"T-Statistic: {t_statistic:.4f}")
st.write(f"P-Value: {p_value:.4f}")
st.write(f"Valor crítico t(0.05, {df_libertad}): {t_critical:.4f}")

# Conclusión
if abs(t_statistic) > t_critical:
    st.write("**Conclusión:** Rechazamos la hipótesis nula. Existe evidencia suficiente para afirmar que hay una diferencia significativa en la producción entre los turnos matutino y vespertino.")
else:
    st.write("**Conclusión:** No se rechaza la hipótesis nula. No existe evidencia suficiente para afirmar que hay una diferencia significativa en la producción entre los turnos matutino y vespertino.")


st.sidebar.write("© 2024 Creado por: Javier Horacio Pérez Ricárdez")
