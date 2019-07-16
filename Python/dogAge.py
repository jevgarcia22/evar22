#get dog weight from user
def getWeight():
    #TODO: input validation
    return int(input("How much does your dog weigh? "))

#get dog age from user
def getAge():
    #TODO: input validation
    return int(input("How old is your dog? "))

def youngDog(age):
    if age == 1:
        humanAge = 15
    elif age == 2:
        humanAge = 24
    elif age == 1 and weight >=100:
        humanAge = 12
    elif age == 2 and weight >=100:
        humanAge = 22
    return humanAge

#calculate age of a small dog
#assumes rate of 4 human years to every dog year
def smallDog(age):
    count = 0
    for x in range(3, age):
        count += 1
    return 28 + (4 * count)

#calculate age of a med dog
#assumes rate of 5 human years to every dog year
def medDog(age):
    count = 0
    for x in range(3, age):
        count += 1
    return 28 + (5 * count)

#calculate age of a lrg dog
#assumes rate of 6 human years to every dog year
def lrgDog(age):
    count = 0
    for x in range(3, age):
        count += 1
    return 28 +(6 * count)

#calculate age of a giant dog
#assumes rate of 7 human years to every dog year
def giantDog(age):
    count = 0
    if age == 1:
        return 12
    elif age == 2:
        return 22
    elif age == 3:
        return 31
    elif age >=4:
        for x in range(3, age):
            count += 1
        return 31 + (7 * count)

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
def calculateAge():
    age = getAge()
    weight = getWeight()
    #TODO: use input validation for this
    if age <= 0 :
        print("0 is not valid. try again.")
        runAgain()
    elif age == 1 or age == 2:
        humanAge = youngDog(age)
    elif age >=3:
        if weight <=20:
            humanAge = smallDog(age)
        if weight >20 and weight <=50:
            humanAge = medDog(age)
        if weight >50 and weight <=100:
            humanAge = lrgDog(age)
        if weight >100:
            humanAge = giantDog(age)
    printResult(humanAge)
    runAgain()

#print results
def printResult(age):
    if age >=0 and age <=18:
        ageClass = " puppy"
    elif age >=19 and age <=50:
        ageClass = "n adult"
    else:
        ageClass = " senior citizen"
    print("In human years, your dog is approximately {} years old and is a{}.".format(age,ageClass))


def main():
    print("How Old Is My Dog In Human Years?")
    print("Input the weight and age of a dog. This program will determine the approximate age in human years.")
    calculateAge()


if __name__ == "__main__":
    main()
