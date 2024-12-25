# vazifa 1
from dataclasses import dataclass, field

class MyValueError(Exception):
    pass


@dataclass
class Productdata:
    mahsulot_nomi: str
    _narx: int or float = field(repr=False)
    bor_yoki_yoq: bool

    def __post_init__(self):
        if self._narx < 0:
            raise MyValueError("Narx manfiy bolmasligi kerak")

    @property
    def narx(self):
        return self._narx

    @narx.setter
    def narx(self, new_narx):
        if new_narx < 0:
            raise MyValueError("Narx manfiy bolmasligi kerak")
        self._narx = new_narx

@dataclass
class ElectronicProduct(Productdata):
    kafolat_muddati: int


    def __str__(self):
        return (f"Mahsulot nomi: {self.mahsulot_nomi}, Narxi: ${self.narx}, "
                f"Mavjudligi: {'Bor' if self.bor_yoki_yoq else 'Yo\'q'}, "
                f"Kafolat muddati: {self.kafolat_muddati} oy")


laptop = ElectronicProduct(mahsulot_nomi="Laptop", _narx=1200.0, bor_yoki_yoq=True, kafolat_muddati=24)

print(laptop)

# ========================================================================================

# vazifa 2
from dataclasses import dataclass, field


class MyValueError(Exception):
    pass


@dataclass
class Vehicledata:
    markasi: str
    _tezlik: int = field(repr=False)

    def __post_init__(self):
        if self._tezlik >= 300:
            raise MyValueError("Tezlik 300 dan oshmasligi kerak!!!")

    @property
    def tezlik(self):
        return self._tezlik

    @tezlik.setter
    def tezlik(self, new_tezlik):
        if new_tezlik >= 300:
            raise MyValueError("Tezlik 300 dan oshmasligi kerak!!!")
        self._tezlik = new_tezlik

@dataclass
class Car(Vehicledata):
    yoqilgi_turi: str

    def __str__(self):
        return (f"Mashina markasi: {self.markasi}, Tezlik: {self.tezlik} km/soat, "
                f"Yoqilg'i turi: {self.yoqilgi_turi}")



@dataclass
class Bicycle(Vehicledata):
    tormiz_turi: str

    def __str__(self):
        return (f"Motodsikl markasi: {self.markasi}, Tezlik: {self.tezlik} km/soat, "
                f"Tormoz turi: {self.tormiz_turi}")


car = Car(markasi="Toyota", _tezlik=250, yoqilgi_turi="Benzin")
print(car)

bicycle = Bicycle(markasi="Giant", _tezlik=150, tormiz_turi="Disk")
print(bicycle)

# ========================================================================================

# vazifa 3
from dataclasses import dataclass, field

class MyValueError(Exception):
    pass


@dataclass
class Bookdata:
    kitob_nomi: str
    _narx: int or float = field(repr=False)
    muallifi: str

    def __post_init__(self):
        return self._narx

    @property
    def narx(self):
        return self._narx

    @narx.setter
    def narx(self, new_narx, admin):
        if admin:
            if new_narx > 0:
                self._narx = new_narx
                print(f"Narx {new_narx} ga o'zgartirildi.")
            else:
                print("Narx manfiy yoki nol bo'lishi mumkin emas.")
        else:
            print("Sizda narxni o'zgartirish huquqi yo'q.")

@dataclass
class EBook(Bookdata):
    fayl_xajmi: int or float

    def info(self):
        return f"E-Book: '{self.kitob_nomi}' by {self.muallifi}, File size: {self.fayl_xajmi}MB, Price: ${self.narx:.2f}"

@dataclass
class PrintedBook(Bookdata):
    qogoz_turi: str

    def info(self):
        return f"Printed Book: '{self.kitob_nomi}' by {self.muallifi}, Paper type: {self.qogoz_turi}, Price: ${self.narx:.2f}"



ebook = EBook(kitob_nomi="Python Programming", muallifi="John Doe", _narx=10.99, fayl_xajmi=5.5)
printed_book = PrintedBook(kitob_nomi="Machine Learning", muallifi="Jane Smith", _narx=25.99, qogoz_turi="Glossy")

print(ebook.info())
print(printed_book.info())

# ========================================================================================

# vazifa 4
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Employee(ABC):
    name: str
    position: str
    _salary: float

    @property
    def salary(self):
        return self._salary

    def increase_salary(self, amount, approved_by):
        if approved_by.lower() == "director":
            self._salary += amount
            print(f"{self.name}'ning maoshi {amount} ga oshirildi. Yangi maosh: {self._salary}")
        else:
            print(f"{self.name}'ning maoshini oshirish huquqi {approved_by}da mavjud emas.")

    @abstractmethod
    def perform_duties(self):
        pass

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, "Manager", salary)

    def manage_team(self):
        return f"{self.name} jamoani boshqarmoqda."

    def perform_duties(self):
        return f"{self.name} rahbarlik vazifalarini bajaradi."

class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, "Developer", salary)

    def write_code(self):
        return f"{self.name} kod yozmoqda."

    def perform_duties(self):
        return f"{self.name} dasturlash bilan shug'ullanadi."

manager = Manager("Ali", 5000)
developer = Developer("Bek", 3000)

print(manager.salary)
print(developer.salary)

manager.increase_salary(1000, "Director")
developer.increase_salary(500, "HR")

manager.manage_team()
manager.perform_duties()

developer.write_code()
developer.perform_duties()

# ========================================================================================

# vazifa 5
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Athlete(ABC):
    name: str
    sport: str
    _records: list

    @property
    def records(self):
        return self._records

    def update_records(self, new_record):
        if new_record not in self._records:
            self._records.append(new_record)
            print(f"{self.name} yangi rekord qo'shdi: {new_record}")
        else:
            print(f"{self.name} uchun rekord allaqachon mavjud: {new_record}")

    @abstractmethod
    def special_skill(self):
        pass

class Runner(Athlete):
    def __init__(self, name, records):
        super().__init__(name, "Running", records)

    def special_skill(self):
        print(f"{self.name} juda tez yuguradi.")

    def run_distance(self, distance):
        print(f"{self.name} {distance} metr masofani yugurdi.")

class Swimmer(Athlete):
    def __init__(self, name, records):
        super().__init__(name, "Swimming", records)

    def special_skill(self):
        print(f"{self.name} suvda tez suzadi.")

    def swim_pool(self, pool_length):
        print(f"{self.name} {pool_length} metr havzani suzib o'tdi.")

runner = Runner("Usain Bolt", ["100m: 9.58s"])
swimmer = Swimmer("Michael Phelps", ["200m Butterfly: 1:51.51"])

print(runner.records)
print(swimmer.records)

runner.update_records("200m: 19.19s")
swimmer.update_records("200m Butterfly: 1:51.51")

runner.special_skill()
runner.run_distance(400)

swimmer.special_skill()
swimmer.swim_pool(50)

