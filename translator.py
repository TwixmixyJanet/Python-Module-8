translations = {
  "hello":"hola",
  "thank you":"gracias",
  "sorry":"lo siento"
}

done = False

while not done:
  word = input("enter an english word:")
  word = word.lower()
  
  if word == "done":
    done == True
  elif word in translations:
    print(translations[word])
  else:
    print("that word is not in the dictionary")
    
  