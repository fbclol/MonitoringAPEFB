set terminal dumb

set xlabel "day of month" 
set ylabel "number of tasks"
set title "Number of tasks in each day of month"

set key on outside left bmargin box title "Légende"
set datafile separator ";"
#set autoscale
set xdata time
set timefmt "%Y-%m-%d-%H:%M:%S"
set xdata time
set format x "%d/%m"
#set yrange [0:1000]

plot 	"../stockage_collection/bdd/stat.dat" using 0:5 title "Tasks_Total./Days",\
	"../stockage_collection/bdd/stat.dat" using 0:6 title "Tasks_Running./Days" 

set yrange [GPVAL_DATA_Y_MIN:GPVAL_DATA_Y_MAX]
replot
