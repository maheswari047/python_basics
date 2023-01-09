#######ENGINE################


def lms_engine(p_loan_rules_masterdata,p_cust_cs,p_cust_loan,p_cust_name):
 cust_out={}
 for c1 in p_loan_rules_masterdata :
   # print(c1)

   if p_cust_cs>=c1["cust_cs_start"] and p_cust_cs<=c1["cust_end"] and p_cust_loan>=c1["loan_amt_start"] and p_cust_loan<=c1["loan_amt_end"]:
    cust_out["appl_name"] = p_cust_name
    cust_out["appl_cs"] = p_cust_cs
    cust_out["loan_amt"] = p_cust_loan
    cust_out["appl_status"] = "approved"
    cust_out["appl_int"]=c1["int"]
    cust_out["appl_dur"] = c1["dur"]

 return(cust_out)