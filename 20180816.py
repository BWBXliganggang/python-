

#######一个整数，加上100后是一个完全平方数，加上168之后又是一个..，该数为多少？
##while true:
##      if math.sqrt(num+10)-int(math.sqrt(num+100)) ==0 and ....:
##            print()
##            break



###########给出年月日，如何算出这是这年的第几天(可以直接用专门的模块解决）
##
##def leap(Year):
##      if (Year%4==0 and Year%100!=0) or Year%400==0:
##            return 1
##      else:
##            return 0
##      
##
##year = int(input("请输入年:"))
##month = int(input("请输入月:"))
##day = int(input("请输入日:"))
##
##tianshu=[31,28,31,30,31,30,31,31,30,31,30,31]
##days = 0
##for i in range(month-1):
##      days=days+tianshu[i]
##days=days+leap(year)+day
##print(days)


###########判断一个范围内有多少的素数，不考虑效率和复杂度的情况下，每次迭代都是
          #迭代至这个数的前一个数。考虑效率的话，每次迭代到这个数的平方根
##from math import sqrt
##def main():
##      for i in range(10,301):
##            flag=1
##            a = int(sqrt(i))
##            for j in range(2,a+1):
##                  if i%j==0:
##                        flag=0
##                        break
##            if flag ==1:
##                  print(i)
##
##if __name__ == "__main__": #判断是否直接在运行该.py文件 
##      main()


##将一个正整数分解质因数。 90 = 2*3*3*5
   ##不断的求其最小被整除的数，然后让其除以这个数，重复这个过程
##def main():
##      n = int(input("请输入一个整数："))
##      print("n = ",end=" ")
##      while(n!=1):
##            for i in range(2,int(n+1)):
##                  if n%i==0:
##                        n=n/i
##                        if n==1:
##                              print("%d"%i,end=" ")
##                        else:
##                              print("%d *"%i,end=" ")
##                        break
##if __name__=="__main__":
##      main()
            
#输入一行字符，分别统计出其英文按字母、空格、数字、和其他字符的个数。
  #关键是如何判断 isalpha() isspace()isdigit()
##   for c in Str:
##         if c.isalpha():
##               ..
##         elif.....

##判断一个数是不是完数（因子之和）。6 =1+2+3
##from math import sqrt
##n = int(input('input a number:'))
##sum = n*-1 #是为了让第一次sum+=n/i后，sum为0，之后sum的值+1，+2，+3
##k = int(sqrt(n))
##for i in range(1,k+1):
##      if n%i == 0:
##            sum += n/i  
##            sum += i
##if sum == n:
##      print ("这个数是完数")
##else:
##      print ("这个数不是完数")


#求1 +2！+3！+..+20！
##      s = 0
##      t = 1
##for i in range(1,21):
##      t*=i
##      s+=t
##print(s)
## 不需要嵌套循环就可以做到










                           





      
