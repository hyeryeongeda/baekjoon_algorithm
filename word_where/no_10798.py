words = [input() for i in range(5)] # 5개의 단어를 입력

result = ''
max_len = max(len(word) for word in words)
for i in range(max_len):
  for j in range(5) :
    if(i < len(words[j])):
      result += words[j][i]

print(result)