#15 human years == first year of med-size dog
#year two for a dog == 9 human years
#after that, each human year == 5 dog years** make note that this is APPROX

#according to American Kennel Association, a small dog will age 4 years each
#year starting at age 3

#for medium and big dogs, they age approx 5 years for each human year
#starting at age 3

#for giant dogs, they age approx 7 years for each human year

#figure out dog age in human years

#get dog weight from user
def getWeight():
    weight = int(input("How much does your dog weigh? "))
    return weight

#get dog age from user
def getAge():
    age = int(input("How old is your dog? "))
    return age

def youngDog(age):
    if age == 1:
        humanAge = 15
    elif age == 2:
        humanAge = 24
    printResult(humanAge)
    runAgain()

#calculate age of a small dog
#assumes rate of 4 human years to every dog year
def smallDog(age):
    count = 0
    if age >= 3:
        for x in range(3, age):
            count += 1
        humanAge = 28 + (4 * count)
    return humanAge

#calculate age of a med to lrg dog
#assumes rate of 5 human years to every dog year
def medToLrgDog(age):
    count = 0
    if age >=3:
        for x in range(3, age):
            count += 1
        humanAge = 28 + (5 * count)
    return humanAge

#calculate age of a giant dog
#assumes rate of 7 human years to every dog year
def giantDog(age):
    count = 0
    if age == 1:
        humanAge = 12
    elif age == 2:
        humanAge = 22
    elif age == 3:
        humanAge == 31
    elif age >=4:
        for x in range(3, age):
            count += 1
        humanAge = 28 + (7 * count)
    printResult(humanAge)
    runAgain()

#prompt user to run again
def runAgain():
    again = input("Run again? y/n: ").lower()
    while again == "n":
        print("goodbye!")
        break
    else:
        print("restarting program...")
        main()

#calculate age based on weight range
def calculateAge(weight, age):
    if age <= 0 :
        print("0 is not valid. try again.")
        runAgain()
    elif age >= 1 and age <= 2 and weight <100:
        youngDog(age)
    elif age == 1 or age == 2 and weight >=100:
        giantDog(age)
    else:
        #for dogs >2 years age
        if weight <=20:
            age = smallDog(age)
        if weight >20 and weight <=99:
            age = medToLrgDog(age)
        if weight >=100:
            age = giantDog(age)
        printResult(age)
        runAgain()
        # return age

def printResult(age):
    if age >=0 and age <=18:
        ageClass = " puppy"
    elif age >=19 and age <=50:
        ageClass = "n adult"
    else:
        ageClass = " senior citizen"
    print("In human years, your dog is approximately {} years old and is a{}.".format(age,ageClass))

#main function to run methods
def main():
    weight = getWeight()
    age = getAge()
    calculateAge(weight, age)

main()
