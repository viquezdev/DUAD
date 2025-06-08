product_price=float(input("Tell me the price: "))
if(product_price<100):
    final_price=product_price-(product_price*0.02)
else:
    final_price=product_price-(product_price*0.10)
print(f"The final price is {final_price}")