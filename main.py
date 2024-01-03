import sqlite3

conn = sqlite3.connect('cars.db')
c = conn.cursor()

# query = '''
# CREATE TABLE car (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     car_brand VARCHAR(50),
#     car_model VARCHAR(50),
#     car_color VARCHAR(50),
#     car_year DATE,
#     car_price FLOAT
# );
# '''
#
# c.execute(query)
conn.commit()


while True:
    menu = input("1 - insert new car, 2 - search car by brand, 3 - search car by brand and model, 4 - search by price, 5 - see all cars, 6 - close program ")
    match menu:
        case "1":
            brand = input("Car brand")
            model = input("Car model")
            color = input("Car color")
            year = input("Car year")
            price = input("Car price")

            try:
                with conn:
                    c.execute(
                        "INSERT INTO car (car_brand, car_model, car_color, car_year, car_price) VALUES (?, ?, ?, ?, ?)",
                        (brand, model, color, year, price))
                print('successfully added')
            except sqlite3.Error as e:
                print("SQLite error:", e)

        case "2":
            brand = input("Car brand")
            with conn:
                c.execute("SELECT * FROM car WHERE car_brand=?", (brand,))
                print(c.fetchall())

        case "3":
            brand = input("Car brand")
            model = input("Car model")
            with conn:
                c.execute("SELECT * FROM car WHERE car_brand=? AND car_model=?", (brand, model))
                print(c.fetchall())

        case "4":
            price_from = input("Price from")
            price_to = input("Price to")
            with conn:
                c.execute("SELECT * FROM car WHERE car_price BETWEEN ? AND ?", (price_from, price_to))
                print(c.fetchall())

        case "5":
            with conn:
                c.execute(f"SELECT * From car")
                print(c.fetchall())

        case "6":
            break

        case _:
            print("Insert correct number form menu list")

conn.close()