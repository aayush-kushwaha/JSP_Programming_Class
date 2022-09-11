'''
3. A parameter side is True if the monkey is sitting on the floor. Parameter side is False,\
   if monkey is sitting on a tree. If monkey is  sitting on the floor it has one tail.\
   If same monkey is sitting on the tree, it has 2 tails. Check whether the monkey is \
   having 1 tail or 2 tails.     
'''
a = input("Enter whether monkey is sitting on Floor or Tree. Floor/Tree: ")
if a == "floor" or a == "Floor" or a == "FLOOR" or a == "F" or a == 'f':
    side = True
elif a == "tree" or a == "Tree" or a == "TREE" or a == "T" or a == "t":
    side = False
if side == True:
    print("It has 1 tail!!!")
else:
    print("It has 2 tails!!!")