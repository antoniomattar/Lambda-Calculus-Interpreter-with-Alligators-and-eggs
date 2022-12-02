from logic import *
# TERME = input('Please enter a Lambda-Term: ')
#renvoie conteur le nombre de parentheses ouvertes et indexes la liste des indices des parenthese)

variables_counter = 0
variables = {}

def open_parantheses_counter(terme):
    counter = 0
    indexes = []
    for i in range(len(terme)):
        if terme[i] == '(' or terme[i]=='[' or terme[i]=='{':
            counter += 1
            indexes.append(i)
    return (counter, indexes)


# comme celle d avant 
def close_parantheses_counter(terme):
    counter = 0
    indexes = []
    for i in range(len(terme)):
        if terme[i] == ')' or terme[i]==']' or terme[i]=='}':
            counter += 1
            indexes.append(i)
    return (counter, indexes)

open_list = ["[","{","("]
close_list = ["]","}",")"]
  
# teste si toutes les ouvertes ont ete fermees et quil n y a pas par exemple le cas )(...
def balancedParantheses(terme):
    stack = []
    for i in terme:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    return len(stack) == 0

#renvoie le nombre de parentheses ouvertes qui est aussi le nombre de couples de parenthèses que le terme compte
def parantheses_couples(terme):
    assert balancedParantheses(terme), "Not balanced Terme"
    return (open_parantheses_counter(terme)[0])

def findOpeningParanthesesIndex(terme, closeParentheseIndex):
    assert balancedParantheses(terme), "Not balanced Terme"
    if terme[closeParentheseIndex]== ')':
      openParantheseIndex = closeParentheseIndex
      counter = 1
      while (counter > 0 ):
         openParantheseIndex -=1
         c = terme[openParantheseIndex]
         if c in open_list:
            counter -= 1
         elif c in close_list:
            counter += 1
    
    return openParantheseIndex


# on lui donne l indice dune parenthese ouverte et renvoie l indice de la parenthese fermante
def findClosingParanthesesIndex(terme, openParentheseIndex):
    assert balancedParantheses(terme), "Not balanced Terme"
    closeParantheseIndex = openParentheseIndex
    counter = 1
    while (counter > 0 ):
        closeParantheseIndex +=1
        c = terme[closeParantheseIndex]
        if c == "(" or c=='{' or c=='[':
            counter += 1
        elif c == ")" or c==']' or c=='}':
            counter -= 1
    return closeParantheseIndex

# renvoie ce qu'il y a entre la parenthese ouverte a l indice i et sa parethese fermante
def getTermFromParantheses(terme,i):
    return terme[i+1:findClosingParanthesesIndex(terme,i)]

def getTermsFromParantheses(terme):
    terms = []
    # indexes_of_open_parantheses = open_parantheses_counter(terme)[1]
    # for i in range(len(indexes_of_open_parantheses)):
    #     if findClosingParanthesesIndex(terme,indexes_of_open_parantheses[i]) > findClosingParanthesesIndex(terme,indexes_of_open_parantheses[i-1]):
    #         terms.append(getTermFromParantheses(terme,indexes_of_open_parantheses[i]))
    i = 0
    while i < len(terme):
        if terme[i] == '(' or terme[i]=='{' or terme[i]=='[':
            terms.append(getTermFromParantheses(terme,i))
            i = findClosingParanthesesIndex(terme,i)
        else:
            i+=1
    return terms

#fonction qui enleve les espaces successifs et laisse un seul espace
def remove_multiple_spaces(terme):
    terme = terme.strip()
    new_term=''
    i=0
    while i<len(terme):
        new_term+=terme[i]
        if terme[i]==' ':
            while terme[i]==' ':
                i+=1
        else:
            i+=1
    return new_term

def checkType(terme):
    if "#" == terme[0]:
        return ABS
    elif  terme[0] == '(' or terme[0]=='{' or terme[0]=='[':
        l = getTermsFromParantheses(terme)
        if len(l) == 1 and ( (terme[-1] == ')' or terme[-1]==']' or terme[-1]=='}')):
            return checkType(getTermFromParantheses(terme,0))
        else:
            return APP
    elif not(any(charac in (terme) for charac in ['(',')',' ','#','.', '[', ']','{','}'])):
        return VAR
    else:
        return APP

def isVariable(terme):
    return checkType(terme) == VAR

def isAbstraction(terme):
    return checkType(terme) == ABS

def isApplication(terme):
    return checkType(terme) == APP


#on prend l input de labs en chaine de caractères
def extractInputFromAbs(terme):
    input = ''
    if checkType(terme) == ABS:
        i = 1
        while (terme[i] != "."):
            input += terme[i]
            i+=1
    return input
# on prend l output en chaine de caractères
def extractOutputFromAbs(terme):
    index_of_point = terme.find('.')
    if checkType(terme) == ABS:
        return terme[index_of_point+1:]

def buildVar(terme):
    assert (checkType(terme) == VAR)
    # print(terme)
    if terme[0]!='(' and terme[0]!='{' and terme[0]!='[':
        if terme in variables:
            return variables[terme]
        else:
            variables[terme] = new_var(freshVar())
            return variables[terme]
    else :
        return buildTerm(getTermFromParantheses(terme,0))

def buildAbs(terme):
    assert (checkType(terme) == ABS)
    input = extractInputFromAbs(terme)
    output = extractOutputFromAbs(terme)
    # print(terme,"INPUT:", input,'OUTPUT:', output)
    if not(terme [0] in open_list):
        return new_abs((buildTerm(input)),buildTerm(output))
    else:
        return buildTerm(getTermFromParantheses(terme,0))

def extract_terms(text):
    terms = []
    current_term = ""
    paranthesis_level = 0
    for i in range(len(text)):
        if text[i] == "(" or text[i]=='{' or text[i]=='[' :
            if paranthesis_level == 0:
                current_term = ""
            else:
              current_term += text[i]
            paranthesis_level += 1
        elif text[i] == ")" or text[i]==']' or text[i]=='}':
            paranthesis_level -= 1
            if paranthesis_level > 0:
                current_term += text[i]
        elif text[i] == " " and paranthesis_level == 0:
            if current_term != "":
                terms.append(current_term)
                current_term = ""
        else:
            current_term += text[i]
    if current_term != "":
        terms.append(current_term)
    return terms

def buildApp(terme):
    assert (checkType(terme) == APP)
    liste_de_termes = extract_terms(terme)
    if terme[0]!='(' and terme[0]!='{' and terme[0]!='[':
        n = len(liste_de_termes)
        if n == 0:
            return None
        else:
            t = buildTerm(liste_de_termes[0])
        for k in range(1, n):
            if liste_de_termes[k] == '':
                return t
            t = new_app(t, buildTerm(liste_de_termes[k]))
        return t
    else:
        t = buildTerm(liste_de_termes[0])
        for k in range(1, len(liste_de_termes)):
            if liste_de_termes[k] == '':
                return t
            t = new_app(t, buildTerm(liste_de_termes[k]))
        return t
    
def buildTerm(terme):
    if isVariable(terme): return buildVar(terme)
    elif isAbstraction(terme): return buildAbs(terme)
    elif isApplication(terme): return buildApp(terme)

def parseTerm(terme):
    return (buildTerm(remove_multiple_spaces(terme)))