"""
Pyhton For Web applications ITEC320
Lab Work-1
Name : Fahri Han Pınar
Std Number:19000134
"""

name = input(str("What is your name please enter it."))
greetings = (f"Welcome {name}")
work_exp=input(str("How many years work experience year you have ?"))
saying_exp=(f"Your work experiance is {work_exp} years")
print(greetings)
print("Your work experience is : ",work_exp)
b_salary = 2500
i=0

temp = work_exp
work_exp = int(temp)
temp = work_exp

b_salary_temp= b_salary


xtemp=0;

xtemp = work_exp/2




while i<xtemp:
    if work_exp%2==0:
        b_salary+=b_salary*20/100
        #print(b_salary)
        i=i+1


    elif work_exp%2==1:
        work_exp=work_exp-1
        #print(b_salary)
        i=i + 1

print("Year  |  Salary  |  Yearly Income")

print("%d     |  %d  |   {:.2f}".format(b_salary) % (temp, b_salary_temp))




