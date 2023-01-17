
################### Creating empty list and dictionary#############
product_details={}
cust_details={}
billing_details = []
########## Customer details #################
cust_details["name"] ="aaa"
cust_details["id"] =123
cust_details["date"] ="jan"

############# Product details ##################
product_details["product"] ="apple"
product_details["price"] = 10
product_details["quantity"] = 2
product_details["nature"] ="organic"

billing_details.append(product_details)
product_details={}

product_details["product"] ="banana"
product_details["price"] = 20
product_details["quantity"] = 12
product_details["nature"] ="organic"

billing_details.append(product_details)
product_details={}

product_details["product"] ="orange"
product_details["price"] = 32
product_details["quantity"] = 20
product_details["nature"] ="organic"
billing_details.append(product_details)


cust_details["bill"] = billing_details
print(cust_details)

############ Invoice ###################
total=0

for a in cust_details["bill"]:
    print(a['price'])
    print(a["quantity"])
    total = total + ( a["price"] * a["quantity"])


print(total)
