class HamiltonianCycle:

    def __init__(self, adjacency_matrix):
        self.n = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.hamiltonian_path = [0]
    
    def hamiltonian_cycle(self):
        if self.solve(1):
            self.show_cycle()
        else:
            print("No feasible solution found ...")
    
    def solve(self, vertex_position):
        # check whether if we are done: the last node can be connected to the first in order to form a cycle?
        if self.n == vertex_position:
            last_item_index = self.hamiltonian_path[vertex_position-1]
 
            # last node can be connected to the first one so return true because
            # we can form a cycle
            if self.adjacency_matrix[last_item_index][0] == 1:
                self.hamiltonian_path.append(0)
                print(self.hamiltonian_path)
                return True
            # backtrack because we can not form a cycle
            else:
                return False
        
        for vertex_index in range(1, self.n):
            if self.is_feasible(vertex_index, vertex_position):
                self.hamiltonian_path.append(vertex_index)
                print(self.hamiltonian_path)
 
                if self.solve(vertex_position + 1):
                    return True
 
                # BACKTRACK
                self.hamiltonian_path.pop()
 
        return False

    def is_feasible(self, vertex, actual_position):
 
        # first criteria: whether the two nodes are connected?
        if self.adjacency_matrix[self.hamiltonian_path[actual_position - 1]][vertex] == 0:
            return False
 
        # second criteria: whether we have already added this given node?
        for i in range(actual_position):
            if self.hamiltonian_path[i] == vertex:
                return False
 
        return True
 
    def show_cycle(self):
 
        print('Hamiltonian cycle exists: \n')
 
        for v in self.hamiltonian_path:
            print(v, end=" ")
 
 
if __name__ == "__main__":
 
    m = [[0, 1, 1],
         [1, 0, 1],
         [1, 1, 0]]
 
    hamiltonian = HamiltonianCycle(m)
    hamiltonian.hamiltonian_cycle()