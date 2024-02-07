
class CarManager:
    all_cars = []
    total_cars = 0
    last_id = 0
    TERMINAL = [
        "1. Add a car",
        '2. View all cars',
        "3. View total number of cars",
        "4. See a car's details",
        "5. Service a car",
        "6. Update milage",
        "7. Quit"
    ]

    def __init__(self, make: str, model: str, year: int, mileage: int = 0) -> (int, str):
        self._id = None
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = []

        self.set_id
        self.set_make = self._make
        self.set_make = self._model
        self.set_year = self._year
        self.set_mileage = self._mileage
        



    # Class Properties
    @property
    def get_id(self):
        return self._id
    
    @property
    def get_make(self):
        return self._make.title()
    
    @property
    def get_model(self):
        return self._model.title()
    
    @property
    def get_year(self):
        return self._year
    
    @property
    def get_mileage(self):
        return  self._mileage
    
    @property
    def get_service_history(self):
        return self._services
    
    #Validations

    def test_string(self, value):
        if not isinstance(value, str):
            print('Invalid entry - string values only')
        else:
            return value.lower()

    def test_num(self, value):
        if not isinstance(value, int):
            print('Invalid entry - numeric values only')
        else:
            return True

    #Setters
    @get_id.setter
    def set_id(self):
            CarManager.last_id += 1
            self._id = CarManager.last_id
    
    @get_make.setter
    def set_make(self, new_make):
        if self.test_string(new_make):
            self._make = new_make.lower()

    @get_model.setter
    def set_model(self, new_model):
        if self.test_string(new_model):
            self._model = new_model

    @get_year.setter
    def set_year(self, new_year):
        if self.test_num(new_year) and len(str(new_year)) == 4:
            self._year = new_year
        else:
            print(('Invalid year: enter year in the yyyy format'))

    @get_mileage.setter
    def set_mileage(self, new_mileage):
        if self.test_num(new_mileage) and new_mileage > self.get_mileage:
            self._model = new_mileage
        else: 
            print(f'You cannot reduce car mileage. Value must be larger that {self.get_mileage}')


    def add_car(self):
        pass
        

    def view_all_cars():
        pass

    def view_total_cars():
        pass

    def car_details():
        pass

    def service_car():
        pass

    def update_mileage():
        pass

    def quit():
        pass
    
    @staticmethod
    def menu_actions(choice):
        match choice:
            case '1':
                CarManager.add_car()
            case '2':
                CarManager.view_all_cars()
            case '3':
                CarManager.view_total_cars()
            case '4':
                CarManager.car_details()
            case '5':
                CarManager.service_car()
            case '6':
                CarManager.update_mileage()
            case '7':
                return 'Goodbye'
            case _: 
                print("Invalid Choice. Please select a valid option,")
                print('')
                print('')
                CarManager.menu()

    @staticmethod
    def menu():
        for menu_item in CarManager.TERMINAL:
            print(menu_item)
        choice = input("What would you like to do? ")
        return CarManager.menu_actions(choice)
    

    def __str__(self):
        return f'Car {self.get_id}: {self.get_year} {self.get_make} {self.get_model} with {self.get_mileage} miles and {len(self.get_service_history)} services'

print(CarManager.menu())

car_one = CarManager('Buick', 'Lesabre', 1998, 125000)
car_two = CarManager('Honda', 'Civic', 2001, 95000)
print(car_one)
print(car_two)
car_one.set_make = 123
car_one.set_mileage = 100000
car_one.set_model = 'corola'
car_one.set_year = 1
print(car_one)