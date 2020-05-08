import re
import json

class Person:
    global mood
    healthRate="100%"
    moods=("happy","lazy","tired")

    def __init__(self,name,money):
        self.name=name
        self.money=money
    def sleep(self,hour):
        if(hour>7):
            self.mood=self.moods[1]
        elif(hour<7):
            self.mood=self.moods[2]
        else:
            self.mood=self.moods[0]
    def eat(self,meals):
        if(meals==3):
            healthRate='100%'
        elif(meals==2):
            healthRate='75%'
        elif(meals==1):
            healthRate='50%'
    def buy(self,*items):
        numOfItems=len(items)
        cost=10*(numOfItems)
        self.money-=cost

class Employee(Person):

    def __init__(self,name,money,email,salary,distanceToWork,car,id):
        super(Employee,self).__init__(name,money)
        self.email=email
        regex='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if(re.search(regex,email)):
            pass  
        else:  
            print("Invalid Email")
        self.salary=salary
        if(salary<1000):
            print("salary must be 1000 or more") 
        self.distanceToWork=distanceToWork
        self.car=car
        self.id=id

    def work(self,hour):
        if(hour>8):
            self.mood=self.moods[2]
        elif(hour<8):
            self.mood=self.moods[1]
        else:
            self.mood=self.moods[0]
    
    def drive(self,velocity,distance):
        if(velocity>=0 and velocity<=200):
            self.car.run(velocity,distance)
        else:
            print("velocity must be between 0 and 200") 

    def refuel(self,gasAmount=100):
        self.car.FuelRate=100 
    
    def send_mail(self,to,subject,msg,reciever_name):
        f=open("mail.txt",'w')
        f.write("\nFrom:"+self.email+"\nTo:"+to+"\nSubject:"+subject+"\nHi, "+reciever_name+"\n"+msg+"\nThanks") 
        f.close()  

class Office:
    hiredEmployees={}
    employeesNum=0
    def __init__(self,officeName,employees):
        self.employees=employees
        self.officeName=officeName

    def get_all_employees(self):
        return self.employees
    def get_employee(self,emp_id):
         employee=self.employees[emp_id]
         return employee
    def hire(self,emp):
        self.hiredEmployees[emp.id]=emp.name
        self.employeesNum+=1 
    def fire(self,emp_id):
        self.hiredEmployees.pop(emp_id)
        self.employeesNum-=1 
    @staticmethod     
    def calculate_lateness(targetHour,moveHour,distance,velocity):
        time=(distance/velocity)
        arrival=moveHour+time
        if(arrival>targetHour):
            latency=arrival-targetHour
            print("latency is ",latency," of hour") 
        else:
            print("no latency")     
    def deduct(self,emp_id,deduction):
        employee=self.employees[emp_id]
        print("old salary :",employee.salary," L.E")
        employee.salary-=deduction 
        print("new salary :",employee.salary," L.E") 
    def reward(self,emp_id,rewardVal):
        employee=self.employees[emp_id]
        print("old salary :",employee.salary," L.E")
        employee.salary+=rewardVal 
        print("new salary :",employee.salary," L.E")
    @classmethod
    def changeEmpNum(self,num):
        self.employeesNum=num    
    def saveToJSONFile(self,employee):
        data = {}
        data['employees'] = []
        data['employees'].append({
            'name': employee.name,
            'id': employee.id,
        })
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)

class Car:
    FuelRate=0
    def stop(self,remainDistance):
        velocity=0
        if(remainDistance==0):
            print("you arrived")
        else:
            print("remain distance is",remainDistance)
            self.FuelRate=0
    def run(self,velocity,distanceToWork):
        if(self.FuelRate==0):
            print("No Fuel")
            self.stop(distanceToWork)
        elif(self.FuelRate>=(0.01*distanceToWork)):
            self.FuelRate-=(0.01*distanceToWork)
            self.stop(0)
        elif(self.FuelRate<=(0.01*distanceToWork) and self.FuelRate>0):
            remainDistance=(((0.01*distanceToWork)-self.FuelRate)*100)
            self.stop(remainDistance)
        else:
            print("invalid parameters")
      
#code test >>>>
fiat=Car()      
toyota=Car()

ali=Employee("ali",5000,"sahs@yahoo.com",2000,15,fiat,122)
saad=Employee("saad",10000,"saad@yahoo.com",3000,30,toyota,116)

#ali.refuel()
#ali.drive(100,10005)
saad.send_mail("ali2@yahoo.com","interview","you accepted","ali")
f=open("mail.txt",'r')
#print(f.read())
f.close

emps={}
emps.update({ali.id:ali})
emps.update({saad.id:saad})
 
iti=Office("iti",emps)
iti.hire(saad)
iti.hire(ali)
iti.fire(ali.id)
#iti.fire(saad.id)
#print(iti.hiredEmployees)

#iti.calculate_lateness(9,9,20,100)

#iti.deduct(116,1000)

#try to change employees number manually
#iti.changeEmpNum(5)
#print(iti.employeesNum)

#json test
#iti.saveToJSONFile(saad)
#jsonfile=open("data.txt","r")
#print(jsonfile.read())
#jsonfile.close