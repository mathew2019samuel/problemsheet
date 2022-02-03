#open a new file called 'pythonbmi.py'
#need to find the bmi of person with inputs (weight & height)
#Author : Mathew Samuel


#used int to instruct the system that it is an integer
weight = int(input('Enter your weight (kg): ' ))
height = int(input('Enter your height (cm): '))
#converting cm to m2 and dividing weight with height
BMI=weight/ (height/100)**2
print('Your BMI is {}'.format(BMI))