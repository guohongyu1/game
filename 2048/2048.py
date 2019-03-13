import random
class Game2048(object):
    def __init__(self):
        self.scores=0
        self.data=[['' for i in range(4)] for j in range(4)]
        self.ss=[]
        self.s = []
        self.cn=self.choices()

    def start(self):
        while 1:
            window="""
            scores {}
            *-----*-----*-----*-----*
            *{:^5}*{:^5}*{:^5}*{:^5}*                 
            *-----*-----*-----*-----*
            *{:^5}*{:^5}*{:^5}*{:^5}* 
            *-----*-----*-----*-----*
            *{:^5}*{:^5}*{:^5}*{:^5}* 
            *-----*-----*-----*-----*
            *{:^5}*{:^5}*{:^5}*{:^5}*            
            *-----*-----*-----*-----*
            """
            window=window.format(self.scores,
                                *self.data[0],
                                *self.data[1],
                                *self.data[2],
                                *self.data[3]
                                )

            print(window)
            remove=input('>>>')
            if remove=='w':

                self.up()
            elif remove=='s':

                self.down()
            elif remove=='a':
                self.left()
            elif remove=='d':
                self.right()
            elif remove=='q':
                exit('退出')

    # def choice1(self):
    #     print(self.ss)
    #
    #     x=random.randint(0, len(set(self.ss)) - 1)
    #     q=list(self.ss[x])
    #
    #     print(q,type(q))
    #     print(self.data[0])
        # list(self.data[0])[0]=2
    #         q = list(self.ss.pop(x))
    #         print(q,type(q))
    #         print(type(self.data))
    #         print(type(random.choice([2, 2, 2, 2, 4])))
    #     self.data[q[0]][q[1]] = random.choice([2, 2, 2, 2, 4])
    def choices(self):
        for i in range(4):
            for j in range(4):
                if self.data[i][j] == '':
                    self.ss.append((i, j))
        if len(set(self.ss))==16:
            for i in range(2):
                x = random.randint(0, len(set(self.ss)) - 1)
                q = self.ss.pop(x)
                self.data[q[0]][q[1]] = random.choice([2, 2, 2, 2, 4])
        else:

            x = random.randint(0, len(set(self.ss)) - 1)
            q = list(self.ss.pop(x))
            # print(q,type(q))
            # print(type(self.data))
            # print(type(random.choice([2, 2, 2, 2, 4])))
            self.data[q[0]][q[1]] = random.choice([2, 2, 2, 2, 4])
        print(len((self.ss)))
        if len(self.ss) == 0:
            exit('game over')
        self.ss[0:len(self.ss)]=[]
        # print(len(set(self.ss)))
        # print(set(self.ss))
    def adds(self,ds):
        # s = []
        for i in range(4):
            list_data = []
            s=[]
            flag=True
            for j in range(4):
                temp=ds[i][j]
                if temp!= '':
                    list_data.append(temp)
            for i in range(len(list_data)):
                if flag:
                    if i+1<len(list_data) and list_data[i]==list_data[i+1]:
                        s.append(list_data[i]*2)
                        self.scores+=list_data[i]*2
                        if self.scores ==2048:
                            exit('win')
                        flag=False
                    else:
                        s.append(list_data[i])
                else:
                    flag=True
            n=len(s)
            for i in range(4-n):
                s.append('')
            # print(s)
            self.s.append(s)
        # print(self.s)
        # ds[0:len(ds)]=self.s
        # self.s=[]
        return self.s

    def up(self):
        print('up')
        self.data=self.t(self.adds(self.t(self.data)))
        # print(zip(self.adds(list(zip(*self.data)))))
        self.s = []
        self.choices()
    def down(self):
        print('down')
        self.data=self.t(self.rever(self.adds(self.rever(self.t(self.data)))))
        self.s = []
        self.choices()
    def left(self):
        print('left')
        # self.data = list(reversed(self.adds(list(reversed(self.data)))))
        self.data =self.adds(self.data)
        self.s = []
        self.choices()
    def rever(self,s):
        return [i[::-1] for i in s]

    def t(self,s):
        return [list(i) for i in zip(*s)]
    def right(self):
        print('right')
        # self.data.reverse()
        self.data=self.rever(self.adds(self.rever(self.data)))
        self.s = []
        # self.adds(list(reversed(self.data)))
        # self.data.reverse()

        self.choices()
if __name__=="__main__":
    x=Game2048()
    x.start()


