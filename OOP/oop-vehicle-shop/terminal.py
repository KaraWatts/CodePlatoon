from car_management import CarManager

TERMINAL = [
    "1. Add a car",
    '2. View all cars',
    "3. View total number of cars",
    "4. See a car's details",
    "5. Service a car",
    "6. Update milage",
    "7. Quit"
]


def car_manager_menu():
    for menu_item in TERMINAL:
        print(menu_item)
    choice = input("What would you like to do? ")
    return menu_actions(choice)


def menu_actions(input):
    match input:
        case "1":
            CarManager.add_car()
            car_manager_menu()
        case "2":
            CarManager.view_all_cars()
            car_manager_menu()
        case "3":
            CarManager.view_num_cars()
            car_manager_menu()
        case "4":
            CarManager.see_car_details()
            car_manager_menu()
        case "5":
            CarManager.car_service()
            car_manager_menu()
        case "6":
            CarManager.update_mileage()
            car_manager_menu()
        case "7":
            return 'Goodbye'
        case _:
            print('Not a valid option')
            car_manager_menu()



print(car_manager_menu())

# car_one = CarManager('Buick', 'Lesabre', 1998, 125000)
# car_two = CarManager('Honda', 'Civic', 2001, 95000)
# print(car_one)
# print(car_two)
# car_one.set_make = 123
# car_one.set_mileage = 100000
# car_one.set_model = 'corola'
# car_one.set_year = 1
# print(car_one)