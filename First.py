# temp=open('C:/Users/cl/Desktop/text.txt','a+')
# print(3+1,file=temp)
# temp.close()


# from decimal import Decimal
# print(Decimal('1.1')+Decimal('2.2'))
# presednt=input('大圣想要什么礼物')
# print(presednt,type(presednt))


# s=int(input("请输入一个整数"))
# if s%2==0:
#     print("输入的是偶数")
# else:
#     print("输入的是奇数")

# score=int(input("输入分数"))
# if score>=90 and score<100:
#     print("A")
# elif score>=80 and score<90:
#     print("B")
# elif score>=70 and score<80:
#     print("C")
# elif score>=60 and score<70:
#     print("D")
# elif score>=0 and score<59:
#     print("E")
# else:
#     print("输入数据非法")

# 计算1到100之间的偶数和
# sum=0
# s=1
# while s<=100:
#     if s%2==0:
#         sum+=s
#     s+=1
# print(sum)

#for循环计算1到100之间的偶数和
# sum=0
# for i in range(1,101):
#     if i%2==0:
#         sum+=i
# print(sum)

#输入三次密码退出
# s=0
# while s<3:
#     pwd=input("请输入密码")
#     if pwd=="123":
#         print("密码输入正确")
#         break
#     else:
#         print("密码输入不正确")
#         s+=1

#输入1到50之间所有5的倍数
# for i in range(1,51):
#      if i%5!=0:
#          continue
#      else:
#         print(i)

#输出一个三行四列的矩形
# for _ in range(1,4):
#     for _ in range(1,5):
#         print("*",end="\t")#不换行输出
#     print("")


#打印三角形
#打印九九乘法表
for l in range(1,10):
    for _ in range(1,l+1):
        print(l,"*",_,"=",l*_,end="\t")
    print("")