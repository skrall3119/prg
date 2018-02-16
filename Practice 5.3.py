def main(): #assigns functions to variables and prints results from the fuctions
    actualValue = getValue()
    assessmentValue = calculateAssessmentValue(actualValue)
    propertyTax = findPropertyTax(assessmentValue)

    print("The assessment value of your home is: $" + format(assessmentValue, ',.2f'))
    print("The property tax on your home is: $" + format(propertyTax, ',.2f'))

def getValue(): #asks the user for input 
    actualValue = float(input("Enter the actual value of your property. "))
    return actualValue

def calculateAssessmentValue(houseValue): #calculates the assessment value using the value provided by the user
    assessmentValue = houseValue * .6
    return assessmentValue

def findPropertyTax(assessmentValue): #calculates property tax based on the value of calculateAssessmentValue
    x =  assessmentValue / 100
    propertyTax = .72 * x
    return propertyTax

main()
