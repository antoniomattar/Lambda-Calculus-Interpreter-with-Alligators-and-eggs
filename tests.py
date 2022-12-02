from logic import *
# x=new_var(freshVar())
# y=new_var(freshVar())
# z=new_var(freshVar())
# w = new_var(freshVar())
# print(isVariable(x) or isVariable(y) or isVariable(z))
# print(getVariables(z))


# X = new_abs(x, new_app(x, y))
# Y = new_abs(y, new_app(y, y))
# Z = new_abs(z, new_app(z, x))

# print(isAbstraction(X) or isAbstraction(Y) or isAbstraction(Z))
# print(getVariables(Z))


# app1 = new_app(x, y)
# app2 = new_app(y, z)
# app3 = new_app(z, X)

# print(isApplication(app1) or isApplication(app2) or isApplication(app3))
# print(getFirstTerm(app1))
# print(getVariables(app3))

# print(getCommonVariables(Y,Z))
# print(isCommonVariables(X,Z))
# print(getOutputVariablesFromAbs(X))

# print(X)
# print(substitute(x,z,X))

# print(getBoundVariables(new_abs(x,new_app(new_app(x,y),new_abs(new_var('j'),new_var('j'))))))

# Z = new_abs(x,new_abs(y,new_abs(x, y)))
# Z1 = alpha_rename(Z,y)
# Z2 = alpha_rename(Z1,x)
# S = new_app(new_abs(x,x),new_abs(y,x))
# S1 = alpha_rename(S,y)
# S2 = alpha_rename(S1,x)
# print(S2)

# A=new_abs(x,new_app(new_abs(y,new_app(x,y)),y))
# B=new_app(new_abs(x,new_app(x,y)),x)
# C = new_app(new_abs(x,new_abs(y,x)),y)
# D = new_app(new_abs(x,new_abs(y,new_app(x,y))),new_abs(y,y))
# E = new_app(new_abs(x,new_abs(y,new_app(x,y))),new_abs(y,new_abs(z,new_app(x,z))))
# F = new_app(new_app(new_abs(x,x),y),new_abs(z,z))
# Y_COMBINATOR = new_app(new_abs(x,new_app(x,x)),new_abs(y,new_app(y,y)))
# print('/n')
# print(to_string(E))
# print('/n')
# print((beta_reduction(E)))
# print(x)
# print(beta_reduction_totale(E))
# print(to_string([APP, [APP, [ABS, x, y], y] , z]))
# # print(beta_reduction_totale(Y_COMBINATOR))

# #############################################################################################################################
# import parser
# # A = "#x.(x)(y)"
# # print(getTermsFromParantheses("(AAAAAA)(BBBBBBBBB)(CCCCCCCCC)"))
# # print(buildTerm(A))
# # print(remove_first_and_last_spaces('ll'))
# # print(isAbstraction(A))
# # print(isApplication("(x)(y)(z)"))
# # print(checkType("(#x.x)"))
# # print(buildTerm('(#x.x)(#y.y)'))
# # print(remove_inutile_spaces('(#x.x)(#y.y)'))
# # print(open_parantheses_counter('((((((((((('))
# # print(close_parantheses_counter('((((((((((()'))
# # print(buildAbs("#x.ABC"))
# # print(checkType("(#x.xx)(fds)"))
# # print(findClosingParanthesesIndex('()',0))


# x=new_var(freshVar())
# y=new_var(freshVar())
# z=new_var(freshVar())
# term= new_app(new_abs(x,x),new_app(new_abs(y,y),z))
# #print(annotated_to_string(annotate_beta_reduction(term)))
# print(annotated_to_string(beta_reduction_choice_n(annotate_beta_reduction(term),1)))
import parsing
#print(annotated_to_string(x))
#beta_reduction_interactive_totale(parsing.parseTerm(input("Enter a term: ")))
# beta_reduction_interactive_totale(parsing.parseTerm(input("Enter a term: ")))

### ADD SAVE IMAGE CHOICE FOR BETA REDUCTION!!!!
#print(parsing.buildTerm("(#x.[#y.(y n)])"))
#print(parsing.buildTerm("(#x.[#y.(y n)])"))