set terminal dumb

set xlabel "day of month" 
set ylabel "% of memory available"
set title "% memory available in the last 5 days"


set key on outside left bmargin box title "Légende"
set datafile separator ";"
set autoscale
set xdata time
set timefmt "%Y-%m-%d-%H:%M:%S"
set xdata time
set format x "%d/%m"
set yrange [0:100]

plot "../stockage_collection/bdd/stat.dat" using 1:4 title "Mem./Days" 
