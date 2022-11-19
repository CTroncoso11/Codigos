import csv


with open("hola.csv","r") as csv_file:
 csv_reader=csv.reader(csv_file)
  with open("new_hola.csv","w") as new_hola:
   escribir=csv.writer(new_hola, delimiter="-")
   
   for line in csv_reader:
    escribir.writerow(line)