import argparse
from helpers import *

# 1. variable sold_list gets the output (list) of get_sold() (with the date passed into get_inventory and exp_list get the ouput (list) of get_expired() 
# 2. if user passes in "all" the turnover of complete inventory is displayed within specified time frame (start_date, end_date)
# 3. if user passes in a product the turnover for this product is displayed within specified time frame
# 4. error message if type of product passed in is incorrect
# 5. error message if product passed in does not exist in inventory
def turnover(start_date: str, end_date: str, product: str):
    # checks if format of dates passed in is correct
    checkStartDate = checkDate(start_date)
    checkEndDate = checkDate(end_date)

    if checkStartDate == True and checkEndDate == True:
        #creates a txt file to store the result of turnover in
        create_txt("turnover.txt")

        sold_list = get_sold(end_date)
            
        if product == "all":
            total_sold   = 0
            
            for sold_product in sold_list:
                sell_date = sold_product[3]
                if sell_date >= start_date and sell_date <= end_date:
                    sell_price = float(sold_product[4])
                    total_sold += sell_price
            
            turnover = total_sold
            
            console.print(f"The total turnover from {start_date} until {end_date} for {product} is [green]{turnover:.2f}[/].")
            f = open("turnover.txt", "a")
            f.write(f"The total turnover from {start_date} until {end_date} for {product} is {turnover:.2f}.")
            f.close()

        elif type(product) == str:
            total_sold   = 0
            for list_item in sold_list:
                if product in list_item:
                    for sold_product in sold_list:
                        sell_date = sold_product[3]
                        if product in sold_product and sell_date >= start_date and sell_date <= end_date:
                            sell_price = float(sold_product[4])
                            total_sold += sell_price

                    turnover = total_sold
                    console.print(f"The total turnover from {start_date} until {end_date} for {product}[/] is {turnover:.2f}[/].")
                    f = open("turnover.txt", "a")
                    f.write(f"The total turnover from {start_date} until {end_date} for {product} is {turnover:.2f}")
                    f.close()
                    return    
                
            console.print("Product not in inventory.", style="bold red")    
            
        else:
            console.print("Please enter a valid product name or 'all'.", style="bold red")
    else:
        console.print(f"Please enter the dates in correct format yyyy-mm-dd.", style="bold red")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Report total or product turnover for specified timeframe.")
                
    parser.add_argument("start_date", help="Enter start date for timeframe (format: yyyy-mm-dd).")
    parser.add_argument("end_date", help="Enter end date for timeframe (format: yyyy-mm-dd).")
    parser.add_argument("product", help="Enter product in lowercase (i.e. 'orange') or 'all' for the turnover report.")

    args = parser.parse_args()

    turnover(start_date=args.start_date, end_date=args.end_date, product=args.product)