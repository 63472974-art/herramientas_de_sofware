print("=== REGISTRO DE ESTUDIANTE ===")

# Solicitar datos
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
carrera = input("Ingrese su carrera: ")
semestre = int(input("Ingrese su semestre: "))

# Estado de matricula
matriculado = True

#solicitar la primera nota
nota1 = float(input("ingrsa la nota 1:"))
while nota1 < 0 or nota1 > 20:
    print("la nota debe estar entre 0 y 20")
    nota1 = float(input("ingrsa la nota 1:"))
 
 #solicitar la segunda nota   
nota2 = float(input("ingrsa la nota 2:"))
while nota2 < 0 or nota2> 20:
    print("la nota debe estar entre 0 y 20")
    nota2 = float(input("ingrsa la nota 2:"))
 
 #solicitar la tercera nota   
nota3 = float(input("ingrsa la nota 3:"))
while nota3 < 0 or nota3> 20:
    print("la nota debe estar entre 0 y 20")
    nota3 = float(input("ingrsa la nota 3:")) 
      
#creamos una lista de notas 
notas =[nota1, nota2, nota3]

#acumuladores y contadores
suma = 0
aprobada = 0
desaprobadas = 0

#procesar notas 
for nota in notas:
    #sumando nota1 + nota2 + nota3
    suma = suma + nota
    if nota >=13:
        aprobada = aprobada + 1
    else:
        desaprobadas = desaprobadas + 1
        
#calcular promedio
promedio = suma / len(notas)

#clasificar al estudiante 
if promedio >= 17:
    estado = "puede acceder a la beca en URUSAYUA"
else:
    estado = "tiene que pagar la matricula completa"
    
# Cursos
cursos = [
    "Herramientas de Desarrollo de Software",
    "Base de Datos",
    "Redes"
]

# Mostrar datos
print("\n=== RESULTADO ACADEMICO ===")
print("Nombre:", nombre)
print("Edad:", edad)
print("Carrera:", carrera)
print("Semestre:", semestre)

print("\nNotas:")

for i in range(len(notas)):
    print("nota", 1+1, ":", notas[i])
    
print("\nPromedio:", round(promedio,2))
print("notas aprobadas:", aprobada)
print("notas desaprobadas:", desaprobadas)
print("estado: ", estado)
    
  

    