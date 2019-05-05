from log_reader import reader
f=reader()
from csv_writer import ins

from math_foo import median,pers_90,pers_99 #Основные статистические функции, которые мы написали в другом файле

import datetime


import re
nn=re.split('\;|,', f[0])[4].split()[-1]
for i in range(1,10):
    st=re.split('\;|,', f[i])
    #if st[4].split()[-1]==nn:
        #print(i)


#Эта штука будет смотреть текущее время работы системы
current_time=datetime.datetime.strptime(re.split('\;|,', f[0])[0],'%H:%M:%S.%f')
#Создаём словарь очередей, где на вход поступает входной сигнал и ожидает своего ответа
quant={}

#Счётчик заполненности словаря
sch=0

Seconds_mass={}

for i in range(50000):
    st=re.split('\;|,', f[i])
    if ("P2_COD"not in f[i]) and ('SQLProxy' not in f[i]): #Проверяем нет ли у нас игнорируемых сигналов
        
        mee=[]
        if st[8].split()[0]=='type':
            mee=st[8].split()
        else:
            for j in range(4,len(st)-3):
                if st[j].split()[0]=='type':
                    mee=st[j].split()
            

        #Случай, поступает новая входная команда
        #Данные содержатся в формате [формат, время начала исполнения]
        if ( st[4].split()[-1] not in quant ) and ( int(mee[-1])<100 ):
            quant[st[4].split()[-1]]=[int(mee[-1]),datetime.datetime.strptime(st[0],'%H:%M:%S.%f')]
            sch+=1
    
        #Случай, когда поступает новая выходная команда
        if ( st[4].split()[-1] in quant ) and ( int(mee[-1])>100 ):
            quant[st[4].split()[-1]][1]=abs(quant[st[4].split()[-1]][1]-datetime.datetime.strptime(st[0],'%H:%M:%S.%f')).total_seconds()
            sch-=1
            
        #Проверяем прошла ли секунда и если да, то заносим все данные в таблицу
        if (abs(current_time-datetime.datetime.strptime(st[0],'%H:%M:%S.%f')).total_seconds()>1 and sch==0) or (i==len(f)):
            #Теперь отсчёт начинаем с другого момента
            timing=current_time.strftime("%H.%M.%S")
            current_time=datetime.datetime.strptime(st[0],'%H:%M:%S.%f')
            
            
            
            #Теперь, когда истекла секунда, создаём словарь для последующего занесения данных в ксв (Хааа, звучит прям как кфс)))
            #Seconds_mass={} - так будут его звать
            Seconds_mass={}

            for j in quant:
                #Проверяем есть ли указанный элемент в словаре
                if quant[j][0] not in Seconds_mass:
                    Seconds_mass[quant[j][0]]=[quant[j][1]]
                else:
                    Seconds_mass[quant[j][0]].append(quant[j][1])
                    
            #Заносим результаты в csv
            for j in Seconds_mass:
                Seconds_mass[j].sort()
                ins(timing,j,len(Seconds_mass[j]),sum(Seconds_mass[j])/len(Seconds_mass[j]),median(Seconds_mass[j]),pers_90(Seconds_mass[j]),pers_99(Seconds_mass[j]),max(Seconds_mass[j]))

