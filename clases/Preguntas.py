import Funciones as f
from tkinter.messagebox import *
class Preguntas:
    def __init__(self) -> None:
        pass
    
    def preguntas(opc): 
        if opc == "pantallaazul":
            f.array.clear()#Limpió la última ejecución
            answer = askyesno(title='Responda la pregunta',message='¿Presenta pantallazos azules?')
            if answer:
                Preguntas.preguntas(str(f.QuestionOrFactSi("pantallaazul")))
            else:
                Preguntas.preguntas(str(f.QuestionOrFactNo("pantallaazul")))
        if opc == "pitidolargo":
            f.array.clear()#Limpió la última ejecución
            answer = askyesno(title='Responda la pregunta',message='¿Al iniciar el equipo emite un pitido largo?')
            if answer:
                Preguntas.preguntas(str(f.QuestionOrFactSi("pitidolargo")))
                f.fondoF("ram") 
            else:
                Preguntas.preguntas(str(f.QuestionOrFactNo("pitidolargo")))       
        if opc == "pitidocorto":
            f.array.clear()#Limpió la última ejecución
            answer = askyesno(title='Responda la pregunta',message='¿Al iniciar el equipo emite pitidos cortos?')
            if answer:
                Preguntas.preguntas(str(f.QuestionOrFactSi("pitidocorto")))
                f.fondoF("grafica")  
            else:
                Preguntas.preguntas(str(f.QuestionOrFactNo("pitidocorto")))
                f.fondoF("tecnico")
        if opc == "sobrecalentamiento":
            f.array.clear()#Limpió la última ejecución
            answer = askyesno(title='Responda la pregunta',message='¿Tiene problemas de sobrecalentamiento?')
            if answer:
                Preguntas.preguntas(str(f.QuestionOrFactSi("sobrecalentamiento")))
            else:
                Preguntas.preguntas(str(f.QuestionOrFactNo("sobrecalentamiento")))
        if opc == "temperaturacpualta":
            f.array.clear()#Limpió la última ejecución
            answer = askyesno(title='Responda la pregunta',message='¿La temperatura del procesador es alta?')
            if answer:
                Preguntas.preguntas(str(f.QuestionOrFactSi("temperaturacpualta")))
            else:
                Preguntas.preguntas(str(f.QuestionOrFactNo("temperaturacpualta")))    
        if opc == "mensajeserror":
            f.array.clear()#Limpió la última ejecución
            answer = askyesno(title='Responda la pregunta',message='¿Manada mensajes de error?')
            if answer:
                Preguntas.preguntas(str(f.QuestionOrFactSi("mensajeserror")))
                f.fondoF("problemascpu")
            else:
                Preguntas.preguntas(str(f.QuestionOrFactNo("mensajeserror")))
        if opc == "sedetiene":
            f.array.clear()#Limpió la última ejecución
            answer = askyesno(title='Responda la pregunta',message='¿Se detiene de manera inesperada?')
            if answer:
                Preguntas.preguntas(str(f.QuestionOrFactSi("sedetiene")))
                f.fondoF("problemascpu")
            else:
                Preguntas.preguntas(str(f.QuestionOrFactNo("sedetiene")))  
        if opc == "enciende":
            f.array.clear()#Limpió la última ejecución
            answer = askyesno(title='Responda la pregunta',message='¿El equipo enciende?')
            if answer:
                Preguntas.preguntas(str(f.QuestionOrFactSi("enciende")))
                f.fondoF("cortocircuito")
            else:
                Preguntas.preguntas(str(f.QuestionOrFactNo("enciende")))
                f.fondoF("fuentedepoder")  
        if opc == "mantenimiento":
            f.array.clear()#Limpió la última ejecución
            answer = askyesno(title='Responda la pregunta',message='¿Ha realizado algún mantenimiento al equipo enlos últimos 6 meses?')
            if answer:
                Preguntas.preguntas(str(f.QuestionOrFactSi("mantenimiento")))
                f.fondoF("tecnico")
            else:
                Preguntas.preguntas(str(f.QuestionOrFactNo("mantenimiento")))
                f.fondoF("suciedadypolvo")  
        if opc == "reinicioscontinuos":
            f.array.clear()#Limpió la última ejecución
            answer = askyesno(title='Responda la pregunta',message='¿Ha experimentado reinicios continuos?')
            if answer:
                Preguntas.preguntas(str(f.QuestionOrFactSi("reinicioscontinuos")))
                f.fondoF("driversysoftware")
            else:
                Preguntas.preguntas(str(f.QuestionOrFactNo("reinicioscontinuos")))
                f.fondoF("tecnico")  
        