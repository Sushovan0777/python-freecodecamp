def arithmetic_arranger(problems,show_answers=False):
    n=0
    result_numbers1 = []
    result_numbers2 = []
    operators = []
    for item in problems:
        num1,operator,num2=item.split()
        result_numbers1.append(num1)
        result_numbers2.append(num2)
        operators.append(operator)
   # print(result_numbers2,'\n',result_numbers1,'\n',operators)
           
    #print(operators)
    expression=vertical_arranger(result_numbers1,result_numbers2,operators,show_answers)
    print(expression)
def max_length(num1,num2):
    num1=str(num1)
    num2=str(num2)
    if len(num1)>len(num2):
        return len(num1)
    elif len(num2)>len(num1):
        return len(num2)
    elif len(num1)==len(num2):
        return len(num1)
def vertical_arranger(num1,num2,operator,show_answer=False):
    top=""
    bottoms =""
    banners =""
    answers =""
    for i in range(len(num1)):
        max=max_length(num1[i],num2[i])
        if len(num1[i])>=len(num2[i]):
            top+='  '+num1[i]
        else:
            space=2+len(num2[i])-len(num1[i])
            top+=' '*space+num1[i]
        if len(num2[i])>=len(num1[i]):
            bottoms+=operator[i]+' '+num2[i]
        else:
            space=len(num1[i])-len(num2[i])
            bottoms+=operator[i] + ' ' + ' '*space + num2[i]
        banners+='-'*(max+2)
        top+='    '
        bottoms+='    '
        banners+='    '
    if show_answer:
        for i in range(len(num1)):
            max=max_length(int(num1[i]),int(num2[i]))
            digits=max+2
            if operator[i] == "+":
                answer =int(num1[i])+int(num2[i])
            
            else:
                answer =int(num1[i])-int(num2[i])   
            space = digits - len(str(answer))
            answers+=' '*space+str(answer)+'    '
        format=f"{top}\n{bottoms}\n{banners}\n{answers}"
    else:
        format=f"{top}\n{bottoms}\n{banners}\n"

    return format
def tester(problems):
    if len(problems) > 5:
        print("Error: Too many problems.")
        return False
    for problem in problems:
        problem = problem.split(" ")
        if problem[1] not in ['+','-']:
            print("Error: Operator must be '+' or '-'.")
            return False
        elif len(problem[0]) > 4 or len(problem[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return False
        
        # Type Validation. Can only be integer.
        try:
            problem[0] = int(problem[0])
            problem[2] = int(problem[2])
            
        except ValueError:
            print("Error: Numbers must only contain digits.")
            return False
    return True
def main():
    problems_example=["32 + 698", "3801 - 2", "45 + 43", "123 + 49"] 
    problems=[] 
    print("Enter the problems as shown in the example\n(Rules:\t1.number of problem should be less than 5\n\t2. Numbers cannot be more than four digits.\n\t3.Operator must be '+' or '-'.)\n\t4.After every numbers and operator space should be given.")
    print("Example:",problems_example,'\n')
    choice='y'
    while choice=='y':
        problem=input("Enter the problem: ")
        problems.append(problem)
        choice=input("Do you want to enter more problems?(y/n): ")
        if choice=='n':
            break
    if len(problems)==0:
        print("No problem entered.") 
    choice=input("do you wnat to show the answers(y/n)") 
    if tester(problems):    
        if choice=='y':
            arithmetic_arranger(problems,True)
        else:
            arithmetic_arranger(problems)
if __name__ == "__main__":
    main()