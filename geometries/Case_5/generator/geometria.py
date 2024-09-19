import FreeCAD as App
import Part
import Mesh
import MeshPart  # Importar MeshPart para convertir sólidos a mallas
import csv

# Crear un nuevo documento en FreeCAD
doc = App.newDocument()

# Definir las dimensiones del cilindro principal
radio_principal = 0.0145  # Radio del cilindro en m
altura_principal = 0.435  # Altura del cilindro en m

# Crear el cilindro principal
cilindro_principal = Part.makeCylinder(radio_principal, altura_principal)

# Añadir el cilindro principal al documento
Part.show(cilindro_principal)

# Definir las dimensiones de los cilindros pequeños
radio_pequeno = 0.0025  # Radio de los cilindros pequeños en mm
altura_pequeno = 0.003  # Altura de los cilindros pequeños en mm

# Leer el archivo CSV y crear los cilindros pequeños
csv_path = "puntos.csv"  # Ruta al archivo CSV
with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        x, y = float(row[0]), float(row[1])
        # Crear el cilindro pequeño
        cilindro_pequeno = Part.makeCylinder(
            radio_pequeno, altura_pequeno, App.Vector(x, y, altura_principal)
        )
        # Añadir el cilindro pequeño al documento
        Part.show(cilindro_pequeno)

# Crear el segundo cilindro principal, posicionado después de los cilindros pequeños
desplazamiento_z = altura_principal + altura_pequeno  # Desplazamiento en Z

segundo_cilindro = Part.makeCylinder(
    radio_principal, altura_principal, App.Vector(0, 0, desplazamiento_z)
)
Part.show(segundo_cilindro)

# Convertir los objetos sólidos a mallas antes de la exportación
mesh_cilindro_principal = MeshPart.meshFromShape(
    Shape=cilindro_principal, LinearDeflection=0.01, AngularDeflection=0.1
)
mesh_cilindro_secundario = MeshPart.meshFromShape(
    Shape=segundo_cilindro, LinearDeflection=0.01, AngularDeflection=0.1
)

# Crear objetos de malla en el documento
mesh_obj_principal = doc.addObject("Mesh::Feature", "MeshPrincipal")
mesh_obj_principal.Mesh = mesh_cilindro_principal

mesh_obj_secundario = doc.addObject("Mesh::Feature", "MeshSecundario")
mesh_obj_secundario.Mesh = mesh_cilindro_secundario

# Exportar los objetos malla a un archivo STL
export_stl_path = (
    "geometria.stl"  # Cambia esta ruta a donde quieras guardar el archivo STL
)
Mesh.export([mesh_obj_principal, mesh_obj_secundario], export_stl_path)

# Guardar el archivo como STEP
export_step_path = (
    "geometria.step"  # Cambia esta ruta a donde quieras guardar el archivo STEP
)
doc.saveAs(export_step_path)

# Exportar el conjunto a un archivo STEP
Part.export(doc.Objects, export_step_path)

# Cerrar el documento
App.closeDocument(doc.Name)

print(
    f"Cilindro con pequeños cilindros y segundo cilindro exportado como STEP en {export_step_path} y STL en {export_stl_path}"
)
