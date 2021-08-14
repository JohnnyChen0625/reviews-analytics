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

	
