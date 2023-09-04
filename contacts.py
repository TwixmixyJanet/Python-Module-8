people = ["Ann", "Chelsea", "Nichole", "Max"]
title = ["Marketing Coordinator", "Software Developer", "Sales Representative", "Technical Writer"]

# Empty dictionary to add to
company_org = {}

#Use lists to add people and roles to company_org dictionary
for i in range(len(people)):
  person = people[i]
  person_title = title[i]
  company_org[person] = person_title

print(company_org)