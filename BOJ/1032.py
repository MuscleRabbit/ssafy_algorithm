N = int(input())

strings = list();

for _ in range(N):
  strings.append(input())

pattern = str();

for i in range(len(strings[0])):
  char = set();
  for j in range(N):
    char.add(strings[j][i]);
  if len(char) == 1:
    pattern += char.pop()
  else:
    pattern += '?'

print(pattern)