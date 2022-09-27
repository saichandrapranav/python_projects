print("hello welcome to rock paper scissors game.")

rock = "rock"
paper = "paper"
scissor = "scissor"
score = 0
count = 0

while count < 6:
    n = input("Enter anything between rock,paper,scissor ")
    if n == "rock":
        print("rock")
        score += 1
        count += 1


    elif n == "paper":
        print("paper")
        score += 1
        count += 1

    else:
        print("scissors")
        score +=1
        count += 1

    if count == 6:
        break
    else:
        continue

print(score)