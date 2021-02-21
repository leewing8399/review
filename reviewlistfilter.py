data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)    	# 读取文档
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('档案读取完了，总共有' , len(data), '笔资料')        	#len 看一看清单DATA里装了多少东西

# print(data)                 	#打印全部	
# print(data(0))					打印第一句			

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)        #读一笔后就加入，总和 
	#print(sum_len)                   每一笔留言都加上去的数值

	# 求平均，总长度除以每一笔长度data的长度
print('留言的平均长度为',sum_len/len(data))


# 56 清单筛选
new =[]
for d in data:
	if len(d) < 100:
		new.append(d)
		 # 每一条留言为d ,如果留言的长度有小于100放入清单new.

print('一共有', len(new),'笔留言长度小于100') # len(new)得出几笔资料

print(new[0])


 