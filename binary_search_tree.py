class Binary_Search_Tree(): # create a node 
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def add_child(self,data):
        if data == self.data:
            return 
        if data <self.data:
            # add data to the node to the left 
            if self.left:
                # if the data already exists
                self.left.add_child(data)
                #recursion
            else:
                self.left=Binary_Search_Tree(data)
        else:
            if self.right:
                # if the data already exists
                self.right.add_child(data)
                #recursion
            else:
                self.right=Binary_Search_Tree(data)
    def in_order_traversal(self):
        elements=[]
        #step 1 Search left tree
        if self.left:# if left element exists
            # recursion 
            elements+=self.left.in_order_traversal()
        
        # visiting base node
        elements.append(self.data)

        if self.right:# if right element exists
            # recursion 
            elements+=self.right.in_order_traversal()
        return elements
    
    def search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min() 
            self.data = min_val
            self.right = self.right.delete(min_val)
            # max_val=self.left.find_max()
            # self.data= max_val
            #self.left=self.lest.delete(max_val)

        return self        

def build_tree(elements):
    root= Binary_Search_Tree(elements[0]) # assign first element as root node
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root


if __name__=='__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]
