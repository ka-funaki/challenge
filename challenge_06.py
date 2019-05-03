camus = "カミュ"

print(camus[0])
print(camus[1])
print(camus[2])

input1 = input("何を:")
input2 = input("誰に:")

print("私は昨日{}を書いて、{}に送った！".format(input1, input2))

aldous = "aldous Huxley was born in 1894"

print(aldous.capitalize())

question = "どこで？　だれが？　いつ？"
question = question.split()
print(question)

fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox[0:6])+fox[6]
print(fox)

scream = "A screaming comes across the sky."
scream = scream.replace("s", "$")
print(scream)

hemingway = "Hemingway"
print(hemingway.index("m"))

print("あいう\"え\"お")

three1 = "three " + "three " + "three "
three2 = "three " * 3

print(three1)
print(three2)

april = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
print(april[:11])
