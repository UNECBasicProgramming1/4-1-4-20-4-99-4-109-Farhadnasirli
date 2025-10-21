import math

#4.1

#a=int(input())
#b=int(input())
#if a>b:
    #print("наибольшее число",a)
    #print("наименьшее число",b)
#elif b>a:
    #print("наибольшее число",b)
    #print("наименьшее число",a)
#else:
    #print("оба числа равны")

#4.2

#x=int(input())
#y=0
#if x>0:
    #y=(math.sin(x))**2
    #print(y)
#else:
    #y=1-2*(math.sin(x))**2
    #print(y)

#4.3

#x=int(input())
#y=0
#if x>0:
    #y=(math.sin(x))**2
    #print(y)
#else:
    #y=1+2*(math.sin(x))**2
    #print(y)

#4.4

#x=int(input())
#y=int(input())
#if x>4:
    #print("2")
#else:
    #print("1")

#4.5

#x=int(input())
#y=int(input())
#if y>3:
    #print("1")
#else:
    #print("2")

#4.6

#a)

#x=float(input())
#if x<=2:
    #y=x
#else:
    #y=2
#print(y)

#b)

#x=float(input())
#if x<=3:
    #y=-x
#else:
    #y=-3
#print(y)

#4.7

#x=int(input())
#if math.sin(x)<0:
    #k=x**2
#else:
    #k=abs(x)
#if k<x:
    #f=k*x
#else:
    #f=k+x
#print(f)


#4.8

#x=int(input())
#if math.sin(x)<0:
    #k=abs(x)
#else:
    #k=x**2
#if x<k:
    #f=abs(x)
#else:
    #f=k*x
#print(f)

#4.9

#a=float(input())
#b=float(input())
#if a>b:
    #print("Максимальное число:",a)
    #print("Минимальное число:",b)
#else:
    #print("Максимальное число:",b)
    #print("Минимальное число:",a)

#4.10

#kilometr=float(input())
#futov=float(input())
#kilometr=kilometr*1000
#futov=futov*0.3048
#if kilometr>futov:
    #print("наименьшее расстояние",futov)
#else:
    #print("наименьшее расстояние",kilometr)

#4.11

#kmchas=float(input())
#metrsek=float(input())
#kmchas=kmchas*(5/18)
#if kmchas>metrsek:
    #print(kmshas,"больше")
#elif kmchas<metrsek:
    #print(metrsek,"больше")
#else:
    #print("скорости равны")

#4.12

#r=int(input())
#a=int(input())
#skruq=math.pi*(r**2)
#skvadrat=a**2
#if skruq>skvadrat:
    #print(skruq,"больше")
#else:
    #print(skvadrat,"больше")

#4.13

#v1=int(input())
#m1=int(input())
#v2=int(input())
#m2=int(input())
#r1=m1/v1
#r2=m2/v2
#if r1>r2:
    #print("первый материал плотнее")
#else:
    #print("второй материал плотнее")

#4.14

#R1=int(input())
#R2=int(input())
#U1=int(input())
#U2=int(input())
#I1=U1/R1
#I2=U2/R2
#if I1>I2:
    #print("первый ток больше")
#else:
    #print("второй ток больше")

#4.15

#a=int(input())
#b=int(input())    
#c=int(input())
#D=b**2-4*a*c
#if D > 0:
    #print("Два действительных корня.")
#elif D == 0:
    #print("Один действительный корень.")
#else:
    #print("Действительных корней нет.")

#4.16

#a=int(input())
#b=int(input())    
#c=int(input())
#D=b**2-4*a*c
#x1=(-b-(D)**0.5)/(2*a)
#x2=(-b+(D)**0.5)/(2*a)
#if D>0:
    #print("корни",x1,x2)
#else:
    #print("корней нет")

#4.17

#year=int(input())
#month=int(input())
#yearnow=int(input())
#monthnow=int(input())
#if month>monthnow:
    #age=yearnow-year-1
    #month=12-(month-monthnow)
    #print(age,month)       
#elif month<monthnow:
    #age=yearnow-year
    #month=monthnow-month
    #print(age,month)
#else:
    #print(yearnow-year)

#4.18

#skruq=int(input())
#skvadrat=int(input())
#r=(skruq/(math.pi))**0.5
#a=(skvadrat)**0.5
#a)
#if 2*r<=a:
    #print("круг помещается")
#else:
    #print("круг не помещается")

#b)
#if a*(2**0.5)<=2*r:
    #print("квадрат помещается")
#else:
    #print("квадрат не помещается")

#4.19

#skruq=int(input())
#streuq=int(input())
#r=(skruq/(math.pi))**0.5
#a=((streuq*4)/((3)**0.5))**0.5

#a)
#rvpisan=(a*(3)**0.5)/6
#if r<=rvpisan:
    #print("поместится")
#else:
    #print("нет")
#b)
#ropisan=(a*(3)**0.5)/3
#if r>=ropisan:
    #print("поместится")
#else:
    #print("нет")

#4.20

#a1=float(input())
#a2=float(input())


#4.99

#a)

#a=float(input())
#b=float(input())
#if b>a:
    #max_val=b
#if a>b:
    #max_val=a
#print("Наибольшее число",max_val)

#b)

#a=float(input())
#b=float(input())
#max_val=a
#if b>a:
    #max_val=b
#print("Наибольшее число", max_val)

#4.100

#a=float(input())
#b=float(input())
#if b>a:
    #max_val=b
    #min_val=a
#if b<a:
    #min_val=b
    #max_val=a
#print("Наибольшее число",max_val)
#print("Наименьшее число",min_val)

#4.101

#a)

#a=float(input())
#b=float(input())
#c=float(input())
#if b>a and b>c:
    #max_val=b
#if c>a and c>b:
    #max_val=c
#if a>b and a>c:
    #max_val=a
#print("Наибольшее число:", max_val)

#b)

#a=float(input())
#b=float(input())
#c=float(input())
#if a>b and c>b:
    #min_val=b
#if b>c and a>c:
    #min_val=c
#if b>a and c>a:
    #min_val=a
#print("Наименьшее число:", min_val)

#4.102

#a=float(input())
#b=float(input())
#c=float(input())
#d=float(input())
#if b>a and b>c and b>d:
    #max_val = b
#if c>a and c>b and c>d:
    #max_val = c
#if d>a and d>b and d>c:
    #max_val = d
#print("Наибольшее число:", max_val)

#4.103

#x=float(input())
#abs1=(x**2)**0.5
#print("Абсолютная величина",abs1)

#4.104

#a)

#a=float(input())
#b=float(input())
#abs1=(a**2)**0.5
#abs2=(b**2)**0.5
#print("Полусумма абсолютных величин заданных чисел",(abs1+abs2)/2)

#b)

#a=float(input())
#b=float(input())
#abs1=(a**2)**0.5
#abs2=(b**2)**0.5
#print(" квадратный корень из произведения абсолютных величин заданных чисел",(abs1*abs2)**0.5)

#4.105

#a=int(input())
#b=int(input())
#if abs(a)>abs(b):
    #a=a/2
#print(a)

#4.106

#a=int(input())
#b=int(input())
#if a**0.5>b**0.5:
    #b=b*5
#print(b)

#4.107

#a=int(input())
#b=int(input())
#c=int(input())
#x=[a,b,c]
#for i in x:
    #if i%2==0:
        #print(i)

#4.108

#a=int(input())
#b=int(input())
#c=int(input())
#x=[a,b,c]
#for i in x:
    #if i>=0:
        #print(i**2)

#4.109

#a=float(input())
#b=float(input())
#c=float(input())
#x=[a,b,c]
#for i in x:
    #if 1.6<=i<=3.8:
        #print(i)
