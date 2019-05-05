#Расчитываем медиану значений: берём 50- среднее значение в упорядоченной выборке
def median(mass):
    if len(mass)%2==0:
        a=mass
        return (a[len(mass)//2]+a[(len(mass)//2)-1])/2
    else:
        return(mass[len(mass)//2])

#Расчитываем 90- перцентиль
def pers_90(mass):
    return(mass[round((len(mass)/10)*9)-1])

#Расчитываем 99- перцентиль
def pers_99(mass):
    return(mass[round((len(mass)/100)*99)-1])
