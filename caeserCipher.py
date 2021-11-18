import os, time

cipherEncodeText = []
cipherDecodeText = []

def cipherEncode(text, shift):
  alphaLower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

  alphaUpper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

  for i in text:
    if i.islower():
      for x in alphaLower:
        if i == x:
          index = alphaLower.index(i)
          newChar = index + shift
          if newChar <= 25:
            addChar = alphaLower[newChar]
            cipherEncodeText.append(addChar)

          elif newChar > 25:
            getNewIndex =  newChar - 25 - 1
            addChar = alphaLower[getNewIndex]
            cipherEncodeText.append(addChar)

    elif i.isupper():
      for x in alphaUpper:
        if i == x:
          index = alphaUpper.index(i)
          newChar = index + shift
          if newChar <= 25:
            addChar = alphaUpper[newChar]
            cipherEncodeText.append(addChar)
          elif newChar > 25:
            getNewIndex =  newChar - 25 - 1
            addChar = alphaUpper[getNewIndex]
            cipherEncodeText.append(addChar)
          
  
def cipherDecode(text, shift):
  alphaLower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

  alphaUpper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  for i in text:
    if i.islower():
      for x in alphaLower:
        if i == x:
          index = alphaLower.index(i)
          newChar = index - shift
          if newChar <= 25:
            addChar = alphaLower[newChar]
            cipherDecodeText.append(addChar)

          elif newChar > 25:
            getNewIndex =  newChar + 25 + 1
            addChar = alphaLower[getNewIndex]
            cipherDecodeText.append(addChar)

    elif i.isupper():
      for x in alphaUpper:
        if i == x:
          index = alphaUpper.index(i)
          newChar = index - shift
          if newChar <= 25:
            addChar = alphaUpper[newChar]
            cipherDecodeText.append(addChar)
          elif newChar > 25:
            getNewIndex =  newChar + 25 + 1
            addChar = alphaUpper[getNewIndex]
            cipherDecodeText.append(addChar)

run = True
while run:
  userInput = input("Do you want to encode text or decode text? Type encode/decode: ").lower()
  print()
  if userInput == "encode":
    text = input("Enter Some Text To Encode: ")
    shiftPattern = int(input("Enter The Amount You Want To Shift: "))
    cipherEncode(text, shiftPattern)
    print()
    print(''.join(str(x) for x in cipherEncodeText))
    print()
    cipherEncodeText.clear()


  elif userInput == "decode":
    text = input("Enter the encoded text: ")
    shiftPattern = int(input("Enter the shift pattern: "))
    cipherDecode(text, shiftPattern)
    print()
    print(''.join(str(x) for x in cipherDecodeText))
    print()
    cipherDecodeText.clear()
  else:
    os.system("clear")
    run = False
