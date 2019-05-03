dramas = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]

for drama in dramas:
    print(drama)

for num in range(25, 51):
    print(num)

numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")

num1 = [8, 19, 148, 4]
num2 = [9, 1, 33, 83]
num3 = []

for i in num1:
    for j in num2:
        num3.append(i * j)

print(num3)
