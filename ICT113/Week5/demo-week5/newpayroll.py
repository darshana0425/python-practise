#Program: Payroll System
#Author: Umesh Poudel
#Date: 13th Aug 2022

def calc_wage(hours_worked):
    hourly_rate=20
    wage=hours_worked * hourly_rate
    return wage;

def print_payroll_summary(employees):
    # print payroll-summary-report
    print(" \n{:^60}\n".format("Payroll Summary"))
    print("{:20}{:20}{:20}".format("Name","Hours","Wage"))
    print("="*60)

    total_wage=0.0
    total_hours=0

    for record in employees:
        name,hours,wage =record.split(",")
        total_hours=total_hours + int(hours)
        total_wage=total_wage + float(wage)

        print("{:20}{:20}${:20}".format(name,hours,wage))

    print("="*60)
    print("{0:>20}{2:3}{1:>17}${3:5}".format("Hours ","Wage ",total_hours,total_wage))


def main():
    #empty list
    employees=[]
    print(" --- Payroll System--- \n")
    
    while(True):
        name=input("Enter employee name:")
        hours=int(input("Enter hours worked:"))
        wage= calc_wage(hours)
        #create a record to add to the employee list from the inputs
        #format: John,20,400
        record = "{},{},{}".format(name,hours,wage)
        #Add to the employees list
        employees.append(record)
        choice=input("\n\nPress (Y or y) to continue,any key to exit ")
        
        if(choice.lower()!='y'):
            break;
            
    print_payroll_summary(employees)
    
main() #call main
