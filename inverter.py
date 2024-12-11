import pandas as pd

def invertir_signo_columnas_y(file_path, output_path):
    # Leer el archivo completo para conservar encabezados
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Encontrar la línea donde comienzan los datos de columnas (con Frame#)
    data_start = next(i for i, line in enumerate(lines) if line.startswith('Frame#'))
    header = lines[:data_start + 2]  # Encabezados y metadatos
    header_line = lines[data_start + 1]  # Línea con los nombres de las columnas
    
    # Crear DataFrame desde los datos
    column_names = header_line.strip().split('\t')
    data = pd.read_csv(file_path, sep='\t', skiprows=data_start + 2, names=column_names)
    
    # Identificar y modificar columnas que contienen "Y"
    y_columns = [col for col in data.columns if "Y" in col]
    for col in y_columns:
        data[col] *= -1  # Invertir el signo de los valores
    
    # Guardar el archivo con el encabezado original
    with open(output_path, 'w') as f:
        f.writelines(header)  # Escribir encabezado original
        data.to_csv(f, sep='\t', index=False, header=False)  # Escribir datos sin nombres de columnas
    
    return output_path

# Ejemplo de uso
file_path = '/ruta/a/tu/archivo/P19.trc'  # Cambiar por la ruta del archivo original
output_file_path = '/ruta/a/tu/archivo/P19_invertido.trc'  # Cambiar por la ruta del archivo modificado
invertir_signo_columnas_y(file_path, output_file_path)
