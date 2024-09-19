#Miguel Rosas

# Verifica si se proporciona la cantidad_simulaciones como argumento
if [ $# -eq 0 ]; then
  echo "Uso: $0 cantidad_simulaciones"
  exit 1
fi

# Obtiene la cantidad_simulaciones desde el primer argumento
cantidad_simulaciones=$1

lc1=100
lc2=120
lc3=140
lc4=160
lc5=180
lc6=200
lc7=220
lc8=240

# Valores de Reynolds a utilizar
valores_lc=("lc1" "lc2" "lc3" "lc4" "lc5" "lc6" "lc7" "lc8")

# Leer valores desde el archivo parametros.txt
nu=$(grep -oP 'nu\s*=\s*\K[\d.+-]+' parametros.txt)
Ld=$(grep -oP 'Ld\s*=\s*\K[\d.+-]+' parametros.txt)
Re=$(grep -oP 'Re\s*=\s*\K[\d.+-]+' parametros.txt)
v=$(grep -oP 'v\s*=\s*\K[\d.+-]+' parametros.txt)

lcc=$(grep -oP 'lcc\s*=\s*\K[\d.+-]+' parametros.txt)
rd=$(grep -oP 'rd\s*=\s*\K[\d.+-]+' parametros.txt)
l1=$(grep -oP 'l1\s*=\s*\K[\d.+-]+' parametros.txt)
a=$(grep -oP 'a\s*=\s*\K[\d.+-]+' parametros.txt)
rp=$(grep -oP 'rp\s*=\s*\K[\d.+-]+' parametros.txt)
np=$(grep -oP 'np\s*=\s*\K[\d.+-]+' parametros.txt)

tf=$(grep -oP 'tf\s*=\s*\K[\d.+-]+' parametros.txt)
dt=$(grep -oP 'dt\s*=\s*\K[\d.+-]+' parametros.txt)
wi=$(grep -oP 'wi\s*=\s*\K[\d.+-]+' parametros.txt)

# Bucle para crear y mover carpetas, editar y genrar mallado
for ((i = 1; i <= $cantidad_simulaciones; i++)); do
  # Genera el nombre de la carpeta
  carpeta_caso_i="Case_$i"

  # Crea la carpeta del caso
  mkdir "$carpeta_caso_i"

  # Copia carpetas del caso dentro de las carpetasgeneradas
  cp -r "Case_0/0/" "$carpeta_caso_i/"
  cp -r "Case_0/constant/" "$carpeta_caso_i/"
  cp -r "Case_0/system/" "$carpeta_caso_i/"
  cp "Scripts/graficar_p1.py" "$carpeta_caso_i"
  cp "Scripts/graficar_p2.py" "$carpeta_caso_i"
  cp "Scripts/graficar_p3.py" "$carpeta_caso_i"
  cp "Scripts/graficar_p4.py" "$carpeta_caso_i"
  cp "Scripts/graficar_p5.py" "$carpeta_caso_i"
  cp "Scripts/extractor_p1.py" "$carpeta_caso_i"
  cp "Scripts/extractor_p2.py" "$carpeta_caso_i"
  cp "Scripts/extractor_p3.py" "$carpeta_caso_i"
  cp "Scripts/extractor_p4.py" "$carpeta_caso_i"
  cp "Scripts/extractor_p5.py" "$carpeta_caso_i"
  cp "Scripts/extractor_p1.sh" "$carpeta_caso_i"
  cp "Scripts/extractor_p2.sh" "$carpeta_caso_i"
  cp "Scripts/extractor_p3.sh" "$carpeta_caso_i"
  cp "Scripts/extractor_p4.sh" "$carpeta_caso_i"
  cp "Scripts/extractor_p5.sh" "$carpeta_caso_i"
  cp -r "./geometries/$carpeta_caso_i/triSurface" "$carpeta_caso_i/constant"
  ddir=$(pwd)
  sed -i "s|\$ddir|$ddir|g" "./$carpeta_caso_i/extractor_p1.py"
  sed -i "s|\$ddir|$ddir|g" "./$carpeta_caso_i/extractor_p2.py"
  sed -i "s|\$ddir|$ddir|g" "./$carpeta_caso_i/extractor_p3.py"
  sed -i "s|\$ddir|$ddir|g" "./$carpeta_caso_i/extractor_p4.py"
  sed -i "s|\$ddir|$ddir|g" "./$carpeta_caso_i/extractor_p5.py"
  sed -i "s|\$ddir|$ddir|g" "./$carpeta_caso_i/extractor_vel.py"
  cd "$carpeta_caso_i/"

  # Reemplazar valores en sus respectivos archivos
  sed -i "s/\$nuu/$nu/g" ./0/U
  sed -i "s/\$Ree/$Re/g" ./0/U
  sed -i "s/\$vv/$v/g" ./0/U
  sed -i "s/\$nuu/$nu/g" ./constant/transportProperties
  sed -i "s/\$LL/$Ld/g" ./0/U

  sed -i "s/\$rdd/$rd/g" ./mesh.geo
  sed -i "s/\$l11/$l1/g" ./mesh.geo
  sed -i "s/\$aa/$a/g" ./mesh.geo
  sed -i "s/\$lcccc/$lcc/g" ./mesh.geo

  sed -i "s/\$rdd/$rd/g" ./geometry_script/geometry.geo
  sed -i "s/\$l11/$l1/g" ./geometry_script/geometry.geo
  sed -i "s/\$aa/$a/g" ./geometry_script/geometry.geo
  sed -i "s/\$rpp/$rp/g" ./geometry_script/geometry.geo

  sed -i "s/\$npp/$np/g" ./geometry_script/generator_point_process.py
  sed -i "s/\$rpp/$rp/g" ./geometry_script/generator_point_process.py
  sed -i "s/\$rdd/$rd/g" ./geometry_script/generator_point_process.py

  sed -i "s/\$wii/$wi/g" ./system/controlDict
  sed -i "s/\$dtt/$dt/g" ./system/controlDict
  sed -i "s/\$tff/$tf/g" ./system/controlDict

  sed -i "s/\$ii/$i/g" ./extractor_p1.py
  sed -i "s/\$ii/$i/g" ./extractor_p2.py
  sed -i "s/\$ii/$i/g" ./extractor_p3.py
  sed -i "s/\$ii/$i/g" ./extractor_p4.py
  sed -i "s/\$ii/$i/g" ./extractor_p5.py
  sed -i "s/\$aa/$a/g" ./extractor_p1.py
  sed -i "s/\$aa/$a/g" ./extractor_p2.py
  sed -i "s/\$aa/$a/g" ./extractor_p3.py
  sed -i "s/\$aa/$a/g" ./extractor_p4.py
  sed -i "s/\$aa/$a/g" ./extractor_p5.py
  sed -i "s/\$rdd/$rd/g" ./extractor_p1.py
  sed -i "s/\$rdd/$rd/g" ./extractor_p2.py
  sed -i "s/\$rdd/$rd/g" ./extractor_p3.py
  sed -i "s/\$rdd/$rd/g" ./extractor_p4.py
  sed -i "s/\$rdd/$rd/g" ./extractor_p5.py

  mkdir Case_0
  mv 0/ Case_0/
  mv constant/ Case_0/
  mv system/ Case_0/
  mv geometry_script/ Case_0/
  mv mesh.geo Case_0/
  mv mesh.msh Case_0/

  # Se inicia el ciclo para variar el valor de lc
  for j in {0..7}; do
    #se genera contador k
    k=$((j + 1))

    # se crea carpeta del caso para el valor de Reynolds
    carpeta_lc="Case_${i}_${valores_lc[$j]}"
    mkdir "$carpeta_lc"

    #se copian los archivos a la carpeta del caso
    cp -r Case_0/0/ "$carpeta_lc/"
    cp -r Case_0/constant/ "$carpeta_lc/"
    cp -r Case_0/system/ "$carpeta_lc/"

    #Se reemplaza el valor de lc en el archivo 0/U
    sed -i "s/\$lcc/${!valores_lc[$j]}/g" "$carpeta_lc/system/blockMeshDict"
    sed -i "s/\$rdd/$rd/g" "$carpeta_lc/system/blockMeshDict"
    sed -i "s/\$aa/$a/g" "$carpeta_lc/system/blockMeshDict"
    sed -i "s/\$l11/$l1/g" "$carpeta_lc/system/blockMeshDict"

    cd "$carpeta_lc/"
    touch "${valores_lc[$j]}.foam"

    surfaceFeatureExtract
    blockMesh
    snappyHexMesh -overwrite

    decomposePar
    mpirun -np 6 simpleFoam -parallel >log
    cd ..
  done
  kitty --hold -e bash -c "./extractor_p1.sh && ./extractor_p2.sh && ./extractor_p3.sh && ./extractor_p4.sh && ./extractor_p5.sh ; exec bash" &
  cd ..
done

echo "Proceso completado."
