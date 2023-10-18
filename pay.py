saat = int(input("Enter saat : "))
pool = float(input("Enter pool : "))

if saat >100 :
    overtime_hours =saat - 100                                      
    overtime_pay = overtime_hours * (pool * 1.5)                    
    regular_pay = 100 * pool                                        
    pay = regular_pay + overtime_pay
    print("your income is ", pay)
else :
    pay = saat * pool                                               
    print ("your income" , pay)
