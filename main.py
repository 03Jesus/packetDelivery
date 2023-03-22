import datetime
from classes import *
from classes.person import Person, Customer, Receiver
from classes.address import Address
from classes.payMethod import PayMethod
from classes.products import Product, StandardPackage, OverweightPackage
from classes.bill import Bill
from classes.deliver import Deliver

ACTUAL_DATE = datetime.datetime.now()

#Main
if __name__ == "__main__":
    id_counter = 100
    print("Welcome to the delivery system!")
    print(("*" * 10) + " Please enter your data " + ("*" * 10)) 
    #Ask for name
    name = input("Enter your name: ")
    #Ask for street
    street = input("Enter your street: ")
    #Ask for number
    number = int(input("Enter your number: "))
    #Ask for city
    city = input("Enter your city: ")
    #Ask for zip code
    zip_code = input("Enter your zip code: ")
    #Ask for pay method
    print("Pay methods: ")
    print("1. Cash")
    print("2. Credit Card")
    print("3. Debit Card")
    print("4. PayPal")
    print("5. Bank Transfer")
    #Validate pay method
    while True:
        try:
            pay_method = int(input("Enter your pay method: "))
            if pay_method not in range(1, 6):
                raise ValueError
            break
        except ValueError:
            print("Invalid pay method. Try again.")

    print(("*" * 10) + " Please enter the receiver data " + ("*" * 10)) 
    #Ask for receiver name
    receiver_name = input("Enter receiver name: ")
    #Ask for receiver street
    receiver_street = input("Enter receiver street: ")
    #Ask for receiver number
    receiver_number = int(input("Enter receiver number: "))
    #Ask for receiver city
    receiver_city = input("Enter receiver city: ")
    #Ask for receiver zip code
    receiver_zip_code = input("Enter receiver zip code: ")

    print(("*" * 10) + " Please enter the contact data " + ("*" * 10)) 
    #Ask for contact name
    contact_name = input("Enter contact name: ")
    #Ask for contact street
    contact_street = input("Enter contact street: ")
    #Ask for contact number
    contact_number = int(input("Enter contact number: "))
    #Ask for contact city
    contact_city = input("Enter contact city: ")
    #Ask for contact zip code
    contact_zip_code = input("Enter contact zip code: ")

    print(("*" * 10) + " Please enter the products " + ("*" * 10)) 
    products = []
    while True:
        id_counter += 1
        weight = float(input("Weight: "))
        description = input("Description: ")
        cost = float(input("Cost: "))
        quantity = int(input("Quantity: "))
        weight_limit = float(input("Weight limit: "))
        #Calculate if the product is a standard package or an overweight package
        if weight * quantity <= weight_limit:
            products.append(StandardPackage(id, weight, description, cost, quantity))
        else:
            products.append(OverweightPackage(id, weight, description, cost, weight_limit))
        #ask if there are more products
        if input("More products? (y/n): ") == "n":
            break

    #Create deliver
    deliver = Deliver(id_counter, ACTUAL_DATE, Customer(name, Address(street, number, city, zip_code), PayMethod(pay_method, "Cash")),
                                                        Receiver(receiver_name, Address(receiver_street, receiver_number, receiver_city, receiver_zip_code)),
                                                        Address(street, number, city, zip_code),
                                                        Address(receiver_street, receiver_number, receiver_city, receiver_zip_code),
                                                        Person(contact_name, Address(contact_street, contact_number, contact_city, contact_zip_code)),
                                                        products)
    #Create bill
    bill = Bill(Customer(name, Address(street, number, city, zip_code), PayMethod(pay_method, "Cash")), deliver)
    #Print bill
    print(("*" * 10) + " Bill " + ("*" * 10)) 
    print(bill)