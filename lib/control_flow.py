#!/usr/bin/env python3


def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"


def hows_the_weather(temp):
    if temp < 40:
        return "It's brisk out there!"
    elif temp < 65:
        return "It's a little chilly out there!"
    elif temp <= 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def calculator(operation, num1, num2):
    calculations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2,
    }
    if operation in calculations:
        return calculations[operation]
    else:
        print("Invalid operation!")
        return None
