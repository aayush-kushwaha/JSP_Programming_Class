'''
4. A parameter is True, if the girl is smiling. Parameter smile is False, if a girl is crying.\
   A boy wants to propose a girl on Valentines Day. If she smiles then it means proposal is \
   accepted. If she cries then proposal is rejected. Print 'Happy', if she accepts the proposal\
   print 'sad', if she rejects the proposal.         

'''
girl = input("Is girl smiling or crying? \n")
if girl == 'smiling':
    smile = True
else:
    smile = False
if smile == True:
    print("Proposal is accepted :)")
else:
    print("Proposal is rejected :_(")
