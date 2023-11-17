breakfast_name = ['Alu Parata', 'Tanduri Ruti', 'Nan', 'Dal Puri', 'Ruti', 'Dal Vaji', 'Halua', 'Egg Omlete',
                  'Chicken Soup']
breakfast_price = [30, 40, 35, 35, 30, 20, 25, 20, 35]
lunch_name = ['Fried Rice', 'Fried Chicken', 'Kachi Biryani', 'Chicken Khichuri', 'Mutton Khichuri', 'Mutton Tehari',
              'One Plate Vat', 'Koi Fish', 'Hilsha Fish']
lunch_price = [100, 150, 230, 180, 280, 220, 50, 80, 120]
dinner_name = ['Mutton Rezala', 'Mutton Leg Roast', 'Chicken Kalia', 'Alu Bhorta', 'Moshur Dal', 'Chicken Vegetable',
               'Rui Fish', 'Mutton Biryani', 'Faluda']
dinner_price = [150, 120, 80, 20, 40, 40, 120, 200, 60]
ordered_food = []
ordered_bill = []
discount = 0


def home_page():
    print("*" * 20 + " Welcome to Food Ordering Management System " + "*" * 20 + "\n"
                                                                   "\t(O) ORDER FOOD\n"
                                                                   "\t(E) EXIT APP\n" +
          "_" * 84)

    input_1 = str(input("Please Select Your Operation: "))
    if (input_1 == 'O' or input_1 == 'o'):
        main_menu()

    elif (input_1 == 'E' or input_1 == 'e'):
        print("Exiting Food Ordering App")

    else:
        print("Wrong Input")


def main_menu():
    print("*" * 31 + " MAIN MENU " + "*" * 31 + "\n"
                                                "\t(B) BREAKFAST\n"
                                                "\t(L) LUNCH\n"
                                                "\t(D) DINNER\n" +
          "_" * 72)

    input_1 = str(input("Please Select Your Operation: "))
    if (input_1 == 'L' or input_1 == 'l'):
        show_lunch()

    elif (input_1 == 'D' or input_1 == 'd'):
        show_dinner()

    elif (input_1 == 'B' or input_1 == 'b'):
        show_breakfast()

    else:
        print("Wrong Input")


def show_breakfast():
    print("SERIAL   FOOD ITEM           PRICE")
    for i in range(len(breakfast_name)):
        print(
            "No." + str(i + 1) + "     " + str(breakfast_name[i]) + " " * (20 - len(breakfast_name[i])) + "Tk. " + str(
                breakfast_price[i]))

    total_bill = 0
    while True:
        food_item = input("Please Select Your Food Serial Number: ")

        if not food_item.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue

        food_item = int(food_item)

        if 1 <= food_item <= len(breakfast_name):
            print(str(breakfast_name[food_item - 1]) + " is added to your cart")
            ordered_food.append(breakfast_name[food_item - 1])
            ordered_bill.append(breakfast_price[food_item - 1])
            total_bill += breakfast_price[food_item - 1]

            option = input("Anything else? (y/n)")
            if option.lower() != 'y':
                break
        else:
            print("Invalid serial number. Please select a number between 1 and", len(breakfast_name))


    print("Ordered Foods:")
    print("SERIAL   FOOD ITEM           PRICE")
    for i in range(len(ordered_food)):
        print("No." + str(i + 1) + "     " + str(ordered_food[i]) + " " * (20 - len(ordered_food[i])) + "Tk. " + str(
            ordered_bill[i]))
    print("-----------------------------------")
    print("Total Bill = Tk." + str(total_bill))

    input_1 = input("Apply Discount? (y/n):")
    if input_1 == 'Y' or input_1 == 'y':
        global discount
        while True:
            try:
                discount = int(input("Discount % ?:"))
            except ValueError:
                print("Invalid input. Let's try again...")
            else:
                break
        total_bill = total_bill - (total_bill * discount / 100)
        print("Total Bill after Discount: TK. " + str(total_bill))

    elif (input_1 == 'N' or input_1 == 'n'):
        print("Total Bill without any Discount: TK. " + str(total_bill))

    else:
        print("Wrong Input")

    print("\t(P) PAYMENT\n"
          "\t(C) CANCEL\n")

    input_1 = input("Please Select Your Option: ")
    if (input_1 == 'P' or input_1 == 'p'):
        payment()

    elif (input_1 == 'C' or input_1 == 'c'):
        print("Your Order Cancel")

    else:
        print("Wrong Input")


def show_lunch():
    print("SERIAL   FOOD ITEM           PRICE")
    for i in range(len(lunch_name)):
        print("No." + str(i + 1) + "     " + str(lunch_name[i]) + " " * (20 - len(lunch_name[i])) + "Tk. " + str(
            lunch_price[i]))

    total_bill = 0
    while True:
        food_item = input("Please Select Your Food Serial Number: ")

        if not food_item.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue

        food_item = int(food_item)

        if 1 <= food_item <= len(lunch_name):
            print(str(lunch_name[food_item - 1]) + " is added to your cart")
            ordered_food.append(lunch_name[food_item - 1])
            ordered_bill.append(lunch_price[food_item - 1])
            total_bill += lunch_price[food_item - 1]

            option = input("Anything else? (y/n)")
            if option.lower() != 'y':
                break
        else:
            print("Invalid serial number. Please select a number between 1 and", len(lunch_name))


    print("Ordered Foods:")
    print("SERIAL   FOOD ITEM           PRICE")
    for i in range(len(ordered_food)):
        print("No." + str(i + 1) + "     " + str(ordered_food[i]) + " " * (20 - len(ordered_food[i])) + "Tk. " + str(
            ordered_bill[i]))
    print("--------------------------------------")
    print("Total Bill = Tk." + str(total_bill))

    input_1 = input("Apply Discount? (y/n):")
    if (input_1 == 'Y' or input_1 == 'y'):
        global discount
        while True:
            try:
                discount = int(input("Discount % ?:"))
            except ValueError:
                print("Invalid input. Let's try again...")
            else:
                break
        total_bill = total_bill - (total_bill * discount / 100)
        print("Total Bill after Discount: TK. " + str(total_bill))

    elif (input_1 == 'N' or input_1 == 'n'):
        print("Total Bill without any Discount: TK. " + str(total_bill))

    else:
        print("Wrong Input")

    print("\t(P) PAYMENT\n"
          "\t(C) CANCEL\n")
    input_1 = input("Please Select Your Option: ")
    if (input_1 == 'P' or input_1 == 'p'):
        payment()
    elif (input_1 == 'C' or input_1 == 'c'):
        print("Your Order Cancel")

    else:
        print("Wrong Input")


def show_dinner():
    print("SERIAL   FOOD ITEM           PRICE")
    for i in range(len(dinner_name)):
        print("No." + str(i + 1) + "     " + str(dinner_name[i]) + " " * (20 - len(dinner_name[i])) + "Tk. " + str(
            dinner_price[i]))

    total_bill = 0
    while True:
        food_item = input("Please Select Your Food Serial Number: ")

        if not food_item.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue

        food_item = int(food_item)

        if 1 <= food_item <= len(dinner_name):
            print(str(dinner_name[food_item - 1]) + " is added to your cart")
            ordered_food.append(dinner_name[food_item - 1])
            ordered_bill.append(dinner_price[food_item - 1])
            total_bill += dinner_price[food_item - 1]

            option = input("Anything else? (y/n)")
            if option.lower() != 'y':
                break
        else:
            print("Invalid serial number. Please select a number between 1 and", len(dinner_name))


    print("Ordered Foods:")
    print("SERIAL   FOOD ITEM           PRICE")
    for i in range(len(ordered_food)):
        print("No." + str(i + 1) + "     " + str(ordered_food[i]) + " " * (20 - len(ordered_food[i])) + "Tk. " + str(
            ordered_bill[i]))
    print("--------------------------------------")
    print("Total Bill = Tk." + str(total_bill))

    input_1 = input("Apply Discount? (y/n):")
    if (input_1 == 'Y' or input_1 == 'y'):
        global discount
        while True:
            try:
                discount = int(input("Discount % ?:"))
            except ValueError:
                print("Invalid input. Let's try again...")
            else:
                break
        total_bill = total_bill - (total_bill * discount / 100)
        print("Total Bill after Discount: TK. " + str(total_bill))

    elif (input_1 == 'N' or input_1 == 'n'):
        print("Total Bill without any Discount: TK. " + str(total_bill))

    else:
        print("Wrong Input")

    print("\t(P) PAYMENT\n"
          "\t(C) CANCEL\n")

    input_1 = input("Please Select Your Option: ")
    if (input_1 == 'P' or input_1 == 'p'):
        payment()

    elif (input_1 == 'C' or input_1 == 'c'):
        print("Your Order Cancel")

    else:
        print("Wrong Input")


def payment():
    print("Your Payment is Successful")

    input_1 = input("You want Receipt?""\n"
                    "\t(R) RECEIPT\n"
                    "Please Press (R/r):")

    if (input_1 == 'R' or input_1 == 'r'):
        receipt()

    else:
        print("Wrong Input")


def receipt():
    sum = 0
    print("**************************************")
    print("-------------- Receipt ---------------")
    print("--------------------------------------")
    import datetime
    now = datetime.datetime.now()
    print("   Date & Time: " + now.strftime("%Y-%m-%d  %I:%M %p"))
    print("--------------------------------------")
    print("SERIAL   FOOD ITEM           PRICE")
    for i in range(len(ordered_food)):
        print("No." + str(i + 1) + "     " + str(ordered_food[i]) + " " * (
                20 - len(ordered_food[i])) + "Tk. " + str(
            ordered_bill[i]))
        sum += ordered_bill[i]
    print("--------------------------------------")
    print("Total Bill:           (PAID) Tk. " + str(sum - sum * discount / 100))
    print("**************************************")
    input_1 = str(input("Do you want to exit?\n(E) EXIT\nPlease Press (E/e):"))

    if (input_1 == 'E' or input_1 == 'e'):
        print("Exiting App...")

    else:
        print("Wrong Input")


if __name__ == '__main__':
    home_page()