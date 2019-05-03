print("aaa")
print("bbb")
print("ccc")

x = 100

if x < 10:
    print("10未満")
else:
    print("10以上")

if x <= 10:
    print("10以下")
elif x <= 25:
    print("25以下")
else:
    print("25より大きい")

y = 3

print(x%y)

print(x//y)

age = 4

if age == 29:
    print("同い年！")
elif age < 29 and age >=20:
    print("若い！")
elif age > 29:
    print("先輩！")
else:
    print("子供！")
