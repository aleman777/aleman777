
class Car:



    def __init__(self,brand,model,year,color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.wheels = 4

    def print_car(self):
        print(f"I am a {self.brand} {self.model} {self.color} {self.year}")


def main():
     car1 = Car("BMW", "520d sport", "2024", "white")
     car1.print_car()
     car2 = Car("Toyota","camry","2022","black")
     car2.print_car()



if __name__ == '__main__':
    main()