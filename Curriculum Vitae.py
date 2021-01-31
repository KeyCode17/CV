import datetime
import os
import time
import random

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
todayyear = int(now.strftime("%Y"))
agenowdate = todaydate - date_birth
agenowmonth = todaymonth - month_birth
agenowyear = todayyear - year_birth
agenow = todayyear - year_birth - 1

if agenowyear >= 0:
    if agenowmonth == 0:
        if todaydate >= 17:
            agenow = int(agenow)
            agenow += 1
            agenow = str(agenow)
    if agenowmonth >= 1:
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
my_experience1 = dapoer + ' Front End Web Developer'
my_experience2 = school + ' ' + city + ' as Photography Educator'
graduate = 2019
expertise_List = ('Phtography', 'Adobe Series', 'Microsoft word', 'Python', 'HTML', 'CSS', 'Java Script', 'Node.js', 'ReactJS')
myemail = "m.daffa.karyudi@gmail.com"
myinstagram = "daffakaryudi"
mygithub = "KeyCode17"
#------FUNCTION LIST------FUNCTION LIST------FUNCTION LIST------#-
def clear():
    os.system('cls')

def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end=" ")
        time.sleep(1)
        t -= 1

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
    print("What i used in this job   : " + str(expertise_List[4:]))
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
    print("My Github      : " + mygithub)
    print('\n')

def Calculator():
    try:
        clear()
        print('\n')
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

        while True:
        # Take input from the user
            choice = input("Enter choice(1/2/3/4): ")

        # Check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):
                print('\n')
                num1 = float(input("Enter first number: "))
                print('\n')
                num2 = float(input("Enter second number: "))
                print('\n')
                num3 = num1

                if choice == '1':
                    num3+=num2
                    print(num1, "+", num2, "=", num3)
                    countdown(int(3))
                    break

                elif choice == '2':
                    num3-=num2
                    print(num1, "-", num2, "=", num3)
                    countdown(int(3))
                    break

                elif choice == '3':
                    num3*=num2
                    print(num1, "*", num2, "=", num3)
                    countdown(int(3))
                    break

                elif choice == '4':
                    num3/=num2
                    print(num1, "/", num2, "=", num3)
                    countdown(int(3))
                    break
            else:
                print("Invalid Input")
    except:
        print("Number Only!")
        countdown(int(3))
def gameguess():
        try:
            print("\n\nWelcome To Guess Number")
            print("choose Range")
            x = int(input("from : "))
            y = int(input("Until : "))
            guessit = random.randrange(x, y)
            clear()
            chances = int(input("\nChances To Guess : "))
            chances = str(chances)
            clear()
            print("\nChances Left : " + chances)
            while True:
                guess = int(input("Please enter your guess : "))


                if guess == guessit:
                    print("\nCongratulations" + gender + yournamedone)
                    countdown(int(5))
                    break
                elif guess < guessit:
                    print("\nWrong guess, too low")
                    chances = int(chances)
                    chances-= 1
                    chances = str(chances)
                    print("\nChances Left : " + chances)
                    if chances == 0:
                        clear()
                        print("\nYou Lose")
                        guessit = str(guessit)
                        print("The Answer is : " + guessit)
                        countdown(int(5))
                        break
                    elif chances != 0:
                        continue
                elif guess > guessit:
                    print("\nWrong guess, too high")
                    chances = int(chances)
                    chances-= 1
                    chances = str(chances)
                    print("Chances Left : " + chances)
                    if chances == 0:
                        clear()
                        print("\nYou Lose")
                        guessit = str(guessit)
                        print("The Answer is : " + guessit)
                        countdown(int(5))
                        break
                    elif chances != 0:
                        continue
        except:
            print("Number Only!")
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
        time.sleep(2)
        print('\n')

while True:
    clear()
    print('\n')
    print(TODAY)
    print("Hallo " + gender + yournamedone)
    print("\nABOUT ME :")
    aboutmyself()
    wanttoknow = str(input("What you want to know : \n1.About my academic background \n2.About my experience \n3.My Contact \n4.My website \n5.Disclaimer\n6.Calculator \n7.Game Guess Number \n8.Exit \nQuestion number "+ increase + ": "))
    print('\n')

    if wanttoknow == "1":
        increase = int(increase)
        increase += 1
        increase = str(increase)
        academic_background()
        time.sleep(7)
        countdown(int(3))
        continue

    if wanttoknow == "2":
        increase = int(increase)
        increase += 1
        increase = str(increase)
        exp()
        time.sleep(9)
        countdown(int(3))
        continue

    if wanttoknow == "3":
        increase = int(increase)
        increase += 1
        increase = str(increase)
        mycontact()
        time.sleep(3)
        countdown(int(3))
        continue

    if wanttoknow == "4":
        increase = int(increase)
        increase += 1
        increase = str(increase)
        print('\n'*3)
        print("Sorry in progres")
        countdown(int(3))
        continue

    if wanttoknow == "5":
        increase = int(increase)
        increase += 1
        increase = str(increase)
        print("© 2020 MOCHAMMAD DAFFA PUTRA KARYUDI ALL RIGHTS RESERVED")
        countdown(int(3))
        continue

    if wanttoknow == "6":
        clear()
        increase = int(increase)
        increase += 1
        increase = str(increase)
        Calculator()
        clear()
        continue

    if wanttoknow == "7":
        clear()
        increase = int(increase)
        increase += 1
        increase = str(increase)
        gameguess()
        clear()
        continue

    if wanttoknow == "8":
        clear()
        print('\n')
        print("question been asked : " + increase)
        print('\n')
        print("Thank you " + gender + yournamedone)
        time.sleep(3)
        countdown(int(3))
        break
        quit()

    else:
        print('\n')
        print('Sorry wrong input [example "1"] ')
        print('\n')
        time.sleep(1)
        countdown(int(3))
        clear()
