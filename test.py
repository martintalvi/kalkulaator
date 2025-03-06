class Cal:
    def __init__(self,a,b):             
        self.a = a
        self.b = b

    def liitmine(self):                
        return self.a + self.b
    def lahutamine(self):               
        return self.a - self.b
    def korrutamine(self):              
        return self.a * self.b
    def jagamine(self):
        if self.b == 0:
            return "Jagamine nulliga pole lubatud!"
        return self.a / self.b
    def jaak(self):
        if self.b == 0:
            return "Jagamine nulliga pole lubatud!"
        return self.a % self.b
    def juur(self):
        if self.a < 0 and self.b % 2 == 0:
            return "Paarisarvulist juurt negatiivsest arvust ei saa leida!"
        return self.a ** (1 / self.b)
    def astendamine(self):
        return self.a ** self.b
    def keskmine(self):
        return (self.a + self.b)/2

a = float(input("Sisesta esimene number: "))
b = float(input("Sisesta teine number: "))

kalk = Cal(a,b)

while True:
    def menu():
        x = '0. Lõpeta\n1. Liitmine\n2. Lahutamine\n3. Korrutamine\n4. Jagamine\n5. Jäägi leidmine\n6. Juure leidmine\n7. Astendamine\n8. Keskmise leidmine'
        print(x)
    menu()
    valik = int(input('Sisesta üks valikutest: '))
    if valik == 0:
        print("Lõpetatud")
        break
    if valik == 1:
        print("Vastus: ",kalk.liitmine())
        break
    elif valik == 2:
        print("Vastus: ",kalk.lahutamine())
        break
    elif valik == 3:
        print("Vastus: ",kalk.korrutamine())
        break
    elif valik == 4:
        print("Vastus: ",kalk.jagamine())
        break
    elif valik == 5:
        print("Vastus: ",kalk.jaak())
        break
    elif valik == 6:
        print("Vastus: ",kalk.juur())
        break
    elif valik == 7:
        print("Vastus: ", kalk.astendamine())
        break
    elif valik == 8:
        print("Vastus: ", kalk.keskmine())
        break
    else:
        print('\nSellist valikut pole! Vali üks number 0st 8ni.')




