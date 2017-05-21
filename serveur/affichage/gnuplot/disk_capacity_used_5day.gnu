set terminal dumb

set xlabel "day of month" 
set ylabel "% disk capacity"
set title "% disk capacity in the last 5 days"


set key on outside left bmargin box title "Légende"
set datafile separator ";"
set autoscale
set xdata time
set timefmt "%Y-%m-%d-%H:%M:%S"
set xdata time
set format x "%d/%m"
set yrange [0:100]

plot "../stockage_collection/bdd/stat.dat" using 1:10 title "Disk/Days" 
