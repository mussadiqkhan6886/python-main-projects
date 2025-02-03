from OOPS_PROJECT import Phone

phone1 = Phone("1280x720", "Note 7 lite", "Infinix", "6GB", "120GB", "32MP", "64MP", "Black\nGreen\nRed\nBlue", "24500 PKR", "New")
phone2 = Phone("1360x1280", "14 Pro Max", "IPHONE", "8GB", "256GB", "100MP", "300MP", "Gold\nBlack\nRed\nGray", "$1500", "New")
phone3 = Phone("1360x1280", "S21", "Samsung", "16GB", "256GB", "90MP", "300MP", "Gray", "$980", "Used, 1.2 years\nno issues")

while True:
    brand = input("Enter Which phone specification you want to see: ").lower()
    if brand != "exit":
        spec = input(f"What specifiction you want to see in {brand}: ").lower()

    if brand == "infinix":
        if spec == "display":
            print(phone1.display)
        elif spec == "name":
            print(phone1.name)
        elif spec == "brand":
            print(phone1.brand)
        elif spec == "ram":
            print(phone1.ram)
        elif spec == "space":
            print(phone1.space)
        elif spec == "front camera":
            print(phone1.front_camera)
        elif spec == "back camera":
            print(phone1.back_camera)
        elif spec == "color":
            print(phone1.color)
        elif spec == "price":
            print(phone1.cost)
        elif spec == "condition":
            print(phone1.condition)
    elif brand == "iphone":
        if spec == "display":
            print(phone2.display)
        elif spec == "name":
            print(phone2.name)
        elif spec == "brand":
            print(phone2.brand)
        elif spec == "ram":
            print(phone2.ram)
        elif spec == "space":
            print(phone2.space)
        elif spec == "front camera":
            print(phone2.front_camera)
        elif spec == "back camera":
            print(phone2.back_camera)
        elif spec == "color":
            print(phone2.color)
        elif spec == "price":
            print(phone2.cost)
        elif spec == "condition":
            print(phone2.condition)
    elif brand == "samsung":
        if spec == "display":
            print(phone3.display)
        elif spec == "name":
            print(phone3.name)
        elif spec == "brand":
            print(phone3.brand)
        elif spec == "ram":
            print(phone3.ram)
        elif spec == "space":
            print(phone3.space)
        elif spec == "front camera":
            print(phone3.front_camera)
        elif spec == "back camera":
            print(phone3.back_camera)
        elif spec == "color":
            print(phone3.color)
        elif spec == "price":
            print(phone3.cost)
        elif spec == "condition":
            print(phone3.condition)
    elif brand == "exit" or spec == "exit":
        break
    else:
        print("\nError please try again\n")
        
print("Have a nice day")