class TreeUtilities:

    def __get_spacing(depth):
        first_num_spacing = 2 ** depth
        other_num_spacing = 0
        if (depth == 1):
            other_num_spacing = 3
        elif (depth == 2):
            other_num_spacing = 7
        elif (depth == 3):
            other_num_spacing = 15
        elif (depth == 4):
            other_num_spacing = 31
        return [first_num_spacing, other_num_spacing]
    
    @classmethod
    def print_tree(self, node, depth):
        layer_nodes = [node]
        while (len(layer_nodes) > 0):
            layer_has_nodes = False
            next_layer_nodes = []
            current_values = []
            spacing = self.__get_spacing(depth)
            first_num_spacing = spacing[0]
            other_num_spacing = spacing[1]
            for i in range(len(layer_nodes)):
                n = layer_nodes[i]
                if (n is not None):
                    layer_has_nodes = True
                    if (n.left != None):
                        next_layer_nodes.append(n.left)
                    else:
                        next_layer_nodes.append(None)
                    if (n.right != None):
                        next_layer_nodes.append(n.right)
                    else:
                        next_layer_nodes.append(None)
                    #make every number two chars long
                    svalue = str(n.value).rjust(2, ' ')
                else:
                    svalue = '  '
                #spacing for layers
                if (len(current_values) == 0):
                    svalue = svalue.rjust(first_num_spacing, ' ')
                else:
                    svalue = svalue.rjust(other_num_spacing, ' ')
                current_values.append(svalue)
            if (layer_has_nodes):
                print (' '.join(current_values))
            layer_nodes = next_layer_nodes
            depth = depth - 1
    
    @classmethod
    def topview(self, root):
 
        if(root == None):
            return
        q = []
        m = dict()
        hd = 0
        root.hd = hd
    
        # push node and horizontal
        # distance to queue
        q.append(root)
    
        while(len(q)):
            root = q[0]
            hd = root.hd
    
            # count function returns 1 if the
            # container contains an element
            # whose key is equivalent to hd,
            # or returns zero otherwise.
            if hd not in m:
                m[hd] = root.data
            if(root.left):
                root.left.hd = hd - 1
                q.append(root.left)
    
            if(root.right):
                root.right.hd = hd + 1
                q.append(root.right)
    
            q.pop(0)
        for i in sorted(m):
            print(m[i], end="")