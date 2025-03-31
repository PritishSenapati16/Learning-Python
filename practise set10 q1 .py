# Q1 --- Create a class "Programmer" for storing informaton of few programmers working at Microsoft.

# Ans ---
# signing in 
class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,adress):
        self.name = name
        self.salary = salary
        self.adress = adress

p = Programmer("Sumit" , 120000 , "Badambadi cuttack")
print(p.name,p.salary,p.adress,p.company)

p = Programmer("Pritish" , 160000 , "Tulsipur cuttack")
print(p.name,p.salary,p.adress,p.company)

p = Programmer("Tushar" , 130000 , "Puri badadanda")
print(p.name,p.salary,p.adress,p.company)

print("End of program") 
# signing off 


    