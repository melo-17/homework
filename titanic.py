f = open("train.csv", "r")
list_of_p = f.readlines()
f.close()

all_passengers_count, men_survived, women_survived = 0, 0, 0
a = []
for i in range(1, len(list_of_p)):
    a = list_of_p[i].strip().split(',')
    if a[1] == "1" and a[5] == "male":
        men_survived += 1
    if a[1] == "1" and a[5] == "female":
        women_survived += 1
print("Количество выживших мужчин - ", men_survived,
      "Количество выживших женщин - ", women_survived)
