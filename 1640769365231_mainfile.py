class Node:
    def __init__(self,data):
        self.data = data
        self.children = [None]*26
        # self.children = [(None,""),(None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
        self.wordEnd = False
    
class Tree:
    
    def __init__(self):
        self.root = self.getnode("root")

    def getnode(self,character):
        return Node(character)

    def char_to_index(self, character):
        return ord(character) - ord("a")

    def insert(self, word):
        temp = self.root
        for i in range(len(word)):
            index = self.char_to_index(word[i])
            if not temp.children[index]:
                # temp.children[index] = word[i]
                temp.children[index] = self.getnode(word[i])
            temp = temp.children[index]
        temp.wordEnd = True
    

    def search(self, key):
        temp = self.root
        for i in range(len(key)):
            index = self.char_to_index(key[i])
            if not temp.children[index]:
                return False
            temp = temp.children[index]
        return temp.wordEnd
    # def display(self):
    #     t.insert("ilyas")
    #     t.insert("farhan")
    #     t.insert("ali")
    #     t.insert("ramzan")
    #     t.insert("aliza")
    #     s = input("Enter a string to search:")
    #     print(t.search(s))


   
        
    # def display(self,root,word):
    #     i = 0
    #     if root.wordEnd == True:
    #         return root
    #     if root.children[i] == None:
    #         i += 1
    #         return i
    #     else:
    #         index = self.char_to_index(word)
    #         word = root.children[index].data
    #         print(word)
    #         self.display(root.children[index], word)
    #         return root.children[index].data

    def display(self, key):
        temp = self.root
        for i in range(len(key)):
            index = self.char_to_index(key[i])
            print(temp.children[index].data)
            temp = temp.children[index]

    def suggestion(self, word):
        list = []
        index = self.char_to_index(word)
        if self.root.children[index] == None:
            print("No word is present whch starts with this letter you entered.")
        else:

            temp = self.root.children[index]
            list.append(temp.data)
            while temp.wordEnd != True:
                i = 0
                while temp.children[i] == None:
                    i += 1
                list.append(temp.children[i].data)
                temp = temp.children[i]
            for i in range(len(list)):
                print(list[i], end="")

t = Tree()
file = open("Dict.txt",'r')
lines = file.readlines
for line in lines:
    t.insert(line)

# t.display()
# t.insert("ilyas")
# t.insert("farhan")
# t.insert("ali")
# t.insert("ramzan")
# t.insert("ram")
# t.insert("aliza")
# print(t.search("farhan"))
# print(t.search("ilyas"))
# print(t.search("ramzan"))
# print(t.search("alia"))
# # inp = input("Enter string:")
# # t.display(inp)
# t.suggestion("r")
