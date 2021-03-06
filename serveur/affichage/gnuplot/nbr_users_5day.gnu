set terminal dumb

set xlabel "day of month" 
set ylabel "number of users logged"
set title "Number of users logged in the last 5 days"


set key on outside left bmargin box title "Légende"
set datafile separator ";"
set autoscale
set xdata time
set timefmt "%Y-%m-%d-%H:%M:%S"
set xdata time
set format x "%d/%m"


plot "../stockage_collection/bdd/stat.dat" using 1:2 title "User/Days" 