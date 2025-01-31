product_name = input("Enter product name: ")
purchased_quantity = int(input("Enter purchased quantity : "))  #Must be positive integers

discounted_rate_1 = 0.10  #Equivalent to 10%
discounted_rate_2 = 0.15  #Equivalent to 15%

if purchased_quantity > 0:
    cost_per_product = float(input("Cost per item: "))  # must be positive floating integers
    if cost_per_product > 0 and type(cost_per_product) == float:
        sold_quantity = int(input("Enter sold quantity: "))  #must be positive integers and not exceed the purchased quantity
        if 0 < sold_quantity <= purchased_quantity:
            selling_price_per_product = float(input("Selling price per item: "))  #must be positive floating-point numbers
            if type(selling_price_per_product) == float and selling_price_per_product>0.0:
                province = input("Enter province: ").upper()  #must be one of the listed provinces
                if province == "ON":
                    GST_or_HST = 13
                    total_purchase_cost = purchased_quantity * cost_per_product
                    if sold_quantity > 100:
                        discounted_rate = discounted_rate_1
                    elif sold_quantity > 200:
                        discounted_rate = discounted_rate_2
                    else:
                        discounted_rate =0
                        print("No Discount")

                    discounted_selling_price_per_product = selling_price_per_product * (1 - discounted_rate)
                    total_revenue_excluding_GST_or_HST = sold_quantity * discounted_selling_price_per_product
                    GST_or_HST_amount = total_revenue_excluding_GST_or_HST * discounted_rate
                    total_revenue_including_GST_or_HST = total_revenue_excluding_GST_or_HST + GST_or_HST
                    profit_or_loss = total_revenue_excluding_GST_or_HST - total_purchase_cost
                    print("*********************************************************")
                    print("*** Final Report ***")
                    print("*********************************************************")
                    print("Category \t Value")
                    print("Product Name: ", product_name)
                    print("Province: ", province)
                    print("Purchased Quantity: ", purchased_quantity)
                    print("Sold Quantity: ", sold_quantity)
                    print("Remaining Quantity")
                    print("Total purchase cost: ", total_purchase_cost)
                    print("Discount Rate: ", discounted_rate_1*100,"%")
                    print("Discounted_per_product: ", discounted_selling_price_per_product)
                    print("Total Revenue excluding GST/HST",total_revenue_excluding_GST_or_HST)
                    print("GST amount",GST_or_HST_amount)
                    print("Total Revenue(Incl. GST)", total_revenue_including_GST_or_HST)
                    print("No profit or loss",profit_or_loss)
                    print("************************************************************")

                else:
                    print("Province must be ON")
            else:
                print("Invalid input, the value must be positive")
        else:
            print("Sold quantity cannot exceed purchase quantity")
            exit(0)
    else:
        print("Invalid input, the value must be positive")
        exit(0)
else:
    print(f"Invalid input the value must be positive ")
    exit(0)



