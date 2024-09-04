"""import cv2

def verificar_indices_camara(max_indices=10):
    for i in range(max_indices):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Cámara encontrada en el índice: {i}")
            cap.release()
        else:
            print(f"No se puede abrir la cámara en el índice: {i}")

# Verificar los primeros 10 índices de cámara
verificar_indices_camara(10)"""
try:
    from pymodbus.client import ModbusTcpClient
    print("pymodbus se ha importado correctamente.")
except ModuleNotFoundError:
    print("pymodbus no se ha encontrado.")