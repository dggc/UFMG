set title "Fixando os vertices"
set yrange [0.0:0.1]
set xlabel "Porcentagem de arestas"
set ylabel "Tempo(s)"
set terminal png
set output "plot.png"
plot 'time1000.dat' with lines, 'time1250.dat' with lines, \
     'time1500.dat' with lines, 'time1750.dat' with lines, \
     'time2000.dat' with lines
