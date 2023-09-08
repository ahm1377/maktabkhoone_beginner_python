num=int(input())
num1=int(num/100)
num2=int(((num/10)%10))
num3=int(num%10)
m_num=int(((num3*100)+(num2*10)+num1))
m_num*=2
print(m_num)
