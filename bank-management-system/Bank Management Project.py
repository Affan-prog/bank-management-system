import time

path = fr"C:\Users\AFFAN\Desktop\bank-management-system"

def intro():
    
    print()
    print("     ** Bank Management System **")
    print("             Islamic")
    print()
    print("      Brought to you by :")
    print("          Muhammad Affan")
    
    print()
    
    while(True):
    
        start = input("Press Enter to go to Main Menu :")
        
        if(start == ""):
            print("-")
            repeater()
            break
        else:
            print("")
            print("Invalid Input. Try Again .")
            print("")


def main_Menu():

    print()
    print()
    print("        ** Main Menu **")
    print()
    print("1. Open Account")
    print("2. Cash Deposit")
    print("3. Withdraw Amount")
    print("4. Transfer Amount")
    print("5. View Account")
    print("6. Reset PIN")
    print("7. Bill Payment")
    print("8. Statement of Account")
    # print("9. Admin")
    print()
    print("0. Exit")        


def repeater():

    main_Menu()
    options = [1,2,3,4,5,6,7,8,9,0]
    print()

    while(True):
        
        try:
        
            option = int(input("Select an option :"))
    
            if(option in options):
        
                if(option==1):
            
                    open_account_1()
            
                elif(option==2):
                    
                    deposit_amount_2()
            
                elif(option==3):
            
                    withdraw_amount_3()
            
                elif(option==4):
            
                    transfer_amount_4()
            
                elif(option==5):
            
                    view_account_5()
            
                elif(option==6):
            
                    reset_pin_6()
            
                elif(option==7):
            
                    bill_payment_7()
            
                elif(option==8):
            
                    SOA_8()
            
                # elif(option==9):
            
                #     admin_9()
            
                elif(option==0):
            
                    print("Program Terminated.")
                    
                break
        
            else:
                
                print("Invalid Input")
            
        except:
            
            print("")
            print("Input can only be an Integer. Try Again !")
            print("")


def open_account_1():

    

    cust_dtl = {

            "Account Type": "c",
            "Name":"",
            "Date of Birth":"",
            "Phone":"",
            "Initial Deposit":0,
            "Account Balance":0,
            "Time Created":time.strftime("%H:%M %x"),
            "PIN":0,
            "IBAN":0

            
        } 

    print()
    print("        * Open Account *")
    print()



    # 1- Name


    while(True):

        name = input("Enter Full Name : ").strip()
        account_name = name.lower()

        all_alphas = True

        if(name!=""):

            for i in account_name:

                if(i in "abcdefghijklmnopqrstuvwxyz "):

                    all_alphas = True

                else:

                    all_alphas = False
                    break
            
            if(all_alphas==True):

                cust_dtl["Name"] = name
                break

            else:

                print("Invalid Input.")

        else:
            
            print("")
            print("Invalid Input. Name cannot be empty")
            print()       


    # 2- DOB

    while(True):
        
        print("")
        print("Date format : Day-Month-Year, i.e ( 01-12-2000 )")
        
        dob = input("Enter Date of Birth : ").strip()

        all_digits = True

        if(dob!="" and len(dob)==10):

            for i in dob:

                if(i in "0123456789- "):
                    
                    all_digits = True

                else:

                    all_digits = False
                    break

            if(all_digits == True):

                cust_dtl["Date of Birth"] = dob
                break

            else:

                print("Invalid Input. Please enter date in correct format !")

        else:
            
            print("")
            print("Invalid Input. Please enter date in given format !")
            print()  

    # 3- Phone

    while(True):

        try :
            
            phone = input("Enter phone number : ").strip()
            all_digits = True

            if(len(phone)==11):
                
                for i in phone:
                    
                    if(i in "0123456789"):
                        all_digits = True
                        
                    else:
                        all_digits = False
                        break
                    
                if(all_digits == True ):
                    cust_dtl["Phone"] = phone
                    break
                
                elif(all_digits == False):
                    print("Invalid Input !")
                    
            else:
                print("Phone number must contain 11 Digits. !")
                
            
        except :
            
            print("Invalid Input !")

    # 4- Initial Deposit
        
    while(True):
        
        try:
        
            initial = float(input("Enter initial deposit [eg : Minimum = Rs.1000 ]: Rs."))
            
            if(initial < 1000):
                
                print("* Minimum initial deposit = Rs.1000 *")
                
            elif(initial >= 1000):
                cust_dtl["Initial Deposit"] = initial
                cust_dtl["Account Balance"] += cust_dtl["Initial Deposit"]
                cust_dtl.pop("Initial Deposit")
                break
            
        except :
            
            print("Invalid Input !")
        

    print("Details Completed !")

    # 5- PIN

    while(True):


        try:
            pin = int(input("Set 4-Digit PIN code : "))

            if(digit_count(pin) == 4):

                cust_dtl["PIN"] = pin
                break

            else:
                
                print("")
                print("Invalid Input. PIN must contain 4 Digits !")
                print()

        except:

            print("Invalid Input. Try Again !")

    # 6- Favourite food

    while(True):
        
        print("* Note : Please remember your chosen food name; it's needed for PIN resets. *")
        food = input("Enter name of your favourite food: ").strip()
        food_name = food.lower()

        all_alphas = True

        if(food!=""):

            for i in food_name:

                if(i in "abcdefghijklmnopqrstuvwxyz "):

                    all_alphas = True

                else:

                    all_alphas = False
                    break
            
            if(all_alphas==True):

                cust_dtl["food"] = food_name
                break

            else:

                print("Invalid Input.")

        else:
            
            print("")
            print("Invalid Input. Food name cannot be empty")
            print()     



    # Confirmation

    print()
    print("Confirm Details")
    print()

    for x,y in cust_dtl.items():
                    
            if( x == "Account Balance" or x=="IBAN" or x=="Time Created"):
                        
                continue

            else:

                print(x,":",y)

    print()

    print("1. Confirm and Open Account")
    print("2. Cancel and Go Back")


    while(True):

        try:


            stay_or_go = int(input("Select an Option : "))

            # writing to a file
            
            
            if(stay_or_go == 1):

                # getting list of account numbers from file 

                try:
                    file_IBAN = open(fr"{path}\account numbers.txt","r")

                    acc_numbers = eval(file_IBAN.read())
                    largest = max(acc_numbers)
                    cust_IBAN = largest+1
                    cust_dtl["IBAN"] = cust_IBAN
                    file_IBAN.close()

                    # updating the list by appending new/latest account number in it, and then saving/overwriting this updated list in the same file

                    file_IBAN = open(fr"{path}\account numbers.txt","w")

                    acc_numbers.append(cust_IBAN)
                    lst_to_write = str(acc_numbers)
                    file_IBAN.write(lst_to_write)
                    file_IBAN.close()

                    
                    # saving cust_dtl in a file

                    dtls_to_save = str(cust_dtl)
                    cust_info_file = open(fr"{path}\data\Customer info\{cust_IBAN}.txt","w")
                    cust_info_file.write(dtls_to_save)
                    cust_info_file.close()

                    # creating SOA file of the user

                    SOA_file = open(fr"{path}\data\Customer SOA\SOA_{cust_IBAN}","w")
                    SOA_to_write = f"{'Date':<15} {'Description':<30} {'Type':<20} {'Amount':<15}\n\n"
                    SOA_file.write(SOA_to_write)
                    SOA_file.close()

                    # Appending the transaction in Customer's SOA file

                    dep_time = time.strftime("%x")

                    SOA_file = open(fr"{path}\data\Customer SOA\SOA_{cust_IBAN}","a")
                    SOA_to_write = "{0:<15} {1:<30} {2:<20} Rs.{3:<15}\n".format(dep_time,"Initial Deposit","Credit",initial)
                    SOA_file.write(SOA_to_write)
                    SOA_file.close()
                    

                    # Showing the customer his complete details

                    print()
                    print("Account has been Successfully Created !")
                    print()
                    print("Please note your Account number i.e (IBAN) :",cust_IBAN)
                    print()
                    print("        * Account Details *")
                    print()

                    for x,y in cust_dtl.items():
                        
                        if(x=="Account Balance"):
                        
                            print(x,": Rs.",y)

                        else:
                            print(x,":",y)
                    

                    
                    print()

                except Exception as e:

                    print("An Error occured")
                    

                back_to_main = input("Press any key to go to Main Menu :")

                if(back_to_main or back_to_main==""):

                    repeater()


                break


                

                
                # main_menu() function call karna hai idhar !!!!!!!!!!!!!
                # Doneeee!!!


        # ---------------------------------

            elif(stay_or_go != 1):

                cust_dtl = {

                    "Account Type": "",
                    "Name":"",
                    "Date of Birth":"",
                    "Phone":"",
                    "Initial Deposit":0,
                    "Account Balance":0
                    
                }

                print("Process terminated. Back to Main Menu.")
                repeater()

        except:

            print("Invalid Input. Try again !")
   
def deposit_amount_2():

    
    print("")
    print("       * Deposit Amount *")
    print("")

    while(True):

        try:

            AN = int(input("Enter your Account Number :"))

            # i.e converting account number file into list
            file_AN = open(fr"{path}\account numbers.txt","r")
            AN_lst = eval(file_AN.read())
            file_AN.close()

            if(AN in AN_lst):

                print("Account Detected !")

                # getting customer's all data from his dictionary 

                cust_fil = open(fr"{path}\data\Customer info\{AN}.txt","r")
                cust_dtl = eval(cust_fil.read())
                cust_fil.close()

                print()

                while(True):

                    try:

                        pin_code = int(input("Enter your 4-Digit PIN code :"))
                        print("Account confirmed !")
                        print()

                        if(pin_code == cust_dtl["PIN"]):

                            print("Account Holder's Name :",cust_dtl["Name"])
                            print("Your total Account Balance :",cust_dtl["Account Balance"])
                            print("")

                            while(True):

                                try:

                                    dep_amount = float(input("Enter Amount to deposit ( Limit = Rs.500,000 ): Rs."))

                                    if(dep_amount <= 500000 and dep_amount >0):

                                        print("")

                                        while(True):

                                            try:

                                                print(f"Do you wish to deposit Rs.{dep_amount} into your account ?")
                                                print("")
                                                print("1. Yes")
                                                print("2. No")
                                                wish = int(input(f"Select an Option :"))

                                                if(wish==1):

                                                    for x,y in cust_dtl.items():

                                                        if(x=="Account Balance"):

                                                            cust_dtl[x] += dep_amount

                                                    new_cust_fil = open(fr"{path}\data\Customer info\{AN}.txt","w")
                                                    to_write = str(cust_dtl)
                                                    new_cust_fil.write(to_write)
                                                    new_cust_fil.close()

                                                    # updating SOA file of the customer

                                                    dep_time = time.strftime("%x")
                                                    

                                                    SOA_file = open(fr"{path}\data\Customer SOA\SOA_{AN}","a")
                                                    SOA_to_write = "{0:<15} {1:<30} {2:<20} Rs.{3:<15}\n".format(dep_time,"Cash Deposit","Credit",dep_amount)
                                                    SOA_file.write(SOA_to_write)
                                                    SOA_file.close()


                                                    
                                                    print("")
                                                    print("Amount deposited successfully !")
                                                    print("")
                                                    print("Your total Account Balance : Rs.",cust_dtl["Account Balance"])
                                                    print("")
                                                    print("")
                                                    print("Back to Main Menu !")
                                                    print("")

                                                    repeater()


                                                else:

                                                    print("")
                                                    print("Process terminated.")
                                                    print("Back to Main Menu !")
                                                    print("")


                                                    repeater()

      

                                            except:

                                                print("Invalid Input. Please Try Again !")
                                                print("")


                                        break

                                    else:

                                        print("Invalid Input. Try again !")

                                except:

                                    print("Invalid Input. Please Try again !")

                            break

                        else:

                            print("Entered PIN is incorrect !")


                    except:

                        
                        print("Invalid Input. Please Try again !")
                        print("")

                    
                break

            else:
                
                print("Invalid Input. Account does not exist.")
                print("")

            

        except:
            
            print("Invalid Input. Please Try again !")
            print("")

def withdraw_amount_3():

    
    print("")
    print("       * Withdraw Amount *")
    print("")

    while(True):

        try:

            AN = int(input("Enter your Account Number :"))

            # i.e converting account number file into list
            file_AN = open(fr"{path}\account numbers.txt","r")
            AN_lst = eval(file_AN.read())
            file_AN.close()

            if(AN in AN_lst):

                print("Account Detected !")

                # getting customer's all data from his dictionary 

                cust_fil = open(fr"{path}\data\Customer info\{AN}.txt","r")
                cust_dtl = eval(cust_fil.read())
                cust_fil.close()

                print()

                while(True):

                    try:

                        pin_code = int(input("Enter your 4-Digit PIN code :"))
                        print("")

                        if(pin_code == cust_dtl["PIN"]):

                            print("Account Holder's Name :",cust_dtl["Name"])
                            print("Your total Account Balance :",cust_dtl["Account Balance"])
                            bank_balance = cust_dtl["Account Balance"]
                            print("")

                            while(True):

                                try:

                                    wdr_amount = float(input(f"Enter amount to withdraw (i.e upto Rs.{bank_balance} ) : Rs."))

                                    if(wdr_amount <= bank_balance and wdr_amount > 0):

                                        print("")

                                        while(True):

                                            try:

                                                print(f"Do you wish to withdraw Rs.{wdr_amount} from your account ?")
                                                print("")
                                                print("1. Yes")
                                                print("2. No")
                                                wish = int(input(f"Select an Option :"))

                                                if(wish==1):

                                                    for x,y in cust_dtl.items():

                                                        if(x=="Account Balance"):

                                                            cust_dtl[x] -= wdr_amount

                                                    # updating customer's balance

                                                    new_cust_fil = open(fr"{path}\data\Customer info\{AN}.txt","w")
                                                    to_write = str(cust_dtl)
                                                    new_cust_fil.write(to_write)
                                                    new_cust_fil.close()



                                                    # updating customer's SOA

                                                    dep_time = time.strftime("%x")
                                                    

                                                    SOA_file = open(fr"{path}\data\Customer SOA\SOA_{AN}","a")
                                                    SOA_to_write = "{0:<15} {1:<30} {2:<20} Rs.{3:<15}\n".format(dep_time,"Withdrawal","Debit",wdr_amount)
                                                    SOA_file.write(SOA_to_write)
                                                    SOA_file.close()


                                                    
                                                    print("")
                                                    print(f"Withdrawal successfull. Rs.{wdr_amount} has been successfully withdrawn from your account.")
                                                    print("")
                                                    print("Your total Account Balance :",cust_dtl["Account Balance"])
                                                    print("")
                                                    print("")
                                                    print("Back to Main Menu !")
                                                    print("")

                                                    

                                                    repeater()
                                                    break


                                                else:

                                                    print("Process terminated.")
                                                    print("")
                                                    print("Back to Main Menu !")
                                                    print("")


                                                    repeater()
                                                    break

      

                                            except:

                                                print("Invalid Input. Please Try Again !")
                                                print("")


                                        

                                    else:

                                        print("Invalid Input. Please Try again !")

                                except:

                                    print("Invalid Input. Please Try again !")

                            
                            
                            

                        else:

                            print("Entered PIN is incorrect !")


                    except:

                        
                        print("Invalid Input. Please Try again !")
                        print("")


            else:
                
                print("Invalid Input. Account does not exist.")
                print("")

            

        except:
            
            print("Invalid Input. Please Try again !")
            print("")

def transfer_amount_4():

    print("")
    print("")
    print("       * Transfer Amount *")
    print("")
    print("")
    print("Sender's details")
    print("")

    while(True):

        try:
    
            AN = int(input("Enter your Account Number :"))

            file_AN = open(fr"{path}\account numbers.txt","r")
            AN_lst = eval(file_AN.read())
            file_AN.close()

            if(AN in AN_lst):

                print("Account Detected !")
                print("")

                sndr_fil = open(fr"{path}\data\Customer info\{AN}.txt","r")
                sndr_dtl = eval(sndr_fil.read())
                sndr_fil.close()


                while(True):

                    try:

                        pin = int(input("Enter your 4-Digit pin :"))

                        if(pin == sndr_dtl["PIN"]):

                            print("Account confirmed !")
                            print("")

                            print("Account Holder's Name :",sndr_dtl["Name"])
                            print("Your total Account Balance :",sndr_dtl["Account Balance"])
                            print("")

                            while(True):

                                try:

                                    print("")
                                    print("")
                                    print("Beneficiary details")
                                    print("")
                                    

                                    benf_AN = int(input("Enter Reciever's Account Number :"))
                                    

                                    if(digit_count(benf_AN)==10):

                                        if(benf_AN == AN):

                                            print("Cannot Transfer Amount in your own Account.")
                                            continue

                                        else:

                                            while(True):

                                                try:

                                                    transfer_amount = float(input("Enter the transfer amount : Rs."))
                                                    

                                                    if(transfer_amount <= sndr_dtl["Account Balance"]  and transfer_amount > 0 ):

                                                        while(True):

                                                            try:

                                                                print("")
                                                                print(f"Do you wish to transfer Rs.{transfer_amount} ?")
                                                                print("")
                                                                print("1. Yes")
                                                                print("2. No")
                                                                wish = int(input(f"Select an Option :"))

                                                                if(wish==1):
                                                                    
                                                                    if(benf_AN in AN_lst):

                                                                        sndr_dtl["Account Balance"] -= transfer_amount

                                                                        rcvr_fil = open(fr"{path}\data\Customer info\{benf_AN}.txt","r")
                                                                        rcvr_dtl = eval(rcvr_fil.read())
                                                                        rcvr_fil.close()

                                                                        rcvr_dtl["Account Balance"] += transfer_amount

                                                                        # Updating receivers balance

                                                                        new_rcvr_fil = open(fr"{path}\data\Customer info\{benf_AN}.txt","w")
                                                                        to_write_new = str(rcvr_dtl)
                                                                        new_rcvr_fil.write(to_write_new)
                                                                        new_rcvr_fil.close()

                                                                        # Updating senders balance

                                                                        new_sndr_fil = open(fr"{path}\data\Customer info\{AN}.txt","w")
                                                                        to_write_sndr = str(sndr_dtl)
                                                                        new_sndr_fil.write(to_write_sndr)
                                                                        new_sndr_fil.close()


                                                                        # updating customer's SOA

                                                                        dep_time = time.strftime("%x")
                                                                        

                                                                        SOA_file = open(fr"{path}\data\Customer SOA\SOA_{AN}","a")
                                                                        SOA_to_write = "{0:<15} {1:<30} {2:<20} Rs.{3:<15}\n".format(dep_time,"Sent","Debit",transfer_amount)
                                                                        SOA_file.write(SOA_to_write)
                                                                        SOA_file.close()

                                                                    else:


                                                                        sndr_dtl["Account Balance"] -= transfer_amount


                                                                        # Updating senders balance

                                                                        new_cust_fil = open(fr"{path}\data\Customer info\{AN}.txt","w")
                                                                        to_write = str(sndr_dtl)
                                                                        new_cust_fil.write(to_write)
                                                                        new_cust_fil.close()


                                                                        # updating customer's SOA

                                                                        dep_time = time.strftime("%x")
                                                                        

                                                                        SOA_file = open(fr"{path}\data\Customer SOA\SOA_{AN}","a")
                                                                        SOA_to_write = "{0:<15} {1:<30} {2:<20} Rs.{3:<15}\n".format(dep_time,"Sent","Debit",transfer_amount)
                                                                        SOA_file.write(SOA_to_write)
                                                                        SOA_file.close()


                                                                    
                                                                    print("")
                                                                    print(f"Transfer successfull. Rs.{transfer_amount} has been successfully sent.")
                                                                    print("")
                                                                    print("Your total Account Balance : Rs.",sndr_dtl["Account Balance"])
                                                                    print("")
                                                                    print("")
                                                                    print("Back to Main Menu !")
                                                                    print("")

                                                                    repeater()
                                                                    break


                                                                else:

                                                                    print("")
                                                                    print("Process terminated.")
                                                                    print("Back to Main Menu !")
                                                                    print("")


                                                                    repeater()
                                                                    break

                                                            except:

                                                                print("Invalid Input. Please try again.")

                                                        break

                                                    else:

                                                        print("Insufficient Balance.")
                                                        print("")



                                                except:

                                                    print("Invalid Input. Please try again.")

                                        break
                                    
                                    else:

                                        print("Account number must contain 10 Digits.")

                                
                                except:

                                    print("Invalid Input. Please try again.")

                            break

                        else:

                            print("Entered PIN is incorrect.")





                    except:

                        print("Invalid Input. Please try again.")

                break



            else:

                print("Account does not exist. Please try again.")

        except:

            print("Invalid Input. Please try again.")

def view_account_5():

    print("")
    print("        * View Account *")
    print("")

    while(True):

        try:

            AN = int(input("Enter your account number :"))

            file_AN = open(fr"{path}\account numbers.txt","r")
            AN_lst = eval(file_AN.read())
            file_AN.close()

            if(AN in AN_lst):

                print("Account detected !")
                print("")

                cust_fil = open(fr"{path}\data\Customer info\{AN}.txt","r")
                cust_dtl = eval(cust_fil.read())
                cust_fil.close()

                while(True):

                    try:

                        pin_code = int(input("Enter your 4-Digit PIN code :"))

                        if(digit_count(pin_code)==4):

                            if(pin_code==cust_dtl["PIN"]):

                                
                                print("Account confirmed !")
                                print("")
                                print("")

                                print("Following are your account details :")
                                print("")
                                print("")

                                for x,y in cust_dtl.items():
                                    
                                    if(x=="Account Balance"):
                                    
                                        print(x,": Rs.",y)

                                    else:
                                        print(x,":",y)

                                break

                            else:

                                print("Entered PIN is incorrect. Please try again. ")

                        else:

                            print("PIN length must be 4-Digit. Please try again.")

                    except:

                        print("Invalid Input. Please try again.")
            
                print("")
                print("")
                go_main = input("Press any key to go to main menu :")

                if(go_main or go_main==""):

                    print("Back to the Main Menu !")

                    repeater()


                break


            else:

                print("Account does not exist. Please try again.")

        except:

            print("Invalid Input")

def reset_pin_6():


    print("")
    print("")
    print("        * PIN Reset *")
    print("")

    while(True):

        try:
            print("")
            AN = int(input("Enter your Account Number :"))

            file_AN = open(fr"{path}\account numbers.txt","r")
            AN_lst = eval(file_AN.read())
            file_AN.close()

            if(AN in AN_lst):

                print("Account Detected !")
                print("")

                cust_fil = open(fr"{path}\data\Customer info\{AN}.txt","r")
                cust_dtl = eval(cust_fil.read())
                cust_fil.close()


                while(True):

                    try:

                        pin = int(input("Enter your 4-Digit pin :"))

                        if(pin == cust_dtl["PIN"]):

                            print("Account confirmed !")
                            print("")

                            print("Account Holder's Name :",cust_dtl["Name"])
                            print("IBAN : ",cust_dtl["IBAN"])
                            print("Old 4-Digit PIN : ",cust_dtl["PIN"])
                            print("")


                            while(True):

                                try:

                                    food = input("Enter the name of your Favourite Food :").lower()

                                    if(food==cust_dtl["food"]):
                                        print("Details Confirmed !")
                                        print("")
                                        while(True):
                                            
                                            try:

                                                new_pin = int(input("Set a new 4-Digit PIN :"))

                                                if(digit_count(new_pin)==4):

                                                    if(new_pin==cust_dtl["PIN"]):

                                                        print('You cannot reuse your old PIN again.')

                                                    elif(new_pin!=cust_dtl["PIN"]):

                                                        print("")
                                                        print("Confirm reset new PIN ?")
                                                        print("")
                                                        print("1. Yes")
                                                        print("2. No")
                                                        print("")

                                                        while(True):

                                                            try:

                                                                option = int(input("Select an Option :"))

                                                                if(option==1):

                                                                    cust_dtl["PIN"]=new_pin

                                                                    new_cust_fil = open(fr"{path}\data\Customer info\{AN}.txt","w")
                                                                    to_write = str(cust_dtl)
                                                                    new_cust_fil.write(to_write)
                                                                    new_cust_fil.close()  


                                                                    print("")
                                                                    print("Your new PIN is :",new_pin)
                                                                    print("")
                                                                    print("Back to the Main Menu !")
                                                                    
                                                                    go_main = input("Press Any key + Enter to go to main menu :")

                                                                    if(go_main or go_main==""):

                                                                        print("Back to the Main Menu !")

                                                                        repeater()

                                                                    break


                                                                else:

                                                                    print("")
                                                                    print("Process terminated !")
                                                                    print("")
                                                                    print("Back to the Main Menu !")

                                                                    go_main = input("Press any key to go to main menu :")

                                                                    if(go_main or go_main==""):

                                                                        print("Back to the Main Menu !")

                                                                        repeater()

                                                                    break

                                                            except:

                                                                print("Invalid Input.")

                                                        break


                                                else:

                                                    print("PIN must contain 4-Digits.")

                                                


                                            except:

                                                print("Invalid Input.")

                                        break

                                    else:

                                        print("Incorrect Food name. Please try again.")

                                except:

                                    print("Invalid Input.")

                            break

                        else:

                            print("Incorrect PIN Entered !")

                    except:

                        print("Invalid Input.")

                break

        except:

            print("Invalid Input.")

def bill_payment_7():

    print("")
    print("")
    print("        * Bill Payment *")
    print("")
    

    while(True):

        try:
            print("")
            AN = int(input("Enter your Account Number :"))

            file_AN = open(fr"{path}\account numbers.txt","r")
            AN_lst = eval(file_AN.read())
            file_AN.close()

            if(AN in AN_lst):

                print("Account Detected !")
                print("")

                cust_fil = open(fr"{path}\data\Customer info\{AN}.txt","r")
                cust_dtl = eval(cust_fil.read())
                cust_fil.close()


                while(True):

                    try:

                        pin = int(input("Enter your 4-Digit pin :"))

                        if(pin == cust_dtl["PIN"]):

                            print("Account confirmed !")
                            print("")

                            print("Account Holder's Name :",cust_dtl["Name"])
                            print("Your total Account Balance : Rs.",cust_dtl["Account Balance"])
                            print("")
                            print("")

                            print("Bill Options :")
                            print("")
                            print("1. Electricity Bill")
                            print("2. Gas Bill")
                            print("3. Water Bill")
                            print("4. Internet Bill")
                            
                            
                            while(True):

                                try:
                                    print("")
                                    option = int(input("Select an Option :"))

                                    company = ""

                                    if(option == 1):

                                        print("Receiver Account : K-ELECTRIC")
                                        company = "K-ELECTRIC"

                                    elif(option==2):

                                        print("Receiver Account : SSGC")
                                        company = "Gas"

                                    elif(option==3):

                                        print("Receiver Account : KWSB")
                                        company = "Water"

                                    elif(option==4):

                                        print("Receiver Account : PTCL")
                                        company = "Internet"

                                    else:

                                        print("Invalid Input. Please try again.")
                                        continue       

                                    while(True):

                                        try:

                                            print("")
                                            bill_amount = float(input("Enter Bill Amount : Rs."))

                                            if(bill_amount>0 and bill_amount <= cust_dtl["Account Balance"]):

                                                print(f"Do yo wish to pay Rs.{bill_amount} for your {company} Bill ?")
                                                print("")
                                                print("1. Yes")
                                                print("2. No")

                                                while(True):

                                                    try:

                                                        wish = int(input("Select an Option :"))

                                                        if(wish==1):

                                                            cust_dtl["Account Balance"] -= bill_amount
                                                            print(f"You have successfully paid Rs.{bill_amount} for your {company} Bill.")

                                                            new_cust_fil = open(fr"{path}\data\Customer info\{AN}.txt","w")
                                                            to_write = str(cust_dtl)
                                                            new_cust_fil.write(to_write)
                                                            new_cust_fil.close()      

                                                            # updating SOA file of the customer

                                                            dep_time = time.strftime("%x")
                                                            

                                                            SOA_file = open(fr"{path}\data\Customer SOA\SOA_{AN}","a")
                                                            SOA_to_write = "{0:<15} {1:<30} {2:<20} Rs.{3:<15}\n".format(dep_time,company+" Bill","Debit",bill_amount)
                                                            SOA_file.write(SOA_to_write)
                                                            SOA_file.close()
                                                            
                                                            print("")
                                                            print("Your total Account Balance :",cust_dtl["Account Balance"])
                                                            print("")
                                                            print("")

                                                            back_main = input("Press any key to go to Main Menu :")

                                                            if(back_main or back_main==""):

                                                                print("Back to Main Menu !")
                                                                print("")
                                                                repeater() 

                                                                break

                                                            
                                                        else:

                                                            print("Process terminated.")
                                                            print("")
                                                            print("Back to Main Menu !")
                                                            print("")

                                                            repeater() 
                                                            break

                                                    except:

                                                            print("Invalid input. Choose between 1-2 .")

                                                break

                                            elif(bill_amount > cust_dtl["Account Balance"]):

                                                print("Insufficient Balance !")

                                            else:

                                                print("Invalid Input.")


                                        except:

                                            print("Invalid Input.")

                                    break



                                except:

                                    print("Invalid input. Please choose between 1-4")

                            break


                        else:

                            print("Incorrect PIN.")

                    except:

                        print("Invalid Input. Please try again.")

                break

            else:

                print("Account does not exist.")

            

        except:

            print("Invalid Input. Please try again.")

def SOA_8():

    print("")
    print("")
    print("        * Statement of Account *")
    print("")

    while(True):

        try:
            print("")
            AN = int(input("Enter your Account Number :"))

            file_AN = open(fr"{path}\account numbers.txt","r")
            AN_lst = eval(file_AN.read())
            file_AN.close()

            if(AN in AN_lst):

                print("Account Detected !")
                print("")

                cust_fil = open(fr"{path}\data\Customer info\{AN}.txt","r")
                cust_dtl = eval(cust_fil.read())
                cust_fil.close()


                while(True):

                    try:

                        pin = int(input("Enter your 4-Digit pin :"))

                        if(pin == cust_dtl["PIN"]):

                            print("Account confirmed !")
                            print("")
                            print("")
                            print("")

                            print("Account Holder's Name :",cust_dtl["Name"])
                            print("IBAN : ",cust_dtl["IBAN"])
                            print("Account Balance : Rs.",cust_dtl["Account Balance"])
                            print("")

                            # Getting no of transactions , from no. of lines.  Note: A file cannot be read and readlines at the same time !!

                            SOA_file = open(fr"{path}\data\Customer SOA\SOA_{AN}","r")
                            no_txn = len(SOA_file.readlines())
                            print("No. of Transactions :",no_txn-2)
                            print("")
                            print("")
                            SOA_file.close()

                            # Reading Bank Statement , then printing it

                            SOA_file = open(fr"{path}\data\Customer SOA\SOA_{AN}","r")
                            bank_statement = SOA_file.read()
                            SOA_file.close()

                            print(bank_statement)

                            go_main = input("Press any key to go to main menu :")

                            if(go_main or go_main==""):

                                print("Back to the Main Menu !")

                                repeater()

                            break
                        else:

                            print("Incorrect PIN.")

                    except:

                        print("Invalid Input.")

                break

            else:

                print("Account does not exist.")

        except:

            print("Invalid Input.")

# def admin_9():

#     print("Admin")

    

def digit_count(n):

    count = 0

    while(n>0):

        last = n%10
        n = n//10

        count += 1

    return count


intro()