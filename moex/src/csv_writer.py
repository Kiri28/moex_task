import csv
#Запись в новый csv файл
FILENAME = "result_1.csv"
def ins(time,type,quantity,mediun,median,pers90,pers99,max):
    with open(FILENAME, "a", newline="") as file:
        descr = [time,type,quantity,mediun,median,pers90,pers99,max]
        writer = csv.writer(file)
        writer.writerow(descr)

