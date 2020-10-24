import datetime
import os
import time

now = datetime.datetime.now()

TODAY = now.strftime("%d-%B-%Y")
increase = "1"
yourname = str(input("\n\nHallo what's your name: "))
yourname1 = yourname[0]
yourname2 = yourname[1:]
yournameup = yourname1.upper()
yournamelower = yourname2.lower()
yournamedone = yournameup + yournamelower
#-------date----------date---------------date-----------------date---------#
date_birth = 17
month_birth = 9
month_txt_birth = 'September'
year_birth = 2001
todaydate = int(now.strftime("%d"))
todaymonth = int(now.strftime("%m"))
todayyear = int(now.strftime("%y"))
agenowdate = todaydate - date_birth
agenowmonth = todaymonth - month_birth
agenowyear = todayyear - year_birth
agenow = 19

if agenowyear >= 0:
    if todaymonth >= 0:
        if todaydate == 0:
            agenow = int(agenow)
            agenow += 1
            agenow = str(agenow)
        if todaymonth >= 1:
        agenow = int(agenow)
        agenow += 1
        agenow = str(agenow)
            
date_of_birth = str(date_birth) + ' ' + str(month_txt_birth) + ' ' + str(year_birth)

#--------ABOUT ME---------ABOUT ME-------ABOUT ME-------ABOUT ME------#
my_full_name = 'Mochammad Daffa Putra Karyudi'
my_nickname = 'Daffa'
city = 'Malang'
nation = 'Indonesia'
place_of_birth = city + ',' + nation
lived_in = city + ',' + nation
dapoer = 'Dapoer Mamajo'
school = 'SMAN 7'
my_gender = 'Male'
my_experience1 = dapoer + ' as staff it'
my_experience2 = school + ' ' + city + ' as photography educator'
graduate = 2019
expertise_List = ('Phtography', 'Adobe Series', 'microsoft word', 'Python', 'C#', 'HTML', 'CSS', 'Java Script', 'C/C++')
myemail = "m.daffa.karyudi@gmail.com"
myinstagram = "daffakaryudi"
#------FUNCTION LIST------FUNCTION LIST------FUNCTION LIST------#-
def clear():
    os.system('cls')

def aboutmyself():
    myname()
    mygender()
    age()
    placeofbirth()
    livedin()
    print('\n')
    
def myname():
    print("My name        : " + my_full_name + " (" + my_nickname + ")")

def placeofbirth():
    print("Birth place    : " + place_of_birth)

def mygender():
    print("Gender         : " + my_gender) 

def livedin():
    print("Lived in       : " + lived_in)

def exp():
    print('\n')
    print(my_experience1)
    print("What i used in this job   : " + str(expertise_List[0:3]))
    print('\n')
    print(my_experience2)
    print("What i used in this job   : " + str(expertise_List[0:3]))
    print('\n')
    print("My coding language        : \n" + str(expertise_List[3:]))
    print('\n')

def age():
    print("Date of birth  : " + date_of_birth)
    print("My age         : " + str(agenow) + ' years old')

def academic_background():
    print('\n')
    print("Graduate in High School within 3 years (2016 - 2019)")
    print(school + " " + city + " science")
    print('\n')
    print("Graduate in Junior High School within 3 years (2013 - 2016)")
    print("SMP Muhammadiyah 2 " + city)
    print('\n')
    print("Graduate in Elementary School within 6 years (2007 - 2013)")
    print("SDN Lowokwaru 1 " + city)
    print('\n')

def mycontact():
    print('\n')
    print("My email       : " + myemail)
    print("My instagram   : " + myinstagram)
    print('\n')
        
        
while True:
    clear()
    genderchooseRandom = str(input("\nare you male or female"'\n\n'"m for male"'\n'"f for female"'\n'"choose here :"))
    genderchoose = genderchooseRandom.lower()
    if genderchoose == "m":
        gender = "Mr."
        print('\n')
        clear()
        break
    
    if genderchoose == "f":
        gender = "Mrs."
        print('\n')
        clear()
        break
    
    else :
        print('\nSorry wrong input [example"M"]')
        time.sleep(5)
        print('\n')

while True:
    print(TODAY)
    print("Hallo " + gender + yournamedone)
    print('\n')
    print("ABOUT ME :")
    aboutmyself()
    wanttoknow = str(input("What you want to know : \n1.About my academic background \n2.About my experience \n3.My Contact \n4.My website \n5.Disclaimer\n6.Exit \nQuestion number "+ increase + ": "))
    print('\n')
    clear()
    
    if wanttoknow == "1":
        increase = int(increase)
        increase += 1
        increase = str(increase)
        academic_background()
        time.sleep(10)
        continue
        
    if wanttoknow == "2":
        increase = int(increase)
        increase += 1
        increase = str(increase)
        exp()
        time.sleep(12)
        continue
        
    if wanttoknow == "3":
        increase = int(increase)
        increase += 1
        increase = str(increase)
        mycontact()
        time.sleep(5)
        continue
    
    if wanttoknow == "4":
        increase = int(increase)
        increase += 1
        increase = str(increase)
        print('\n'*3)
        print("Sorry in progres")
        time.sleep(2)
        continue
    
    if wanttoknow == "5":
        increase = int(increase)
        increase += 1
        increase = str(increase)
        print("© 2020 MOCHAMMAD DAFFA PUTRA KARYUDI ALL RIGHTS RESERVED")
        time.sleep(3)
        
    if wanttoknow == "6":
        Print("Thank you " + gender + yournamedone)
        time.sleep(4)
        break

    else:
        print('\n')
        print('Sorry wrong input [example "1"] ')
        print('\n')
        time.sleep(3)
        clear()
