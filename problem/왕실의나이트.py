userinput = input()
row = "abcdefgh"
col = "12345678"
x = ord(userinput[0])-97
y = int(userinput[1])-1

chess=[
  "23444432",
  "34666643",
  "46888864",
  "46888864",
  "46888864",
  "46888864",
  "34666643",
  "23666632"]

print(chess[y][x])
