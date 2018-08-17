#给一个正整数，要求:求它是几位数以及逆序打印出各位数字

##def fun(i,nnn):
##      if i==0:
##            print("这个数是%d位数"%nnn)
##            return
##      print(i%10,end=" ")
##      i=int(i/10)
##      nnn+=1
##      fun(i,nnn)
##i = int(input("请输入一个正整数"))
##fun(i,0)
#运用递归的思想很容易解决这个问题，不断的取最后一个数字，重复这个过程，最后就可以将位数算清楚

#一个正整数，判断它是不是回文数(正读和反读都是一样的)

##def fun(num):
##      flag=0
##      num=str(num)
##      j=int(len(num)/2)
##      for i in range(0,j):
##            if num[i]!=num[len(num)-1-i]:
##                  flag =1
##      if flag == 1:
##            print("不是一个回文数")
##      else:
##            print("是一个回文数")
##while True:
##      a =int(input("请输入一个正整数"))
##      if a==-1:
##            break
##      fun(a)
      
       


