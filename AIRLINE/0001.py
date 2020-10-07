import os
import time
aq=open( 'list_1.txt','r+')
l=aq.readlines()
aq.close()


aw=open( 'list_2.txt','r+')
k=aw.readlines()
aw.close()

ae=open( 'list_3.txt','r+')
j=ae.readlines()
ae.close()

ar=open( 'list_4.txt','r+')
h=ar.readlines()
ar.close()

at=open( 'list_4.txt','r+')
g=at.readlines()
at.close()

ay=open( 'list_4.txt','r+')
f=ay.readlines()
ay.close()
#sintex
string='''
ww   ww 
ww   ww 
ww w ww  
ww/ \ww E L C O M'''

string2=['Tir:-','\n','Name:-','E-mail:-','YOUR GENDER IS:-','LEAVING FROM:-','GOING TO:-']
q=''
def welcom():
    pri(string)
            
        
    
        
def pri(a):
    s=''
    sa=0
    for i in a:
        os.system('cls')
        s=s+a[sa]
        print(s)
        time.sleep(0.0000001)
        sa=sa+1
def pri1(a):
    s=''
    sa=0
    for i in a:
        os.system('cls')
        s=s+a[sa]
        print(s)
        time.sleep(0.02)
        sa=sa+1
def air():
    z='                 ^       '
    x='                ^ ^      '
    c='               ::: >>    '
    v='     <~~      ======\   '
    b=' < <----------======>»» '
    n='     <~~      ======/   ' 
    m='               ::: >>    '
    lx='                V V   '
    kx='                 V    '
    for i in range (100):
        os.system('cls')
        print(i*' '+z)
        print(i*' '+x)
        print(i*' '+c)
        print(i*' '+v)
        print(i*' '+b)
        print(i*' '+n)
        print(i*' '+m)
        print(i*' '+lx)
        print(i*' '+kx)
        time.sleep(0.001)
def home():
    air()
    os.system('cls')
    a=('''
             N I T I N
             A I R L I N E~''')
    pri1(a)
    print('''
    1|Resrrvation
    2|Canellation
    3|user login
    4|Info*''')
    print(q)
#############################################################################################################################################
class start:

        
    def Resrrvation(self):
        welcom()
        self.a=input('Name:-')
        qs=''
        while True:
            print(qs)
            self.s=input('E-mail:-')
            
            if '@' in self.s:
                print ('ok')
                break
            else:
                qs="ERROR__ e-mail is wrong " 
                continue
            
        
        gh=''
        while True:
            print(gh)
            self.d=input('YOUR GENDER IS:-')
            
            if self.d=='Male'or self.d=='male'or self.d=='Female'or self.d=='female'or self.d=='other':
                print ('ok')
                break
            else:
                gh="ERROR__ gender should be MALE\|/FEMALE or other " 
                continue


        while True:
            os.system('cls')
            qo=''
            print('''
LEAVING FROM:-
1|India
2|China
3|Nepal
Choose one''')
            d=input('LEAVING FROM:-')
            print(qs)
            print('''
GOING TO:-
1|India
2|China
3|Nepal
Choose one''')
            do=input('GOING TO:-')
            if do == d:
                qo="ERROR__ Can not go same place try again"
                print ('ok')
                continue
            elif do=='' or d=='':
                qs="ERROR__ Can not can't live any information try again" 
                continue
            elif d== '1'and do=='2':
                a6=open('list_1.txt','r+')
                list1=a6.readlines()
                a6.close()
                w=len(list1)
                if w== 0:
                    os.system('cls')
                    print("SORRY ON SEATS ARE LEFT ")
                    input('press enter')
                    hghggh
                else:
                    qw= open("11.txt","a+")
                    qw.write(list1[w-1])#
                    ff=list1.pop(w-1)
                    a6=open('list_1.txt','w+')
                    for i in list1:
                        a6.writelines(i)
                    a6.close()
                    qw.write('\n')
                    qw.write(self.a)#
                    qw.write('\n')
                    qw.write(self.s)#
                    qw.write('\n')
                    qw.write(self.d)#
                    qw.write('\n')
                    qw.write('India')#
                    qw.write('\n')
                    qw.write('China')#
                    qw.write('\n')
                    qw.close()
                    print("YOUR TRI NUMBER IS "+str(ff))
                    input('')
                    rfgtrg

                    break
            elif do== '1'and d=='3':
                a6=open('list_2.txt','r+')
                list1=a6.readlines()
                a6.close()
                w=len(list1)
                if w== 0:
                    os.system('cls')
                    print("SORRY ON SEATS ARE LEFT ")
                    input('press enter')
                    hghggh
                else:
                    qw= open("22.txt","a+")
                    qw.write(list1[w-1])#
                    ff=list1.pop(w-1)
                    a6=open('list_2.txt','w+')
                    for i in list1:
                        a6.writelines(i)
                    a6.close()
                    qw.write('\n')
                    qw.write(self.a)#
                    qw.write('\n')
                    qw.write(self.s)#
                    qw.write('\n')
                    qw.write(self.d)#
                    qw.write('\n')
                    qw.write('India')#
                    qw.write('\n')
                    qw.write('Nepal')#
                    qw.write('\n')
                    qw.close()
                    print("YOUR TRI NUMBER IS "+str(ff))
                    input('')
                    rfgtrg

                    break
            
            elif do== '2'and d=='1':
                a6=open('list_3.txt','r+')
                list1=a6.readlines()
                a6.close()
                w=len(list1)
                if w== 0:
                    os.system('cls')
                    print("SORRY ON SEATS ARE LEFT ")
                    input('press enter')
                    hghggh
                else:
                    qw= open("33.txt","a+")
                    qw.write(list1[w-1])#
                    ff=list1.pop(w-1)
                    a6=open('list_3.txt','w+')
                    for i in list1:
                        a6.writelines(i)
                    a6.close()
                    qw.write('\n')
                    qw.write(self.a)#
                    qw.write('\n')
                    qw.write(self.s)#
                    qw.write('\n')
                    qw.write(self.d)#
                    qw.write('\n')
                    qw.write('China')#
                    qw.write('\n')
                    qw.write('India')#
                    qw.write('\n')
                    qw.close()
                    print("YOUR TRI NUMBER IS "+str(ff))
                    input('')
                    rfgtrg

                    break
            elif do== '2'and d=='3':
                a6=open('list_4.txt','r+')
                list1=a6.readlines()
                a6.close()
                w=len(list1)
                if w== 0:
                    os.system('cls')
                    print("SORRY ON SEATS ARE LEFT ")
                    input('press enter')
                    hghggh
                else:
                    qw= open("44.txt","a+")
                    qw.write(list1[w-1])#
                    ff=list1.pop(w-1)
                    a6=open('list_4.txt','w+')
                    for i in list1:
                        a6.writelines(i)
                    a6.close()
                    qw.write('\n')
                    qw.write(self.a)#
                    qw.write('\n')
                    qw.write(self.s)#
                    qw.write('\n')
                    qw.write(self.d)#
                    qw.write('\n')
                    qw.write('China')#
                    qw.write('\n')
                    qw.write('Nepal')#
                    qw.write('\n')
                    qw.close()
                    print("YOUR TRI NUMBER IS "+str(ff))
                    input('')
                    rfgtrg

                    break
            elif do== '3'and d=='1':
                a6=open('list_5.txt','r+')
                list1=a6.readlines()
                a6.close()
                w=len(list1)
                if w== 0:
                    os.system('cls')
                    print("SORRY ON SEATS ARE LEFT ")
                    input('press enter')
                    hghggh
                else:
                    qw= open("55.txt","a+")
                    qw.write(list1[w-1])#
                    ff=list1.pop(w-1)
                    a6=open('list_5.txt','w+')
                    for i in list1:
                        a6.writelines(i)
                    a6.close()
                    qw.write('\n')
                    qw.write(self.a)#
                    qw.write('\n')
                    qw.write(self.s)#
                    qw.write('\n')
                    qw.write(self.d)#
                    qw.write('\n')
                    qw.write('Nepal')#
                    qw.write('\n')
                    qw.write('India')#
                    qw.write('\n')
                    qw.close()
                    print("YOUR TRI NUMBER IS "+str(ff))
                    input('')
                    rfgtrg

                    break
            elif do== '3'and d=='2':
                a6=open('list_6.txt','r+')
                list1=a6.readlines()
                a6.close()
                w=len(list1)
                if w== 0:
                    os.system('cls')
                    print("SORRY ON SEATS ARE LEFT ")
                    input('press enter')
                    hghggh
                else:
                    qw= open("66.txt","a+")
                    qw.write(list1[w-1])#
                    ff=list1.pop(w-1)
                    a6=open('list_6.txt','w+')
                    for i in list1:
                        a6.writelines(i)
                    a6.close()
                    qw.write('\n')
                    qw.write(self.a)#
                    qw.write('\n')
                    qw.write(self.s)#
                    qw.write('\n')
                    qw.write(self.d)#
                    qw.write('\n')
                    qw.write('Nepal')#
                    qw.write('\n')
                    qw.write('China')#
                    qw.write('\n')
                    qw.close()
                    print("YOUR TRI NUMBER IS "+str(ff))
                    input('')
                    rfgtrg

                    break
            else:
                continue
#####################################################################################################################################
    def Canellation(self):
        welcom()
        ghr=''
        qq='''['11:1','11:2','11:3','11:4','11:5','11:6','11:7','11:8','11:9','11:10']
['22:1','22:2','22:3','22:4','22:5','22:6','22:7','22:8','22:9','22:10']
['33:1','33:2','33:3','33:4','33:5','33:6','33:7','33:8','33:9','33:10']
['44:1','44:2','44:3','44:4','44:5','44:6','44:7','44:8','44:9','44:10']
['55:1','55:2','55:3','55:4','55:5','55:6','55:7','55:8','55:9','55:10']
['66:1','66:2','66:3','66:4','66:5','66:6','66:7','66:8','66:9','66:10']'''
        while True:
            print(ghr)
            self.dd=input('YOUR TIR number:-')
            
            if self.dd==''or self.dd not in qq:
                ghr=("May you don't give TIR number or type it WRONG")
                continue
            else:
                oo=[]
                w= str(self.dd)+'\n'
                print(w)
                qs=w[0:2]
                io=str(qs)+'.txt'
                ab=open(io,'r+')
                s=0
                la=ab.readlines()
                
                
                for i in la:
                    
            
                    if w==i:
                        a=open('list_'+str(w[0])+'.txt','a+')
                        a.writelines(w)
                        a.close()
                        for ig in range(7):
                            print(la[s])
                            la.pop(s)
                            
                            
                    else:
                        s=s+1
                        oo.append(i)
                ab.close()
                ag=open(io,'w+')

                for i in la:
                    ag.writelines(i)
                    ag.write('\n')
                ag.close()
                oo=[]
                os.system('cls')
                pri1("YOUR TICKET IS CANCELED")
                input('press enter')
                dfsg
                

 ##############################################################################################################################33       
 
        
        
    def userlogin(self):
        while True:
            os.system('cls')
            ax=input('Enter your name:--')
            e=input('enter login password or reset password:--')
            if e=='creat':
                self.creat(ax)
                break
            elif e=='resetall':
                l3=['1','2','3','4','5','5']        
                for i in l3:
                    x=open(str(i)+str(i)+'.txt','w+')             
                    x.close()
                    x=open('list_'+str(i)+'.txt','w+')
                    for j in range(10):
                        x.writelines(i+i+':'+str(j+1))
                        x.write('\n')             
                    x.close()
                    print('all reset')
                    input('')
                    erf
            else:
                continue
           
    def creat(self,ax):
        welcom()
        pri1(ax)
        
           
        while True:
            os.system('cls')
            print('''
ww   ww 
ww   ww 
ww w ww  
ww/ \ww E L C O M'''+'\n',ax)
            
            print('''WHICH FLIGHT YOU WANT TO CHANGE
                11,22,33,44,55,66
                ''')
            er=''
            axw=input('choose flight no.:-')
            if axw not in ''' 11 22 33 44 55 66 ''':
                er='WRONG FLIGHT TRY AGAIN'
                continue
                
            else:
                
                l=str(axw)
                q=l[0]
                x=open('list_'+str(q)+'.txt','w+')
                for i in range(10):
                    x.writelines(q+q+':'+str(i+1))
                    x.write('\n')             
                x.close()
                print('☺ FLIGHT IS NOW RESET ☻')
                  
                input('')
                yhyh
 ###########################################################################################################################################3       
        
        
    def info(self):
        welcom()
        ghr=''
        qq='''['11:1','11:2','11:3','11:4','11:5','11:6','11:7','11:8','11:9','11:10']
['22:1','22:2','22:3','22:4','22:5','22:6','22:7','22:8','22:9','22:10']
['33:1','33:2','33:3','33:4','33:5','33:6','33:7','33:8','33:9','33:10']
['44:1','44:2','44:3','44:4','44:5','44:6','44:7','44:8','44:9','44:10']
['55:1','55:2','55:3','55:4','55:5','55:6','55:7','55:8','55:9','55:10']
['66:1','66:2','66:3','66:4','66:5','66:6','66:7','66:8','66:9','66:10']'''
        while True:
            print(ghr)
            self.ddd=input('YOUR TIR number:-')
            
            if self.ddd==''or self.ddd not in qq:
                ghr=("May you don't give TIR number or type it WRONG")
                continue
            else:
                os.system('cls')
                     
                w= str(self.ddd)+'\n'
                print(w)
                qs=w[0:2]
                io=str(qs)+'.txt'
                ab=open(io,'r+')
                s=0
                lw=ab.readlines()
                fg=''
                for i in lw:
                    
                    
                 
                    if w==i:
                        sq=0
                        for ig in range(7):
                            flg=str(str(string2[sq])+str(lw[s]))+'\n'
                            fg=fg+flg
                            sq=sq+1
                            s=s+1
                 
                    else:
                        s=s+1
                pri1(fg)

                ab.close()
                input(' SERCH IS STOP --Press Enter to main menu')
                fdg
            
                    

aa= start()
home()


while True:
    try:
        ans=int(input('enter your option'))
        if ans in (1,2,3,4):
            if ans==1:
                aa.Resrrvation()
            elif ans==2:
                aa.Canellation()
            elif ans==3:
                
                aa.userlogin()
            elif ans==4:
                aa.info()

        else:
            q=('''"ENTER ONE OF THIS "''')
            home()
            continue 
        break 
    except:
        q=('''"ENTER ONLY INT "''')

        home()
        continue

