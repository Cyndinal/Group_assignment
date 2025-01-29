
product_name = input("Name of the grocery product: ")
purchased_quantity = int(input("Total number of purchased quantity: "))  # Must be positive integers

discounted_rate_1 = 0.10  # Equivalent to 10%
discounted_rate_2 = 0.15  # Equivalent to 15%

if purchased_quantity > 0:
    cost_per_product = float(input("Price paid per product during purchase: "))  # Must be positive floating integers
    if cost_per_product > 0:
        sold_quantity = int(input("Total number of product sold: "))  # Must be positive integers and not exceed the purchased quantity
        if 0 < sold_quantity <= purchased_quantity:
            selling_price_per_product = float(input("Price per product when sold: "))  # Must be positive floating-point numbers
            if selling_price_per_product > 0.0:
                province = input("The province where the sale occurred: ")  # Must be one of the listed provinces
                if province == "ON":
                    GST_or_HST = 13
                    total_purchase_cost = purchased_quantity * cost_per_product
                    if sold_quantity > 200:
                        discounted_rate = discounted_rate_2
                    elif sold_quantity > 100:
                        discounted_rate = discounted_rate_1
                    else:
                        discounted_rate = 0

                    discounted_selling_price_per_product = selling_price_per_product * (1 - discounted_rate)
                    total_revenue_excluding_GST_or_HST = sold_quantity * discounted_selling_price_per_product
                    GST_or_HST_amount = total_revenue_excluding_GST_or_HST * (GST_or_HST / 100)
                    total_revenue_including_GST_or_HST = total_revenue_excluding_GST_or_HST + GST_or_HST_amount
                    profit_or_loss = total_revenue_excluding_GST_or_HST - total_purchase_cost

                    print("Product Name: ", product_name)
                    print("Purchased Quantity: ", purchased_quantity)
                    print("Sold Quantity: ", sold_quantity)
                    print("Remaining Quantity: ", purchased_quantity - sold_quantity)
                    print("Total purchase cost: ", total_purchase_cost)
                    print("Discount Rate: ", discounted_rate)
                    print("Discounted per product: ", discounted_selling_price_per_product)
                    print("Total Revenue excluding GST/HST: ", total_revenue_excluding_GST_or_HST)
                    print("GST amount: ", GST_or_HST_amount)
                    print("Total Revenue including GST/HST: ", total_revenue_including_GST_or_HST)
                    print("Profit or Loss amount: ", profit_or_loss)
                else:
                    print("Province must be ON")
            else:
                print("Selling Price must be a floating value and must be greater than 0.0")
        else:
            print("Sold quantity must be greater than zero and less than purchased quantity")
    else:
        print("Cost price must be a floating value greater than 0.0")
else:
    print(f"Purchase quantity cannot be negative: {purchased_quantity}")
