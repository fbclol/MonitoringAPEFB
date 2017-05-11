set terminal dumb

set xlabel "le jour du mois" 
set ylabel "nbre de utilisateur co."
set title "Nombre d'utilisateur connecté sur les 5 dernier jours"


set key on outside left bmargin box title "Légende"
set datafile separator ";"
set autoscale
set xdata time
set timefmt "%Y-%m-%d-%H:%M:%S"
set xdata time
set format x "%d/%m"

plot "../stockage_collection/bdd/9bf6d4adc10f.dat" using 1:2 title "User/Jour" 