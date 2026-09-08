Name = input("Enter your name: ")
print(f"\n Welcome {Name}!")
print("You are about to begin your GNS 101 test.")
print("Kindly Answer all Questions using the options")
print("GOOD LUCK!")

Questions = [
    'Who is the President of Nigeria? a)Muhammadu Buhari b)Bola Tinubu c)Goodluck Jonathan d)Olusegun Obasanjo',

    'What is the capital of Nigeria? a)Lagos b)Ibadan c)Abuja d)Kano',

    'How many states are there in Nigeria? a)30 b)36 c)37 d)40',

    'Which planet is known as the Red Planet? a)Earth b)Venus c)Mars d)Jupiter',

    'What is 10 + 15? a)20 b)25 c)30 d)35',

    'Which of these is a programming language? a)Python b)Google c)Windows d)Facebook',

    'What does CPU stand for? a)Central Processing Unit b)Computer Personal Unit c)Central Program Utility d)Computer Processing User',

    'Which device is used for typing on a computer? a)Monitor b)Keyboard c)Printer d)Speaker',

    'How many days are there in a normal year? a)300 b)365 c)366 d)400',

    'Which continent is Nigeria located in? a)Asia b)Europe c)Africa d)America',

    'What is 100 divided by 4? a)20 b)25 c)30 d)40',

    'Which of these is an operating system? a)Windows b)Google c)YouTube d)Facebook',

    'What is the opposite of hot? a)Warm b)Cold c)Heat d)Fire',

    'Which animal is known as the king of the jungle? a)Tiger b)Lion c)Elephant d)Leopard',

    'What does RAM stand for? a)Random Access Memory b)Read Access Machine c)Rapid Application Memory d)Random Application Manager'
]

Answer =  ['b', 'c', 'b', 'c', 'b', 'a', 'a', 'b', 'b', 'c', 'b', 'a', 'b', 'b', 'a']

score =0

for number, (ques, ans) in enumerate(zip(Questions, Answer),1):
    print(f"{number}.{ques}")
    user = input('Answer:').lower().strip()
    if user == ans:
        score += 1
        print("Correct !")
    else:
        print("Wrong !")



print("Total=", score)

print("\n ================")
print("    FINAL RESULT")
print("=================")

print(f"Student: {Name}")
percentage = (score/ len(Questions)*100)
print(f"percentage {percentage:.0f}%")
if percentage >= 50:
    print("Passed")
else:
    print("Failed")

    with open("results.txt", "a") as file:
        file.write(
        f"Student: {Name} | "
        f"Score: {score}/{len(Questions)} | "
        f"Percentage: {percentage:.0f}% | "
    )

