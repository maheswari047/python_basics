###################  Shopping Cart   ######################
cust_num =[]
cust_details = {}
cust_products ={}
#########customer details#####################
number_cust =input("enter number of customer")
for e in range(int(number_cust)):
 cust_input = input("enter name, id, date")
 cust_list = list(cust_input.split(','))
 cust_details["name"]= cust_list[0]
 cust_details["id"]= cust_list[1]
 cust_details["date"]= cust_list[2]
 cust_num.append(cust_details)
 cust_details = {}
print(cust_num)

#############################
######Product details##############
product_details = {}
final_prod=[]
num_prod = input("enter number of products")

for a in range(int(num_prod)):
 product_info = input("enter product,quantity and price")
 product_list = list(product_info.split(','))
 product_details["name"] =product_list[0]
 product_details["quantity"] = product_list[1]
 product_details["price"] = product_list[2]
 final_prod.append(product_details)
 product_details ={}
print(final_prod)

##########calculating Total##########################
total =0
for b in final_prod:
 total = total + (int(b["quantity"]) * int(b["price"]))

print("The calculated total = ",total)