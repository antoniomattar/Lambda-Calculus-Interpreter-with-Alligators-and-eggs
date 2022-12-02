from logic import*
from parsing import*
from image_maker import*

f=new_var(freshVar())
x=new_var(freshVar())
y=new_var(freshVar())
z=new_var(freshVar())
w=new_var(freshVar())
u=new_var(freshVar())
h=new_var(freshVar())

FALSE = new_abs(x,new_abs(y,y))
TRUE = new_abs(x,new_abs(y,x))
SUCCS= new_abs(z,new_abs(f,new_abs(x,new_app(new_app(z,f), new_app(f,x)))))
MUL= new_abs(y,new_abs(z,new_abs(f,new_abs(x,new_app(new_app(y,new_app(z,f)),x)))))
ADD= new_abs(x,new_abs(y,new_app(new_app(y,SUCCS),x)))
IS_ZERO= new_abs(z,new_app(new_app(z,new_abs(x,FALSE)),TRUE))
PRED = new_abs(z,(new_abs(f,new_abs(x,new_app((new_app((new_app(z,new_abs(w,new_abs(h,new_app(h, new_app(w,f)))))),new_abs(u,x))), new_abs(u,u))))))
POW = new_abs(x,(new_abs(y,new_app(y,x))))
PAIR = new_abs(x,new_abs(y,(new_abs(f,new_app(new_app(f,x),y)))))
FIRST = new_abs(x,(new_app(x,TRUE)))
SECOND = new_abs(x,(new_app(x,FALSE)))
SUB= new_abs(x,new_abs(y,new_app(new_app(y,PRED),x)))
AND= new_abs(x,new_abs(y,new_app(new_app(x,y),FALSE)))
OR= new_abs(x,new_abs(y,new_app(new_app(x,TRUE),y)))
NOT = new_abs(x,new_abs(y,new_abs(z, new_app(new_app(x,z),y))))
XOR= new_abs(x,new_abs(y,new_app(new_app(x,new_app(new_app(y,FALSE),TRUE)),y)))


#definition des entiers de church
def dec_to_church(entier):
    if entier==0:
        return new_abs(f,new_abs(x,x))
    else:
        term=new_app(f,x)
        while entier>1:
           term= new_app(f,term)
           entier-=1
        return new_abs(f,new_abs(x,term))

def pair(A,B):
    return beta_reduction_totale(new_app((new_app(PAIR,A)),B),None,False)

def getFirstFromPair(p):
    return beta_reduction_totale(new_app(FIRST, p),None,False)

def getSecondFromPair(p):
    return beta_reduction_totale(new_app(SECOND, p),None,False)

def dec_to_lambda_relative_integers(number):
    if number >= 0:
        return pair(TRUE,dec_to_church(number))
    return pair(FALSE, dec_to_church(abs(number)))

def succ(n):#done
    return beta_reduction_totale(new_app(SUCCS,n),'arithmetic expressions',True)

def add(n,m):#done
    return beta_reduction_totale(new_app(new_app(ADD,n),m),'arithmetic expressions',True)

def power(n,m):# done
    return beta_reduction_totale(new_app((new_app(POW, n)),m),'arithmetic expressions',True)

def multiplication(n,m):#done
    return beta_reduction_totale(new_app(new_app(MUL,n),m),'arithmetic expressions',True)

def is_zero(n):#done
    return beta_reduction_totale(new_app(IS_ZERO,n),'arithmetic expressions',True)

def predec(n):#done
     return beta_reduction_totale(new_app(PRED, n),'arithmetic expressions',True)

def sub(n,m):
    return beta_reduction_totale(new_app(new_app(SUB,n),m),'arithmetic expressions',True)

#print(to_string(beta_reduction_totale(new_app(new_app(XOR,TRUE),FALSE),None,False)))
#print(to_string(dec_to_lambda_relative_integers(5)))
# ajouter les etoiles sur les alligators qui Maangent
# ajoter les sauvegardes  
# ajouter le predec ....
# terme qui termine pas
#probleme de l arret

