def calculate_discount(original_price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = original_price * (discount_percentage / 100) 
        final_price = original_price - discount_amount
        return final_priceclear
    else: 
     return original_price
#prompt user input
original_price=float(input("enter the original_price of the item: $")) 
discount_percentage=float(input("enter the discount percentage:")) 
final_price = calculate_discount(original_price, discount_percentage)
if final_price == original_price:
     print("No discount applied. Final price:", final_price)
else:
     print("Final price after discount:", final_price)
    
