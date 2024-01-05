from sqlalchemy import create_engine, Column, String, Integer, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    car_brand = Column(String)
    car_model = Column(String)
    car_color = Column(String)
    car_year = Column(String)
    car_price = Column(FLOAT)

    def __init__(self, car_brand, car_model, car_color, car_year, car_price):
        self.car_brand = car_brand
        self.car_model = car_model
        self.car_color = car_color
        self.car_year = car_year
        self.car_price = car_price

    def __repr__(self):
        return f"car: {self.car_brand} {self.car_model}, color: {self.car_color}, year: {self.car_year}. Car price of this car is {self.car_price}"


engine = create_engine("sqlite:///cars.db", echo=True)

try:
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        menu = input("1 - insert new car, 2 - see all cars, 3 - search by car brand, 4 - search by car brand and model, 5 - search by min and max price, 6 - close program ")
        match menu:
            case "1":
                brand = input("Car brand: ")
                model = input("Car model: ")
                color = input("Car color: ")
                year = input("Car year: ")
                price = input("Car price: ")

                car = Car(brand, model, color, year, price)
                session.add(car)
                session.commit()
                print("Car added successfully!")

            case "2":
                cars = session.query(Car).all()
                print(f"All found cars: {len(cars)}")
                print(cars)

            case "3":
                brand = input("What brand of the car you want to search?: ")
                filtered_cars = session.query(Car).filter(Car.car_brand == brand).all()
                print(f"Number of cars with brand '{brand}': {len(filtered_cars)}")
                print(filtered_cars)

            case "4":
                brand = input("What brand of the car you want to search? ")
                model = input("And what model of this brand you want to search? ")
                filtered_cars = session.query(Car).filter(Car.car_brand == brand, Car.car_model == model).all()
                print(f"Number of cars with brand '{brand}' and model '{model}': {len(filtered_cars)}")
                print(filtered_cars)

            case "5":
                min_price = float(input("Enter the minimum price: "))
                max_price = float(input("Enter the maximum price: "))
                price_range_cars = session.query(Car).filter(Car.car_price.between(min_price, max_price)).all()
                print(f"Number of cars in the price range {min_price} to {max_price}: {len(price_range_cars)}")
                print(price_range_cars)

            case "6":
                break

            case _:
                print("Insert correct number from the menu list")

except Exception as e:
    print(f"An error occurred: {e}")