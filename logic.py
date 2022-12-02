#les lambda termes et les variables sont représentés par des listes dont le premier element indique le type du lambda terme et le deuxieme ses composants

# Constantes




VAR = 'variable'
ABS = "abstraction"
APP = "application"

var_counter = 0

#prend en argument une chaine de caractère et renvoie une variable
def new_var(x):
    return [VAR, x]

# prend en argument deux lamba termes/ variables et renvoie le lambda terme AB
def new_app(A, B): return [APP, A , B]

#prend en argument une variable  x et un lambda terme/variable A et retourne le lambda terme (lambda x. A)
def new_abs(x,A):
    assert isVariable(x), "argument is not a variable!"
    return [ABS, x, A]

# retourne le type du lambda terme mis en parametre
def getType(P): return P[0]

# verifie si terme est de type variable
def isVariable(terme): return getType(terme) == VAR

# True si terme est une application, False sinon
def isApplication(terme): return getType(terme) == APP

#True si terme est un lambda terme de la forme (lambda x . A)
def isAbstraction(terme): return getType(terme) == ABS

# True si terme est un lambda terme de n'importe quelle forme
def isLambdaTerm(terme): return isVariable(terme) or isAbstraction(terme) or isApplication(terme)

# Prends en parametre une variable P et retourne une liste contenant le nom de la variable
def getVariablesFromVar(terme):
    assert isVariable(terme), "argument is not a variable!"
    return [terme]

# Prends en parametre une abstraction 'P' et renvoie une liste des nom des variables que cette abstraction contient
def getVariablesFromAbs(terme):
    assert isAbstraction(terme), "argument is not an abstraction!"
    return getVariables(terme[1]) + getVariables(terme[2])

# Prends en parametre une application P (A B) et nous rend le premier terme A de cette application
def getFirstTerm(app):
    assert isApplication(app), "argument is not an application!"
    return app[1]

# Prends en parametre une application P (A B) et nous rend le deuxieme terme B de cette application
def getSecondTerm(app):
    assert isApplication(app), "argument is not an application!"
    return app[2]

# Prends en parametre une application (A B) et nous rend une liste des variables que contient P(cad les variables de A et de B)
def getVariablesFromApp(terme):
    assert isApplication(terme), "argument is not an application!"
    variables = []
    first = getFirstTerm(terme)
    second = getSecondTerm(terme)
    variables += getVariables(first) + getVariables(second)
    return variables

# Prends en parametre n'importe qu'elle expression 'P' (Lambda-Term) et nous rend les variables de cette expression
def getVariables(terme):
    assert isLambdaTerm(terme), "argument is not a lambda term!"
    if isVariable(terme):
        return getVariablesFromVar(terme)
    elif isAbstraction(terme):
        return getVariablesFromAbs(terme)
    elif isApplication(terme):
        return getVariablesFromApp(terme)

# Prends en parametre une abstraction 'terme1' et n'importe quel lambda-term 'terme2' et nous rend une liste des variables communes entre terme1 et terme2, sinon elle retourne une liste vide
def getCommonVariables(terme1,terme2):
    assert isAbstraction(terme1), "argument is not an abstraction!"
    return  [i for i in getVariables(terme1) if i in getVariables(terme2)]
    return set(getVariables(terme1)).intersection(getVariables(terme2))

# Prends en parametre une abstraction 'terme1' et un lambda-term 'terme2' et nous rend True si terme2 contient des variables de terme1
def isCommonVariables(terme1,terme2):
    return not(len(getCommonVariables(terme1,terme2)) == 0)

# Prends en parametre une abstraction 'A' et nous rend la liste des variables de l'entree de l'abstraction
def getInputVariablesFromAbs(A):
    assert isAbstraction(A), "argument is not an abstraction!"
    return getVariables(A[1])

# Prends en parametre une abstraction 'A' et nous rend la liste des variables de la sortie de l'abstraction
def getOutputVariablesFromAbs(A):
    assert isAbstraction(A), "argument is not an abstraction!"
    return getVariables(A[2])

# retourne la variable en entree de l'abstraction 'A'
def getInputFromAbs(A):
    assert isAbstraction(A), "argument is not an abstraction!"
    return A[1]

# retourne les sorties de l'abstraction 'A'
def getOutputFromAbs(A):
    assert isAbstraction(A), "argument is not an abstraction!"
    return A[2]

# Prends en parametre une une variable a changer, une nouvelle variable et un lambda terme et remplace la variable a changer par la nouvelle variable dans le lambda term.
def substitute(var_a_changer,subs_terme, terme):
    if terme == var_a_changer:
        return subs_terme.copy()
    elif isVariable(terme):
        return terme.copy()
    elif isApplication(terme):
        return new_app(substitute(var_a_changer,subs_terme,getFirstTerm(terme)),substitute(var_a_changer,subs_terme,getSecondTerm(terme)))
    if getInputFromAbs(terme) == var_a_changer:
        return terme.copy()
    return new_abs(getInputFromAbs(terme).copy(),substitute(var_a_changer,subs_terme,getOutputFromAbs(terme).copy()))

#Prends en parametre un lambda terme "grandTerme" et nous retourne lee variables liees de ce terme.
def getBoundVariables(grandTerme):
    vars = []
    if isAbstraction(grandTerme):
        vars += getInputVariablesFromAbs(grandTerme)
        A = getOutputFromAbs(grandTerme)
        if isAbstraction(A) or isApplication(A):
            vars += getBoundVariables(A)
    if isApplication(grandTerme):
        vars += getBoundVariables(getFirstTerm(grandTerme))
        vars += getBoundVariables(getSecondTerm(grandTerme))
    return (vars)

#prend en parametre une variable et retourne une variable fraiche a partir du dictionnaire counters
def freshVar():
    global var_counter
    var_counter += 1
    return (var_counter -1)

# Prends en parametre un lambda term 't' et nous retourne une expression equivalente a 't' mais avec une variable fraiche au lieu de la variable 'var'
def alpha_rename(t,var):
    if isVariable(t):
        return t.copy()
    elif isAbstraction(t):
        x = getInputFromAbs(t)
        A = getOutputFromAbs(t)
        if x == var:
            x1 = new_var(freshVar())
            return new_abs(x1,substitute(var,x1,getOutputFromAbs(t)))
        else:
            return new_abs(x.copy(),alpha_rename(A,var))
    A = getFirstTerm(t)
    B = getSecondTerm(t)
    return new_app(alpha_rename(A,var),alpha_rename(B,var))

#Renvoie un lambda terme qui represente le terme t une fois réduit 
def beta_reduction(t):
    if isVariable(t):
        return None
    elif isAbstraction(t):
        x = getInputFromAbs(t)
        A = getOutputFromAbs(t)
        B = beta_reduction(A)
        if B != None:
            return new_abs(x.copy(),B) ### x.copy() sont inutiles car on ne change jamais le tableau de variables
        else:
            return None
    elif isApplication(t):
        A1 = getFirstTerm(t)
        B1 = getSecondTerm(t)
        A2 = beta_reduction(A1)
        if A2 != None:
            return (new_app(A2,B1))
        elif A2 == None:
            B2 = beta_reduction(B1)
            if B2 != None:
                return (new_app(A1,B2))
            elif isAbstraction(A1):
                x1 = getInputFromAbs(A1)
                C = getOutputFromAbs(A1)
                communBoundVars = [i for i in getBoundVariables(C) if i in getVariables(B1)]
                if communBoundVars == []:
                    return substitute(x1,B1,C)
                else: 
                    terme=A1
                    for var in communBoundVars:
                        terme=alpha_rename(terme,(var))
                        return substitute(getInputFromAbs(terme),B1,getOutputFromAbs(terme))

        else:
            return None

def annotate_reductor(t):
    if isVariable(t):
        return None
    elif isAbstraction(t):
        x = getInputFromAbs(t)
        A = getOutputFromAbs(t)
        B = annotate_reductor(A)
        if B != None:
            return new_abs(x.copy(),B) ### x.copy() sont inutiles car on ne change jamais le tableau de variables
        else:
            return None
    elif isApplication(t):
        A1 = getFirstTerm(t)
        B1 = getSecondTerm(t)
        A2 = annotate_reductor(A1)
        if A2 != None:
            return (new_app(A2,B1))
        elif A2 == None:
            B2 = annotate_reductor(B1)
            if B2 != None:
                return (new_app(A1,B2))
            elif isAbstraction(A1):
                t = t.append('*')
                return t
        else:
            return None

import image_maker
image_counter = 0
def captureImage(terme, path, counter=True, date= True):
    global image_counter
    if type(counter) == bool and counter:
        if path == None:
            image_maker.saveImage(image_maker.createImage(terme),str(image_counter),None,date)
        else:
            image_maker.saveImage(image_maker.createImage(terme),str(image_counter),path,date)
        image_counter += 1
    else:
        if path == None:
            image_maker.saveImage(image_maker.createImage(terme),str(counter),None,date)
        else:
            image_maker.saveImage(image_maker.createImage(terme),str(counter),path,date)
        image_counter += 1

def recognize_term(terme):
    if isApplication(terme):
        first=getFirstTerm(terme)
        second= getSecondTerm(terme)
        if  isAbstraction(first) and isAbstraction(second) :
            a=getOutputFromAbs(first)
            b=getOutputFromAbs(second)
            if isApplication(a) and isApplication(b):
                if isVariable(getFirstTerm(a)) and isVariable(getSecondTerm(a)) and isVariable(getFirstTerm(b)) and isVariable(getSecondTerm(b)):
                    if getFirstTerm(a)==getSecondTerm(a) and getFirstTerm(b)==getSecondTerm(b):
                        if getFirstTerm(a)==getInputFromAbs(first) and getFirstTerm(b)==getInputFromAbs(second):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def beta_reduction_totale(terme, path, saveImages=True):
    if saveImages==False:
        if beta_reduction(terme) != None:
            return beta_reduction_totale(beta_reduction(terme), path, False)
        return (terme)
    else:
        if path == None:
            if annotate_reductor(terme) != None:
                captureImage(annotate_reductor(terme), None)
            else:
                captureImage(terme, None)
        else:
            if annotate_reductor(terme) != None:
                captureImage(annotate_reductor(terme), path)
            else:
                captureImage(terme,path)
        if beta_reduction(terme) != None:
            return beta_reduction_totale(beta_reduction(terme), path)
        return (terme)
    
    
variables_letters_couples = {}

import random,string
def random_string(type):
    if type == 'lower':
        return ''.join(random.choice(string.ascii_lowercase) for i in range(1))
    elif type == 'upper':
        return ''.join(random.choice(string.ascii_uppercase) for i in range(1))

def associateVariableWithLetter(var):
    if var in variables_letters_couples:
        return
    if len(list(variables_letters_couples.keys())) >= 26 :
        x = random_string('upper')
    else:
        x = random_string('lower')
    while x in variables_letters_couples.values():
        x = random_string('lower')
    variables_letters_couples[var] = x


def to_string_var(terme):
    assert (isVariable(terme)), 'The argument is not a variable'
    associateVariableWithLetter(terme[1])
    return variables_letters_couples[terme[1]]
def to_string_abs(terme):
    assert (isAbstraction(terme)), 'The argument is not an Abstraction'
    return "\u03BB"+to_string(getInputFromAbs(terme))+"."+to_string(getOutputFromAbs(terme))

def to_string_app(terme):
    assert (isApplication(terme)), 'The argument is not an application' #ons econd term if application / no () over variable/ if ABS inside APP ()
    premier_terme = ''
    deuxieme_terme = ''
    if isVariable(getFirstTerm(terme)):
        premier_terme += to_string(getFirstTerm(terme)) 
    elif isAbstraction(getFirstTerm(terme)):
        premier_terme += "("+to_string(getFirstTerm(terme))+")" 
    elif isApplication(getFirstTerm(terme)):
        premier_terme += to_string(getFirstTerm(terme))
    if isVariable(getSecondTerm(terme)):
        deuxieme_terme += to_string(getSecondTerm(terme))
    elif isAbstraction(getSecondTerm(terme)):
        deuxieme_terme += "("+to_string(getSecondTerm(terme))+")"
    elif isApplication(getSecondTerm(terme)):
        deuxieme_terme += "("+to_string(getSecondTerm(terme))+")"
    return premier_terme + ' ' + deuxieme_terme

def to_string(terme):
    if isVariable(terme):
        return to_string_var(terme)
    elif isAbstraction(terme):
        return to_string_abs(terme)
    return to_string_app(terme)

counters = 0
def counter():
    global counters
    counters += 1
    return counters

def annotate_beta_reduction(terme):
    if isVariable(terme): return None
    elif isAbstraction(terme):
        x = getInputFromAbs(terme)
        A = getOutputFromAbs(terme)
        B = beta_reduction(A)
        if B != None:
            return new_abs(x,annotate_beta_reduction(A)) 
        else:
            return None
    elif isApplication(terme):
        A1 = getFirstTerm(terme)
        B1 = getSecondTerm(terme)
        A2 = beta_reduction(A1)
        B2 = beta_reduction(B1)
        if isAbstraction(A1):
            if A2 != None and B2 != None:
                x1 = getInputFromAbs(A1)
                C = getOutputFromAbs(A1)
                communBoundVars = [i for i in getBoundVariables(C) if i in getVariables(B1)]
                if communBoundVars == []:     
            
                    return new_app(annotate_beta_reduction(A1),annotate_beta_reduction(B1)) + [substitute(x1,B1,C)] + [counter()]
                else: 
                    t=A1
                    for var in communBoundVars:
                        t=alpha_rename(t,(var))
                
                        return new_app(annotate_beta_reduction(A1),annotate_beta_reduction(B1)) + [substitute(getInputFromAbs(t),B1,getOutputFromAbs(t))] + [counter()]
            if A2 != None and B2 == None:
                x1 = getInputFromAbs(A1)
                C = getOutputFromAbs(A1)
                communBoundVars = [i for i in getBoundVariables(C) if i in getVariables(B1)]
                if communBoundVars == []:     
            
                    return new_app(annotate_beta_reduction(A1),B1) + [substitute(x1,B1,C)] + [counter()]
                else: 
                    t=A1
                    for var in communBoundVars:
                        t=alpha_rename(t,(var))
                
                    return new_app(annotate_beta_reduction(A1),B1) + [substitute(getInputFromAbs(t),B1,getOutputFromAbs(t))] + [counter()]
            if A2 == None and B2 != None:
                x1 = getInputFromAbs(A1)
                C = getOutputFromAbs(A1)
                communBoundVars = [i for i in getBoundVariables(C) if i in getVariables(B1)]
                if communBoundVars == []:     
            
                    return new_app(A1,annotate_beta_reduction(B1)) + [substitute(x1,B1,C)] + [counter()]
                else: 
                    t=A1
                    for var in communBoundVars:
                        t=alpha_rename(t,(var))
                
                        return new_app(A1,annotate_beta_reduction(B1)) + [substitute(getInputFromAbs(t),B1,getOutputFromAbs(t))] + [counter()]
            else:
                x1 = getInputFromAbs(A1)
                C = getOutputFromAbs(A1)
                communBoundVars = [i for i in getBoundVariables(C) if i in getVariables(B1)]
                if communBoundVars == []:
            
                    return new_app(A1,B1) + [substitute(x1,B1,C)] + [counter()]
                else: 
                    t=A1
                    for var in communBoundVars:
                        t=alpha_rename(t,(var))
                
                        return new_app(A1,B1) + [substitute(getInputFromAbs(t),B1,getOutputFromAbs(t))] + [counter()]
        else:
            if A2 != None and B2 != None:
                return new_app(annotate_beta_reduction(A1),annotate_beta_reduction(B1))
            if A2 != None and B2 == None:
                return new_app(annotate_beta_reduction(A1),B1)
            if A2 == None and B2 != None:
                return new_app(A1,annotate_beta_reduction(B1))
            if A2 == None and B2 == None:
                return None

def annotated_to_string(terme):
    String_term=''
    if len(terme)==5:
        first=getFirstTerm(terme)
        second=getSecondTerm(terme)
        String_term+="(\u03BB"+str(terme[4])+to_string(getInputFromAbs(first))+"."+annotated_to_string(getOutputFromAbs(first))+') '
        String_term+='('+ annotated_to_string(second)+ ')'
    else:
        if isApplication(terme):
            first=getFirstTerm(terme)
            second=getSecondTerm(terme)
            String_term+='(' + annotated_to_string(first) + ') '
            String_term+= '('+ annotated_to_string(second) + ') '
        elif isAbstraction(terme):
            String_term+='\u03BB'+ to_string(getInputFromAbs(terme))+ '.' +annotated_to_string(getOutputFromAbs(terme))
        else:
            String_term+=to_string(terme)

        
    return String_term


def beta_reduction_choice_n(terme,n):
    if isVariable(terme): return None
    elif isAbstraction(terme):
        A = getOutputFromAbs(terme)
        B = beta_reduction_choice_n(A,n)
        if B != None:
            return new_abs(getInputFromAbs(terme), beta_reduction_choice_n((A),n))
        else:
            return None
    elif isApplication(terme):
        if len(terme) == 5:
            if terme[4] == n:
                return terme[3]
            else:
                terme = terme[:3]
                A1 = getFirstTerm(terme)
                B1 = getSecondTerm(terme)
                A2 = beta_reduction_choice_n(A1,n)
                B2 = beta_reduction_choice_n(B1,n)
                if A2 != None and B2 != None:
                    return new_app(beta_reduction_choice_n(A1,n),beta_reduction_choice_n(B1,n))
                if A2 != None and B2 == None:
                    return new_app(beta_reduction_choice_n(A1,n),B1)
                if A2 == None and B2 != None:
                    return new_app(A1,beta_reduction_choice_n(B1,n))
                if A2 == None and B2 == None:
                    return None
        else:
                terme = terme[:3]
                A1 = getFirstTerm(terme)
                B1 = getSecondTerm(terme)
                A2 = beta_reduction_choice_n(A1,n)
                B2 = beta_reduction_choice_n(B1,n)
                if A2 != None and B2 != None:
                    return new_app(beta_reduction_choice_n(A1,n),beta_reduction_choice_n(B1,n))
                if A2 != None and B2 == None:
                    return new_app(beta_reduction_choice_n(A1,n),B1)
                if A2 == None and B2 != None:
                    return new_app(A1,beta_reduction_choice_n(B1,n))
                if A2 == None and B2 == None:
                    return None
def beta_reduction_interactive(terme, at):
    global counters
    if at != None:
        print(annotated_to_string(at))
        choice = int(input("Choose a beta reduction: "))
        while choice <= 0 or choice > counters:
            print("Invalid choice")
            choice = int(input("Choose a beta reduction: "))
        try:
            return beta_reduction_choice_n(at,choice)
        finally:
            counters = 0
    else:
        try:
            return terme
        finally:
            counters = 0

def cleanReductions(l):
    if isinstance(l, list):
        return [cleanReductions(i) for i in l][:3]
    else:
        return l

def beta_reduction_interactive_totale(terme,path):
        if beta_reduction((terme)) != None:
            #print(to_string(terme))
            at = (annotate_beta_reduction((terme)))
            captureImage(at,path)
            choix=int(input("voulez-vous faire la reduction tapez sur 1 pour oui tapez sur 2 pour non "))
            if choix==1:
                return beta_reduction_interactive_totale(beta_reduction_interactive(terme,at),path)
            else:
                terme = cleanReductions(terme)
                captureImage((terme),path)
                print("C'est fini, le terme obtenu est : "+to_string(terme))
        else:
            captureImage(terme,path)
            return (terme)



        
