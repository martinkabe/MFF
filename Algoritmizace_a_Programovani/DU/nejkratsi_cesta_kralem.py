class DataReader:
	def _check_obstacles(obstacles):
		list_of_tupples = []
		for obs in obstacles:
			temp_tuple = ()
			for v in obs:
				if v < 1 or v > 8:
					return None
				temp_tuple = temp_tuple + (v-1,)
			list_of_tupples.append(temp_tuple)
		return list_of_tupples

	@classmethod
	def read_data(cls):
		no_obstacles = int(input())
		obstacles = []
		for i in range(no_obstacles):
			obstacle = tuple(map(int, input().split()))
			obstacles.append(obstacle)

		obs = cls._check_obstacles(obstacles)
		start = tuple(map(int, input().split()))
		target = tuple(map(int, input().split()))
		
		if obs is not None:	
			return obstacles, start, target
		return None, start, target

class AStarGraph:
	# Nize bude nasledovat implementace A* algoritmu, ktery je používaný pro vyhledávání optimálních cest v kladně ohodnocených grafech.
	# https://www.youtube.com/watch?v=ySN5Wnu88nE
	# https://cs.wikipedia.org/wiki/A*
 
	def __init__(self, threshold):
		self.threshold = threshold
		self._barriers = []

	@property
	def barriers(self):
		return self._barriers
	
	@barriers.setter
	def barriers(self, b):
		self._barriers = b

	def heuristic(self, start, goal):
		# Jako heuristika bude pouzita Chebyshevova vzdalenost, coz je minimální počet tahů, které musí král provést na šachovnici , 
		# aby mohl cestovat mezi dvěma políčky (sousedni policka nebo diagonalne)
		D = 1
		D2 = 1
		dx = abs(start[0] - goal[0])
		dy = abs(start[1] - goal[1])
		return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
 
	def get_vertex_neighbours(self, pos):
		n = []
		# Tahy, ktere muze sachovy kral provadet (ve vsech smerech i diagonalne, vzdy o jedno policko)
		# zkousim dat koordinaty jako tuple melo by to byt rychlejsi nez list
		for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]:
			x2 = pos[0] + dx
			y2 = pos[1] + dy
			if x2 < 1 or x2 > 8 or y2 < 1 or y2 > 8:
				continue
			n.append((x2, y2))
		return n
 
	def move_cost(self, a, b):
		for barrier in self._barriers:
			if b in barrier:
				return self.threshold # Vratim nejaky prehnane velky cost
		return 1 # Vratim standardni cost = 1, coz odpovida realne jednomu tahu
 
def AStarSearch(start, end, graph):
 
	G = {} # Skutečné ohodnoceni na na tah na každé pozici z počáteční pozice
	F = {} # Odhadnute ohodnoceni na tah od začátku do konce přes tuto pozici
 
	# Inicializace pocatecnich hodnot
	G[start] = 0
	F[start] = graph.heuristic(start, end)
 
	closedVertices = set()
	openVertices = set([start])
	cameFrom = {}
 
	while len(openVertices) > 0:
		# Získej vrchol v otevřeném seznamu s nejnižším skóre F
		current = None
		currentFscore = None
		for pos in openVertices:
			if current is None or F[pos] < currentFscore:
				currentFscore = F[pos]
				current = pos
 
		# Zkontrolujte, zda bylo dosazeno cile
		if current == end:
			# Vrat se zpatky po trase
			path = [current]
			while current in cameFrom:
				current = cameFrom[current]
				path.append(current)
			path.reverse()
			return path, F[end] # HOTOVO!
 
		# Označte aktuální vrchol jako uzavřený
		openVertices.remove(current)
		closedVertices.add(current)
 
		# Aktualizuj skóre pro vrcholy poblíž aktuální pozice
		for neighbour in graph.get_vertex_neighbours(current):
			if neighbour in closedVertices:
				continue # Tento uzel jsme již zpracovali (vsemi moznymi zpusoby)
			candidateG = G[current] + graph.move_cost(current, neighbour)
 
			if neighbour not in openVertices:
				openVertices.add(neighbour) # Novy vrchol objeven
			elif candidateG >= G[neighbour]:
				continue # Toto aktualni G skóre je horší, než predchozi
 
			# Prijmi toto G skore
			cameFrom[neighbour] = current
			G[neighbour] = candidateG
			H = graph.heuristic(neighbour, end)
			F[neighbour] = G[neighbour] + H
 
	return -1
 
if __name__ == "__main__":
	threshold = 100
	barriers, start, target = DataReader.read_data() # nacti prekazky, koordinaty pocatecni a cilove pozice krale
	if barriers is not None:
		# instance objektu
		graph = AStarGraph(threshold)
		# setter pro prekazky
		graph.barriers = [barriers]
		# vyhodi nejkratsi cestu jako List[tuple] vzdalenosti teto cesty jako min(#policek) k dosazeni cile
		result, cost = AStarSearch(start, target, graph)
		# print ("route", result)
		if cost > threshold:
			print (-1)
		else:
			print (cost)
	
# Test 1
# 1
# 2 1
# 1 1
# 2 2

# Test 2
# 12
# 3 5
# 3 6
# 3 7
# 4 7
# 5 7
# 6 7
# 6 6
# 6 5
# 6 4
# 6 3
# 5 3
# 4 3
# 1 1
# 8 8

# Test 3
# 8
# 3 1
# 3 2
# 3 3
# 3 4
# 3 5
# 3 6
# 3 7
# 3 8
# 1 1
# 8 8