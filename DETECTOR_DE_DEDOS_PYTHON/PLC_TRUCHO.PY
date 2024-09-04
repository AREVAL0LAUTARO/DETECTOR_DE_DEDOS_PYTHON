"""# Importar las bibliotecas necesarias
from pymodbus.client.sync import ModbusTcpClient

# Simular la conexión al "PLC" (simulado)
PLC = ModbusTcpClient("127.0.0.1")  # Cambia la IP por la dirección de tu simulador
if not PLC.connect():
    print("Error al conectar con el PLC simulado.")
    exit()

# Simular la escritura en bobinas
deteccion_simulada = [True, False, True, False]  # Ejemplo de datos simulados
PLC.write_coils(1, deteccion_simulada)

# Cerrar la conexión
PLC.close()

print("Datos simulados escritos en el PLC.")"""
from pymodbus.client.sync import ModbusTcpClient