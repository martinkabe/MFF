class HamiltonianPath:

    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix
        self.n = len(adjacency_matrix)
        self.path = [0]
    
    def hamiltonian_path(self):

        if self.solve(1):
            self.show_hamiltonian_path()
        else:
            print("There is no solution to the problem.")
    
    # position is the index of vertex
    def solve(self, actual_position_index):
        if self.n == actual_position_index:
            return True
        
        for vertex_index in range(self.n):
            if self.is_feasible_solution(vertex_index, actual_position_index):
                self.path.append(vertex_index)

                if self.solve(actual_position_index+1):
                    return True
                
                #BACKTRACK
                self.path.pop()
        
        return False
    
    def is_feasible_solution(self, vertex, actual_position):
        if self.adjacency_matrix[self.path[actual_position-1]][vertex] == 0:
            return False
        
        for i in range(actual_position):
            if self.path[i] == vertex:
                return False
        
        return True

    def show_hamiltonian_path(self):
        for v in self.path:
            print(v, end=" ")


if __name__ == '__main__':

    m = [[0,1,0,0,0,1],
        [1,0,1,0,0,0],
        [0,1,0,0,1,0],
        [0,0,0,0,1,1],
        [0,0,1,1,0,1],
        [1,0,0,1,1,0]]

    hp = HamiltonianPath(m)
    hp.hamiltonian_path()
