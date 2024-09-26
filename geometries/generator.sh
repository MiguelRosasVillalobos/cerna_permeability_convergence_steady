#Miguel Rosas

# Verifica si se proporciona la cantidad_simulaciones como argumento
if [ $# -eq 0 ]; then
  echo "Uso: $0 cantidad_simulaciones"
  exit 1
fi

# Obtiene la cantidad_simulaciones desde el primer argumento
cantidad_simulaciones=$1

# Leer valores desde el archivo parametros.txt
rd=$(grep -oP 'rd\s*=\s*\K[\d.+-]+' ../parametros.txt)
a=$(grep -oP 'a\s*=\s*\K[\d.+-]+' ../parametros.txt)
rp=$(grep -oP 'rp\s*=\s*\K[\d.+-]+' ../parametros.txt)
np=$(grep -oP 'np\s*=\s*\K[\d.+-]+' ../parametros.txt)
l1=$(grep -oP 'l1\s*=\s*\K[\d.+-]+' ../parametros.txt)
a=$(grep -oP 'a\s*=\s*\K[\d.+-]+' ../parametros.txt)

# Bucle para crear y mover carpetas, editar y genrar mallado
for ((i = 1; i <= $cantidad_simulaciones; i++)); do
  # Genera el nombre de la carpeta
  carpeta_caso_i="Case_$i"

  # Crea la carpeta del caso
  mkdir "$carpeta_caso_i"

  # Copia carpetas del caso dentro de las carpetasgeneradas
  cp -r "generator/" "$carpeta_caso_i/"
  cd "$carpeta_caso_i/"

  # Reemplazar valores en sus respectivos archivos
  sed -i "s/\$npp/$np/g" generator/generator_point_process.py
  sed -i "s/\$rpp/$rp/g" generator/generator_point_process.py
  sed -i "s/\$rdd/$rd/g" generator/generator_point_process.py
  sed -i "s/\$rdd/$rd/g" generator/geometria.py
  sed -i "s/\$l11/$l1/g" generator/geometria.py
  sed -i "s/\$rpp/$rp/g" generator/geometria.py
  sed -i "s/\$aa/$a/g" generator/geometria.py

  #Generar mallado gmsh
  touch puntos.csv
  mkdir triSurface
  python3 generator/generator_point_process.py
  freecadcmd ./generator/geometria.py
  rm geometria.step.FCStd
  rm geometria.stl
  cd ../
done

echo "Proceso completado."
