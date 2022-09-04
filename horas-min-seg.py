import math
print("-----------------------")
print("HORA-DADOS-LOS-SEGUNDOS")
print("-----------------------")
#Imput
seg =input("Digite el número de segundos ")
seg = int(seg)
min2  = h2 = 0
#Processing
if seg >= 3600:
        h=seg//3600
        s1=seg%3600
        if s1 == 0:
            print("Horas")
            print(h)
            print("Minutos")
            print(min2)
            print("Segundos")
            print(s1)
        else:
            if s1 >= 60:
                min=s1//60
                s2=s1%60
                if s2 == 0:
                    print("Horas")
                    print(h)
                    print("Minutos")
                    print(min)
                    print("Segundos")
                    print(s2)
                else:
                    if s2 <= 59:
                        print("Horas")
                        print(h)
                        print("Minutos")
                        print(min)
                        print("Segundos")
                        print(s2)
else:
            if seg >= 60 and seg < 3600:
                min=seg//60
                s2=seg%60
                if s2 == 0:
                    print("Horas")
                    print(h2)
                    print("Minutos")
                    print(min)
                    print("Segundos")
                    print(s2)
                else:
                    if s2 <= 59:
                        print("Horas")
                        print(h2)
                        print("Minutos")
                        print(min)
                        print("Segundos")
                        print(s2)
            else:
                        print("Horas")
                        print(h2)
                        print("Minutos")
                        print(min2)
                        print("Segundos")
                        print(seg)