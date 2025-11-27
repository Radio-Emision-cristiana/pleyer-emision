import re

# Leer el archivo JavaScript original
with open('/workspace/user_input_files/main.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Eliminar la sección de ANIMACIÓN SIMPLE DEL VISUALIZADOR
js_content = re.sub(
    r'// ========================================\s*// ANIMACIÓN SIMPLE DEL VISUALIZADOR\s*// ========================================.*?console\.log\(\'✅ Visualizador desactivado\'\);[^}]*\}',
    '',
    js_content,
    flags=re.DOTALL
)

# Eliminar referencias a miniEqualizerContainer
js_content = re.sub(
    r'const miniEqualizerContainer = .*?;',
    '',
    js_content
)

# Eliminar llamadas a activateVisualizer() y deactivateVisualizer()
js_content = re.sub(r'\s*// Activar visualizador\s*activateVisualizer\(\);', '', js_content)
js_content = re.sub(r'\s*// Desactivar visualizador\s*deactivateVisualizer\(\);', '', js_content)
js_content = re.sub(r'\s*activateVisualizer\(\);', '', js_content)
js_content = re.sub(r'\s*deactivateVisualizer\(\);', '', js_content)

# Eliminar el test del visualizador en initPlayer
js_content = re.sub(
    r'// Test inmediato del visualizador.*?console\.log\(\'✅ Test del visualizador completado\'\);[^}]*\},\s*2000\);',
    '',
    js_content,
    flags=re.DOTALL
)

# Limpiar múltiples líneas en blanco
js_content = re.sub(r'\n\s*\n\s*\n+', '\n\n', js_content)

# Guardar el archivo JavaScript modificado
with open('/workspace/main_sin_visualizador.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Archivo JavaScript creado sin visualizadores")
