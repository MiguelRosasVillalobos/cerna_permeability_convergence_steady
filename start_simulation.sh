#Miguel Rosas

# Verifica si se proporciona la cantidad_simulaciones como argumento
if [ $# -eq 0 ]; then
	echo "Uso: $0 cantidad_simulaciones"
	exit 1
fi

# Obtiene la cantidad_simulaciones desde el primer argumento
cantidad_simulaciones=$1

lc1=0.012
lc2=0.011
lc3=0.01
lc4=0.009
lc5=0.008
lc6=0.006
lc7=0.003
lc8=0.001

# Valores de Reynolds a utilizar
valores_lc=("lc1" "lc2" "lc3" "lc4" "lc5" "lc6" "lc7" "lc8")

# Leer valores desde el archivo parametros.txt
nu=$(grep -oP 'nu\s*=\s*\K[\d.+-]+' parametros.txt)
Ld=$(grep -oP 'Ld\s*=\s*\K[\d.+-]+' parametros.txt)
Re=$(grep -oP 'Re\s*=\s*\K[\d.+-]+' parametros.txt)

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
	cp -r "Case_0/geometry_script/" "$carpeta_caso_i/"
	cp "Case_0/mesh.geo" "$carpeta_caso_i/"
	cp "Case_0/deltap_extract.py" "$carpeta_caso_i/"

	cd "$carpeta_caso_i/"

	# Reemplazar valores en sus respectivos archivos
	sed -i "s/\$nuu/$nu/g" ./0/U
	sed -i "s/\$Ree/$Re/g" ./0/U
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

	mkdir Case_0
	mv 0/ Case_0/
	mv constant/ Case_0/
	mv system/ Case_0/
	mv geometry_script/ Case_0/
	mv mesh.geo Case_0/
	mv mesh.msh Case_0/
	mv deltap_extract.py Case_0/

	# Se inicia el cilclo para variar el valor de Reynolds
	for j in {0..7}; do
		#se genera contador k
		k=$((j + 1))

		# se crea carpeta del caso para el valor de Reynolds
		mkdir Case_${i}_${valores_lc[$j]}

		#se copian los archivops a la carpeta del caso
		cp -r Case_0/0/ Case_${i}_${valores_lc[$j]}/
		cp -r Case_0/constant/ Case_${i}_${valores_lc[$j]}/
		cp -r Case_0/system/ Case_${i}_${valores_lc[$j]}/
		cp -r Case_0/geometry_script/ Case_${i}_${valores_lc[$j]}/
		cp Case_0/mesh.geo Case_${i}_${valores_lc[$j]}/

		#Se reemplaza el valor de lc en el archivo 0/U
		sed -i "s/\$lccc/${!valores_lc[$j]}/g" Case_${i}_${valores_lc[$j]}/mesh.geo
		sed -i "s/\$lccc/${!valores_lc[$j]}/g" Case_${i}_${valores_lc[$j]}/geometry_script/geometry.geo

		cd Case_${i}_${valores_lc[$j]}/

		cd "./geometry_script/"

		#Generar mallado gmsh
		python3 generator_point_process.py
		./generate.sh
		cd ..
		gmsh "./mesh.geo" -3

		#Genera mallado OpenFoam
		gmshToFoam "mesh.msh"

		# Utiliza grep para eliminar las líneas que contienen la palabra "physicalType" y sobrescribe el archivo original
		grep -v "physicalType" constant/polyMesh/boundary >constant/polyMesh/boundary.temp
		mv constant/polyMesh/boundary.temp constant/polyMesh/boundary

		# Reemplaza "patch" por "wall" en las líneas 35
		sed -i '23s/patch/wall/;' "constant/polyMesh/boundary"

		decomposePar
		mpirun -np 8 simpleFoam -parallel

		reconstructPar
		foamToVTK

		rm -rR processor*

		mv "constant/" ".."
		mv "0/" ".."
		mv "system/" ".."
		mv "VTK/" ".."
		mv "mesh.geo" ".."

		cd ..

		rm -rR "Case_${i}_${valores_lc[$j]}/"

		# Crea la carpeta del caso
		mkdir "Case_${i}_${valores_lc[$j]}"

		mv "constant/" "Case_${i}_${valores_lc[$j]}/"
		mv "0/" "Case_${i}_${valores_lc[$j]}/"
		mv "system/" "Case_${i}_${valores_lc[$j]}/"
		mv "VTK/" "Case_${i}_${valores_lc[$j]}/"
		mv "mesh.geo" "Case_${i}_${valores_lc[$j]}/"

		# Se copia script de extraccion
		cp "Case_0/deltap_extract.py" "Case_${i}_${valores_lc[$j]}/"

		# se reemplaza el valor de i y de j+1 en el script de extraccion
		sed -i "s/\$ii/$i/g" "Case_${i}_${valores_lc[$j]}/deltap_extract.py"
		sed -i "s/\$jj/$k/g" "Case_${i}_${valores_lc[$j]}/deltap_extract.py"

		cd "Case_${i}_${valores_lc[$j]}/"
		pvpython deltap_extract.py

		cd ..

	done

	cd ..
done

echo "Proceso completado."
