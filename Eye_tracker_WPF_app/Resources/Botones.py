import pyttsx3
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
# Función init para obtener una instancia de motor para la síntesis de voz.
engine = pyttsx3.init()

while True:
    print("Esperando recibir mensaje")
    message = socket.recv_string()
    print(f"Recibido: {message}")

    if message == "Cerrar": 
        socket.send_string("Cerrado con exito")
        socket.close()
        break

    # selecciona el mensaje que se va a reproducir
    engine.say(message)

    # Método de ejecución y espera, procesa los comandos de voz.
    engine.runAndWait()

    # Procesar la solicitud
    response = f"Respuesta desde Python: Hola, recibí '{message}'"

    socket.send_string(response)

print("Servidor cerrado")