import os
from pathlib import Path

def mostrar_estructura_directorios(ruta, nivel_maximo=None, mostrar_ocultos=False):
    """
    Muestra la estructura de carpetas, subcarpetas y archivos de una ubicación
    
    Args:
        ruta (str): Ruta a explorar
        nivel_maximo (int, optional): Profundidad máxima de recursión. None para sin límite.
        mostrar_ocultos (bool): Si incluir archivos/carpetas ocultos (que comienzan con . o _)
    """
    try:
        # Validar y normalizar la ruta
        ruta_base = Path(ruta).expanduser().resolve()
        if not ruta_base.exists():
            print(f"❌ La ruta no existe: {ruta_base}")
            return
        
        print(f"\n📁 Estructura de directorios para: {ruta_base}\n")
        
        # Recorrer el árbol de directorios
        for raiz, dirs, archivos in os.walk(ruta_base):
            # Calcular nivel de profundidad
            nivel = raiz.replace(str(ruta_base), '').count(os.sep)
            
            # Aplicar filtro de nivel máximo
            if nivel_maximo is not None and nivel > nivel_maximo:
                continue
                
            # Filtrar carpetas ocultas si es necesario
            if not mostrar_ocultos:
                dirs[:] = [d for d in dirs if not d.startswith(('.', '_'))]
                archivos = [f for f in archivos if not f.startswith(('.', '_'))]
            
            # Mostrar carpeta actual
            indentacion = '    ' * nivel
            print(f"{indentacion}├── {os.path.basename(raiz)}/")
            
            # Mostrar archivos en la carpeta actual
            for archivo in archivos:
                print(f"{indentacion}│   ├── {archivo}")
    
    except PermissionError:
        print(f"⚠️ No tienes permisos para acceder a: {ruta_base}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Muestra la estructura de carpetas y archivos de una ubicación"
    )
    parser.add_argument(
        'ruta',
        nargs='?',
        default='.',
        help='Ruta a explorar (por defecto: directorio actual)'
    )
    parser.add_argument(
        '-l', '--nivel',
        type=int,
        help='Nivel máximo de profundidad a mostrar'
    )
    parser.add_argument(
        '-o', '--ocultos',
        action='store_true',
        help='Mostrar archivos y carpetas ocultas'
    )
    
    args = parser.parse_args()
    
    mostrar_estructura_directorios(
        ruta=args.ruta,
        nivel_maximo=args.nivel,
        mostrar_ocultos=args.ocultos
    )

if __name__ == "__main__":
    main()