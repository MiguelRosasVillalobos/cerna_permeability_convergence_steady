# Lista de valores para v
valores_lc=("lc1" "lc2" "lc3" "lc4" "lc5" "lc6" "lc7" "lc8")
for j in {0..7}; do
  # Crear un archivo temporal para el script modificado
  temp_script="temp_script_${valores_lc[$j]}.py"

  # Copia el script original a un script temporal
  cp extractor_p5.py $temp_script

  # Usa sed para reemplazar '$p' en el script temporal con el valor actual de p
  sed -i "s/\$jj/${valores_lc[$j]}/g" $temp_script

  # Ejecuta el script Python modificado
  pvpython $temp_script

  # Opcional: Eliminar el script temporal después de la ejecución
  rm $temp_script

  # Opcional: Añadir otros comandos aquí si es necesario
done
