data = []
count = 0
with open('reviews.txt', 'r') as f :
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: # %求餘數 1000 的倍數才會印出來
            print(len(data))
print('檔案讀取完, 總共有', len(data), '比資料')

sum_len = 0 #算出留言的平均長度
for d in data: #每一筆資料稱為d data為清單
   sum_len += len(d)

print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
   if  len(d) < 100:
       new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])

# good = [d for d in data if 'good' in d ]
# bad = ['bad' in d for d in data]
# bad = []    
# for d in data;
#   bad.append('bad' in d)
# list comprehension


# 文字記數
wc = {} #word_count
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增新的Key進wc字典

for word in wc:
	if wc[word] > 100000:
	    print(word, wc[word])

print(len(wc))

while True:
    word = input('請問你想查甚麼字: ')
    if word == 'End':
    	break
    if word in wc:
        print(word, '出現過的次數為', wc[word])
    else:
        print('') 
print ('感謝使用此功能') 


    
















