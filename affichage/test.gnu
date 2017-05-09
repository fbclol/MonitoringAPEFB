set terminal dumb

set timefmt "[%Y-%m-%d %H:%M:%S]";
set xdata time; 
set format x "%Y-%m-%d-%H-%M-%S"; 
set yrange [0:5]; 
set xrange ["2009-05-11 07:30:00":"2009-06-11 00:34:00"];
set grid;

plot  'test.dat' using 1:2 t ''