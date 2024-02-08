import re


class CarManager:
    all_cars = {}
    total_cars = 0

    
    def __init__(self, make, model, year, mileage = None, services = None):
        self._id = CarManager.total_cars + 1
        CarManager.total_cars += 1
        self._make = make 
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services     

    def __str__(self):
        return f"ID: {self._id}, Make: {self._make}, Model: {self._model}, Year: {self._year}, Mileage: {self._mileage}, Services: {self._services}"
        
    
    # Validation Methods
    @staticmethod
    def check_int(value, Variable):
        try:
                return int(value)
        except:
                print("Input Error: Numeric values only.")
                CarManager.check_int(input(f"Enter {Variable}: "), Variable)

    @classmethod
    def check_owners(cls, name):
        if name == 'quit':
            return False
        elif name not in cls.all_cars:
            print("Name not found")
            CarManager.check_owners(input("Please enter owner to search in First_Last format: "))
        return True
    @staticmethod
    def check_year(new_year):
        if len(str(new_year)) == 4:
            return CarManager.check_int(new_year, "Year")
        else:
            print(('Invalid year: enter year in the yyyy format'))
            CarManager.check_year(input(f"Enter year: "))

    @classmethod
    def add_car(cls):
        owner_name = input("Enter name in First_Last format: ").lower()
        new_make = input("Enter make: ").lower() 
        new_model = input("Enter model: ").lower()
        new_year = cls.check_int(input("Enter year: "), "year")
        new_mileage = cls.check_int(input("Enter Mileage: "), "Mileage")
        
        new_car = cls(new_make, new_model, new_year, new_mileage)
       
        cls.all_cars[owner_name] = new_car
        
    @classmethod   
    def view_all_cars(cls):
        for car in cls.all_cars:
             print(car, cls.all_cars[car])
        
    @classmethod
    def view_num_cars(cls):
        print(cls.total_cars)
         
    @classmethod
    def see_car_details(cls):
        owner_search = input("Please enter owner to search in First_Last format: ").lower()
        print(cls.all_cars[owner_search])
      
    @classmethod
    def car_service(cls):
        owner_name = input("Enter owner name in First_last format: ").lower()
        if cls.check_owners(owner_name):
            service = input("Enter all services: ")
            cls.all_cars[owner_name]._services = service
            return None
    
        
    @classmethod
    def update_mileage(cls):
        owner_name = input("Enter owner name in First_last format: ").lower()
        mileage = input("Enter mileage: ")
        if cls.check_int(mileage):
            if mileage > cls.all_cars[owner_name]._mileage:
                cls.all_cars[owner_name]._mileage = mileage
               
        else:
            print("Mileage must be a number and contain no decimals")
            cls.update_mileage()
            
        
    



        

# action = input("Please enter what you would like to do. Add a car - enter 'Add' | View all cars - enter 'View all' | View total number of car - enter 'View num' | See a car's details - enter 'See car'. : ")
# if action == "Add":
#     owner_car = input("Please enter owner name: ")  
#     owner_name =  re.sub(r"\s", '_', owner_car)
#     new_make, new_model, new_year = input("Enter make: "), input("Enter model: "), input("Enter year: ")
#     new_car = CarManager(new_make, new_model, new_year)
#     new_car.add_car()
#     print(CarManager.view_all_cars())
#     action
# print(CarManager.terminal_menu())


# car1 = CarManager()