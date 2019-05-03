import csv

with open("st.txt", "r", encoding = "utf-8") as f:
    print(f.read())

answer = input("何か入力してください：")
with open("answer.txt", "w", encoding = "utf-8") as f:
    f.write(answer)

with open("movie.csv", "w", encoding = "utf-8") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["Top Gun", "Risky Business", "Minority Report"])
    w.writerow(["Titanic", "The Revenant", "Inception"])
    w.writerow(["Training Day", "Man on Fire", "Flight"])
    w.writerow(["トップガン", "卒業白書", "マイノリティ・リポート"])
    w.writerow(["タイタニック", "レヴェナント", "インセプション"])
    w.writerow(["トレーニング デイ", "マイ・ボディガード", "フライト"])

movies1 = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movies1.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies1:
        spamwriter.writerow(movie_list)

movies2 = [["トップガン", "卒業白書", "マイノリティ・リポート"], ["タイタニック", "レヴェナント", "インセプション"], ["トレーニング デイ", "マイ・ボディガード", "フライト"]]
with open("movies2.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies2:
        spamwriter.writerow(movie_list)
