#!/usr/bin/env python3
"""
Script para eliminar el código del visualizador del CSS 
manteniendo intacto el mini-player
"""

def remove_visualizer_from_css(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    output_lines = []
    skip_mode = False
    bracket_count = 0
    in_equalizer_block = False
    in_mini_equalizer_block = False
    in_equalizer_keyframes = False
    in_fallback_keyframes = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Detectar inicio de bloques de visualizador
        if '/* Visualizador de ecualizador */' in line:
            skip_mode = True
            in_equalizer_block = True
            i += 1
            continue
        
        if '.equalizer-container {' in stripped or '.equalizer-bar {' in stripped:
            skip_mode = True
            in_equalizer_block = True
            bracket_count = 0
        
        if '/* Visualizador de espectro' in line or '.mini-equalizer-container {' in stripped:
            skip_mode = True
            in_mini_equalizer_block = True
            bracket_count = 0
        
        if '.mini-equalizer-bar' in stripped and '{' in stripped:
            skip_mode = True
            in_mini_equalizer_block = True
            if stripped.count('{') == stripped.count('}'):
                skip_mode = False
                in_mini_equalizer_block = False
                i += 1
                continue
            bracket_count = 0
        
        if 'body.dark-theme .mini-equalizer' in stripped:
            skip_mode = True
            in_mini_equalizer_block = True
            bracket_count = 0
        
        if '@keyframes equalize' in stripped:
            skip_mode = True
            in_equalizer_keyframes = True
            bracket_count = 0
        
        if '@keyframes fallbackEqualize' in stripped:
            skip_mode = True
            in_fallback_keyframes = True
            bracket_count = 0
        
        # Si estamos en modo skip, contar llaves
        if skip_mode:
            bracket_count += stripped.count('{')
            bracket_count -= stripped.count('}')
            
            # Salir del modo skip cuando las llaves se balanceen
            if bracket_count <= 0 and ('{' in stripped or '}' in stripped):
                skip_mode = False
                in_equalizer_block = False
                in_mini_equalizer_block = False
                in_equalizer_keyframes = False
                in_fallback_keyframes = False
                i += 1
                continue
            i += 1
            continue
        
        # Saltar líneas que contengan referencias al equalizer
        if any(keyword in line for keyword in [
            '.equalizer-container',
            '.equalizer-bar:nth-child',
            '.equalizer-bar {',
            '.mini-equalizer-container',
            '.mini-equalizer-bar',
            'body.dark-theme .equalizer',
            'body.dark-theme .mini-equalizer',
            '/* Modo oscuro para el visualizador',
            '/* Barras más delgadas en modo oscuro */',
            '/* Colores del espectro',
            '/* Repetir patrón de colores',
            '/* Patrón de espectro',
            '/* Animación fallback',
            '/* Patrón repetitivo para todas las barras',
            '/* Pausa la animación cuando no está'
        ]):
            # Si es una línea de comentario de visualizador
            if '/*' in line and '*/' not in line:
                # Saltar hasta encontrar el cierre del comentario
                i += 1
                while i < len(lines) and '*/' not in lines[i]:
                    i += 1
                i += 1
                continue
            i += 1
            continue
        
        # Mantener las líneas que no son del visualizador
        output_lines.append(line)
        i += 1
    
    # Escribir el archivo de salida
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)
    
    print(f"✓ CSS procesado: {len(lines)} líneas → {len(output_lines)} líneas")
    print(f"✓ Se eliminaron {len(lines) - len(output_lines)} líneas de visualizador")

if __name__ == "__main__":
    remove_visualizer_from_css(
        'user_input_files/styles.css',
        'styles_sin_visualizador.css'
    )
