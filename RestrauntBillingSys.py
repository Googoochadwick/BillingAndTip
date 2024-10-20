
menu = {
    "Butter Chicken": 12.99,
    "Paneer Tikka": 8.99,
    "Biryani": 10.99,
    "Samosa": 4.99,
    "Naan": 2.99,
    "Dal Makhani": 7.99,
    "Chole Bhature": 6.99,
    "Palak Paneer": 9.99,
    "Tandoori Chicken": 13.99,
    "Gulab Jamun": 5.99,
    "Rogan Josh": 14.99,
    "Aloo Gobi": 7.49,
    "Chicken Korma": 11.99,
    "Pav Bhaji": 6.49,
    "Pani Puri": 3.99,
    "Bhel Puri": 4.49,
    "Lassi": 3.50,
    "Masala Dosa": 8.99,
    "Idli": 6.99,
    "Vada Pav": 2.99,
    "Fish Curry": 12.49,
    "Methi Thepla": 5.99,
    "Dhokla": 4.99,
    "Pulao": 9.49,
    "Kheer": 4.49,
    "Malai Kofta": 10.99,
    "Bhindi Masala": 8.49,
    "Tikka Masala": 11.49,
    "Beef Curry": 13.49,
    "Vegetable Biryani": 9.99,
    "Chicken Vindaloo": 12.99,
    "Masoor Dal": 6.99,
    "Paneer Butter Masala": 10.49,
    "Chaat": 5.49,
    "Tandoori Roti": 2.49,
    "Aloo Tikki": 3.99,
    "Biryani (Veg)": 10.49,
    "Dum Aloo": 8.99,
    "Baida Roti": 4.49,
    "Pork Vindaloo": 13.99,
    "Chickpea Salad": 5.99,
    "Gajar Halwa": 4.99,
    "Nimbu Pani": 2.49,
    "Bisi Bele Bath": 9.49,
    "Khichdi": 7.49,
    "Kofta Curry": 11.49,
    "Mutton Curry": 14.49,
    "Mixed Vegetable Curry": 8.49,
    "Onion Bhaji": 4.99,
    "Raita": 3.49,
    "Mango Chutney": 2.99,
    "Pulao (Non-Veg)": 12.99,
    "Chowmein": 9.99,
    "Vegetable Spring Rolls": 5.49,
    "Tandoori Fish": 13.99,
    "Dahi Puri": 4.49,
    "Kadhi Pakora": 7.49,
    "Paneer Paratha": 9.49,
    "Stuffed Kulcha": 8.99,
    "Masala Chai": 2.99,
    "Chaas": 2.49
}


def main():
    #initializing amount
    amount = 0
    while True:
        try:
            #Input
            item = input("Item: ").title()
            #Checking If It Exists
            if item in menu:
                amount += menu[item]
                print("Amount ",end="")
                #Formating Upto 2 Decimal Points
                print(f"Total: ₹{amount:.2f}")
            elif item == "Exit":
                Rs = amount
                percent = percent_to_float(input("What percentage would you like to tip? "))
                tip = Rs * percent
                print(f"Leave ₹{tip:.2f}")
                break
            else:
                pass

        except EOFError:

            print()
            break


def percent_to_float(p):
    p = p.replace("%","")
    p = float(p)/100
    return(p)
main()
    












