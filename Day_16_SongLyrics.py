print("Song Lyrics Finisher")
print("Fill in the blank lyrics")
counter = 1
while True:
  song = input("Never going to ____ you up: ")
  if song == "give":
    print("Well done")
    break
  else:
    print("Nope wrong answer, try again")
    counter = counter + 1
print("Thank you for playing you solved it in", counter, "tries")
