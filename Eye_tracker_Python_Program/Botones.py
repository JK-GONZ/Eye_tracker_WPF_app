# Import the required module for text 
# to speech conversion
import pyttsx3
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()

while True:
    print("Esperando recibir mensaje")
    message = socket.recv_string()
    print(f"Recibido: {message}")

    if message == "Cerrar": 
        socket.send_string("Cerrado con exito")
        socket.close()
        break

    # say method on the engine that passing input text to be spoken
    engine.say(message)

    # run and wait method, it processes the voice commands.
    engine.runAndWait()

    # Procesar la solicitud (aquí puedes incluir cualquier lógica adicional)
    response = f"Respuesta desde Python: Hola, recibí '{message}'"
    

    socket.send_string(response)

print("Servidor cerrado")