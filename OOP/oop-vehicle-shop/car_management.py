import json


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
    def check_owners(cls, name = None):
        if name == None:
            name = input("Please enter owner to search in First_Last format: ").lower()
        
        
        if name not in cls.all_cars:
            response = input(f"Name not in found in Directory:\n1. Try again\n2. Create new owner account\n3. Quit\n")
            match response:
                 case '1':
                    return cls.check_owners()
                 case '2':
                      return False
                 case '3':
                      return None
        else: 
             return name
    
    @staticmethod
    def check_year(new_year):
        if len(str(new_year)) == 4:
            return CarManager.check_int(new_year, "Year")
        else:
            print(('Invalid year: enter year in the yyyy format'))
            CarManager.check_year(input(f"Enter year: "))

    #Class Manipulation Methods
    @classmethod
    def create_car(cls):
        owner_name = input("Please enter owner to search in First_Last format: ").lower()
        new_make = input("Enter make: ").lower() 
        new_model = input("Enter model: ").lower()
        new_year = cls.check_year(input("Enter year: "))
        new_mileage = cls.check_int(input("Enter Mileage: "), "Mileage")

        new_car = cls(new_make, new_model, new_year, new_mileage)

        return [owner_name, new_car]
        
    @classmethod
    def add_car(cls):
        owner_name, new_car = cls.create_car()
        verified_name = cls.check_owners(owner_name)
        match verified_name:
            case False:
                cls.all_cars[owner_name] = [new_car]
            case None:
                  return None
            case _:
                cls.all_cars[verified_name].append(new_car)
       
        
        
    @classmethod   
    def view_all_cars(cls):
        for owner_name, cars in cls.all_cars.items():
            for car in cars:
                print(owner_name.title(), car)
        
    @classmethod
    def view_num_cars(cls):
        print(cls.total_cars)
         
    @classmethod
    def see_car_details(cls):
        owner_name = cls.check_owners()
        for car in cls.all_cars[owner_name]:
                print(owner_name.title(), car)
      
    @classmethod
    def car_service(cls):
        owner_name = cls.check_owners()
        if owner_name:
            # get list of all cars associated with the owner
            cars = cls.all_cars[owner_name]

            #print all cars associated with the owner
            print(f"Cars owned by {owner_name}:")
            for index, car in enumerate(cars, start=1):
                print(f"{index}. {car}")  
            
            # Prompt the user to select a car for service
            car_index = input("Select car to be serviced: ")

            try:
                car_index = int(car_index)
                selected_car = cars[car_index - 1]  # Adjust index to match list indexing
            except (ValueError, IndexError):
                print("Invalid selection. Please enter a valid car number.")
                return
            
            service = input("Enter all services: ")
            selected_car._services = service
        
    @classmethod
    def update_mileage(cls):
        owner_name = cls.check_owners()
        if owner_name:
            mileage = int(input("Enter mileage: "))
            if cls.check_int(mileage, 'Mileage') and mileage > cls.all_cars[owner_name]._mileage:
                    cls.all_cars[owner_name]._mileage = mileage
            else:
                print(f"You cannot dial back your odometer reading. Return value higher than {cls.all_cars[owner_name]._mileage}")
                cls.update_mileage()


    