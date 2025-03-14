class Book:
    title:str
    author:str
    year:int
    genre:str
    pages:int

    def info(self):
        print(f"name:{self.title}")
        print(f"autor:{self.author}")
        print(f"genre:{self.genre}")
    def is_long(self):
        if self.pages>300:
            print("True")
        else:
            print("False")
a=Book()
a.title="pushka"
a.author="lermontov"
a.year=888
a.genre="grust"
a.pages=40000


class Student:
    name:str
    age:int
    university:str
    year_of_student:int
    gra:float

    def student_year(self):
        print(f"name:{self.name}")
    def is_excellent(self):
        if self.gra>=4.5:
            print("True")
        else:
            print("False")

l=Student()
l.name="lercpp"
l.age=4
l.university="politex-lutshiy"
l.year_of_student=0
l.gra=8.0


class Auto:
    make:str
    model:str
    year:int
    color:str
    mileage:int

    def car_info(self):
        print(f"mark:{self.make}")
        print(f"model:{self.model}")
        print(f"year:{self.year}")
    def needs_service(self):
        if self.mileage>100000:
            print("True")
        else:
            print("False")

c=Auto()
c.make="gromila"
c.model="loshadka"
c.year=1
c.color="ffff"
c.mileage=20


class Telefon:
    brand:str
    model:str
    year:int
    battery_capacity:int
    price:float

    def phon_info(self):
        print(f"brand:{self.brand}")
        print(f"model:{self.model}")
        print(f"year:{self.year}")
    def is_expensive(self):
        if self.price>30000:
            print("True")
        else:
            print("False")

p=Telefon()
p.brand="SSSSSVBVVVVVVV31 POKO YLTRA"
p.model="wwwwwwwwwwwwww09"
p.year=0
p.battery_capacity=0
p.price=10000000000000.1


class Nooyt:
    brand:str
    model:str
    year:int
    ram:int
    price:float

    def laptop_info(self):
        print(f"brand:{self.brand}")
        print(f"model:{self.model}")
        print(f"year:{self.year}")
        print(f"ram{self.ram}")
    def is_high_end(self):
        if self.ram>16 and self.price>50000:
             print("True")
        else:
            print("False")

m=Nooyt()      
m.brand="ne bomba 2025"
m.model="3..2...1.."
m.year=883
m.ram=3
m.price=99999999999.999999
