def reverseWords(input):
  inputWords = input.split(" ")
  inputWords = inputWords[-1::-1]

  output = " ".join(inputWords)
  return output

def reverseWord(input):
  output = input[-1::-1]
  return output

if __name__ == "__main__":
  input = "I like Python"
  rws = reverseWords(input)
  print(rws)
  rw = reverseWord(input)
  print(rw)