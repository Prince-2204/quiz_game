import sys , subprocess 

def clear_screen():

    operating_system = sys.platform

    if operating_system == 'win32':
        subprocess.run('cls' , shell = True)
    

print("\t\tWelcome to the quizz\t\t")

file = open("quiz.txt",'a')

name =input("Please Enter Your Name : ")

file.write(f"Name of the Participant: {name}\n")


print("Levels are as follows :\neasy\nmedium\nhard\n")
level = input("Enter the Level of your quizz : ")
if level.lower() == 'easy':
    pass
elif level.lower() == 'medium':
    pass
elif level.lower() == 'hard':
    pass
        
else:
    print("You Haven't enter the correct level")
    quit()
        


file.write(f"Level of Game: {level}\n")

clear_screen()

print("\t\tLet's Begin\t\t")
print("Rules For the game\n1. According to the Level you selcted You will be provided with 5 Questions\n2. For each correct answer you will be awarded with 4 marks")
print("3. For each incorrect answer 2 marks will be deducted")
print("BEST OF LUCK!!")
print("Press Enter to continue")
clear = input()
clear_screen()
score = 0
if level.lower() == 'easy':

    ans = input("1. What is the difference between HTML and CSS?: ")
    if ans.lower() == 'structure and styling':
        score = score + 4
    
    else:
        score = score - 2
    clear_screen()
    ans = input("2.What is the purpose of a 'for' loop in programming? :  ")
    if ans.lower() == 'iteration':
        score = score + 4 
    else :
        score = score - 2
    clear_screen()
    ans = input("3.What is the role of a parameter in a function? :  ")
    if ans.lower() == 'input':
        score += 4
    else:
        score = score - 2
    clear_screen()

    ans = input("4.What is the output of 5 divided by 2? : ")
    if ans.lower() == '2':
        score += 4
    else:
        score = score - 2
    clear_screen()
    
    ans = input("5.What is the file extension for a Python source code file? : ")

    if ans.lower() == '.py':
        score += 4
    else:
        score = score - 2
    clear_screen()



elif level.lower() == 'medium':
    ans = input("1. What is the time complexity of linear search?")
    if ans.lower() == 'linear':
        score = score + 4
    else:
        score = score - 2
    clear_screen()
    ans = input("2.What data structure is typically used to implement a queue?:  ")
    if ans.lower() == 'queue':
        score = score + 4 
    else :
        score = score - 2
    clear_screen()
    ans = input("3.What does the term 'polymorphism' mean in object-oriented programming? ")
    if ans.lower() == 'multiple':
        score += 4
    else:
        score = score - 2
    clear_screen()

    ans = input("4.What does the term 'recursion' refer to in programming? : ")
    if ans.lower() == 'function':
        score += 4
    else:
        score = score - 2
    clear_screen()
    
    ans = input("5.What is the purpose of the 'elif' statement in Python? : ")

    if ans.lower() == 'conditional':
        score += 4
    else:
        score = score - 2
    clear_screen()



elif level.lower() == 'hard':
    ans = input("1. What is the time complexity of a binary search algorithm?: ")
    if ans.lower() == 'logarithmic':
        score = score + 4
    else:
        score = score - 2
    clear_screen()
    ans = input("2.What is the difference between deep copy and shallow copy in Python? :  ")
    if ans.lower() == 'references':
        score = score + 4 
    else :
        score = score - 2
    clear_screen()
    ans = input("3.What is a deadlock in the context of concurrent programming? :  ")
    if ans.lower() == 'deadlock':
        score += 4
    else:
        score = score - 2
    clear_screen()

    ans = input("4.What is the purpose of the 'yield' keyword in Python? : ")
    if ans.lower() == 'generator':
        score += 4
    else:
        score = score - 2
    clear_screen()
    
    ans = input("5.What is the significance of the DRY principle in software development? : ")

    if ans.lower() == 'repetition':
        score += 4
    else:
        score = score - 2
    clear_screen()


else:
    print("Sorry you haven't enter a valid response")
    quit()

clear_screen()
file.write(f"Name: {name} Score: {score}\n")
print(f"Congratulations Dear {name} , Your Scored {score} in the quiz")

clear_screen()
print("Enter yes or no")
ans = input(f"Do you want too see the correct answers: ")
if ans.lower() == 'yes' and level.lower() == 'easy':
    print(f"Question no 1 answer : structure and styling")
    print(f"Question no 2 answer : iteration")
    print(f"Question no 3 answer : input")
    print(f"Question no 4 answer : 2")
    print(f"Question no 5 answer : .py")

elif ans.lower()== 'yes' and level.lower() == 'medium' :
    print(f"Question no 1 answer : linear")
    print(f"Question no 2 answer : queue")
    print(f"Question no 3 answer : multiple")
    print(f"Question no 4 answer : function")
    print(f"Question no 5 answer : conditional")

elif ans.lower() == 'yes' and level.lower() == 'hard' :


    print(f"Question no 1 answer : logarithmic")
    print(f"Question no 2 answer : references")
    print(f"Question no 3 answer : deadlock")
    print(f"Question no 4 answer : generator")
    print(f"Question no 5 answer : repetition")

elif ans.lower == 'no' :
    print("Thank you for playing , Please Visit Again :)")
    quit()

else :
    print("Please enter a valid input")
    quit()






