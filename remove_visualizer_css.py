import re

# Leer el archivo CSS original
with open('/workspace/user_input_files/styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Patrones a eliminar
patterns_to_remove = [
    # Visualizador de ecualizador completo
    r'/\* Visualizador de ecualizador \*/.*?\.equalizer-bar \{[^}]+\}',
    # Todas las reglas .equalizer-bar:nth-child
    r'\.equalizer-bar:nth-child\(\d+\) \{[^}]+\}',
    # Visualizador de espectro de colores
    r'/\* Visualizador de espectro de colores \*/.*?\.mini-equalizer-bar \{[^}]+\}',
    # Todas las reglas .mini-equalizer-bar:nth-child
    r'\.mini-equalizer-bar:nth-child\([^)]+\) \{[^}]+\}',
    # Patrón repetitivo para barras
    r'/\* Patrón repetitivo para.*?\*/',
    # Reglas adicionales mini-equalizer
    r'body\.dark-theme \.mini-equalizer-container \{[^}]+\}',
    r'body\.dark-theme \.mini-equalizer-bar \{[^}]+\}',
    # Animaciones relacionadas
    r'@keyframes equalize \{[^}]+\}',
    r'@keyframes fallbackEqualize \{[^}]+\}',
    # Pausa la animación
    r'/\* Pausa la animación cuando no está reproduciéndose \*/\s*\.equalizer-container\.paused \.equalizer-bar \{[^}]+\}',
    r'\.mini-equalizer-container\.paused \.mini-equalizer-bar \{[^}]+\}',
    # Secciones completas en media queries para equalizer
    r'\.equalizer-container \{[^}]+\}',
    r'\.equalizer-bar \{[^}]+\}',
    r'\.mini-equalizer-container \{[^}]+\}',
    r'\.mini-equalizer-bar \{[^}]+\}',
]

# Aplicar cada patrón
for pattern in patterns_to_remove:
    css_content = re.sub(pattern, '', css_content, flags=re.DOTALL | re.MULTILINE)

# Limpiar múltiples líneas en blanco consecutivas
css_content = re.sub(r'\n\s*\n\s*\n+', '\n\n', css_content)

# Guardar el archivo CSS modificado
with open('/workspace/styles_sin_visualizador.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Archivo CSS creado sin visualizadores")
