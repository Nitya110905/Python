class Myclass:

    def fun1(self):
        d={}
        for i in range(1,31):
            d[i] = i*i
        print(d)

    def fun2(self,a):
        print(a)
        l = [1,2,3,1,2]
        l1 = []

        for i in l:
            if i not in l1:
                l1.append(i)
            
            print(l1)

    def fun3(self):
        l = [3,4,5]
        l1 = [6,7,8]
        d = {}

        for i in range(len(l)):
            d[l[i]] = l1[i]

        print(d)


f1 = Myclass()

f1.fun1()
f1.fun2(10)
f1.fun3()
    