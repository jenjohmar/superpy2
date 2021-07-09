import argparse
from helpers import *

# 1. opens sold.csv looks at current total line count
# 2. increments total line count with 1 = id
# 3. creates new dict from data passed in, adds id + finds bought_id and adds that
# 4. writes dict to sold.csv
# 5. if amount > 1 each product gets own line and unique sold_id

def sell(prod_name: str, sell_date: str, sell_price: float, amount: int):
    #checks if format of date is correct
    checkSellDate = checkDate(sell_date)

    if checkSellDate == True:
        create_csv("sold.csv", header_sold)
        
        number_of_lines = 0
        with open('sold.csv', 'r') as csv_file:
            for line in csv_file:
                number_of_lines += 1

        id = number_of_lines
    
        new_product_dict = {
            "product_id": id,
            "bought_id": 0,
            "product_name": prod_name,
            "sell_date": sell_date,
            "sell_price": sell_price,
        }

        # returns inventory of today  
        inventory = check_inventory(current_date, prod_name)
        
        #removes  all items from inventory that are not the requested product
        for item in inventory:
            if prod_name not in item:
                inventory.remove(item)
        
        # checks if there are enough items in inventory i.e. >= amount given
        if len(inventory) >= amount:
            # reduces items in inventory to amount given
            inventory = inventory[:amount]
            # writes to sold amount times
            for product in inventory:
                bought_id = product[0]
                old_id = new_product_dict["product_id"]
                new_id = old_id + 1
                new_product_dict["product_id"] = new_id
                new_product_dict["bought_id"] = bought_id
                write_to_sold(new_product_dict)
                        
            console.print(f"Product {prod_name} sold succesfully!", style="bold green")
        else:
            print(f"Amount exceeds product count in inventory! You can currently sell {len(inventory)} of {prod_name}.")

        
    else:
        console.print("Please enter the date in correct format yyyy-mm-dd.", style="bold red")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sell product(s).")
                
    parser.add_argument("prod_name", help="Enter product name in lowercase (i.e. 'orange').")
    parser.add_argument("sell_date", help="Enter product sell date (format: yyyy-mm-dd).")
    parser.add_argument("sell_price", type=float, help="Enter product sell price (format: yyyy-mm-dd).")
    parser.add_argument("amount", type=int, help="Enter amount (number) to sell.")

    args = parser.parse_args()

    sell(prod_name=args.prod_name, sell_date=args.sell_date, sell_price=args.sell_price, amount=args.amount)


