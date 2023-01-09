#############CALLER##################
import os
import engine
import masterdata

input_file = open("D:/Python\lms_input.txt","r")

while True:
    var_file = input_file.readline()
    if not var_file:
        break
    else:
     split_value = var_file.split(',')
     cust_name = split_value[0]
     cust_cs = int(split_value[1])
     cust_loan = int(split_value[2])
     result = engine.lms_engine(p_loan_rules_masterdata=masterdata.loan_rules_masterdata,
                                p_cust_cs=cust_cs,
                                p_cust_loan=cust_loan,
                                p_cust_name=cust_name)
     print(result)
     out_file = open("D:/Python\lms_output","a")
     output_file = out_file.write(str(result)+"\n")

input_file.close()
out_file.close()





