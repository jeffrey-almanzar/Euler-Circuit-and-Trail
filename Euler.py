#Jeffrey Almanzar
class Euler_CT:

    def __init__(self):
        self.vertices =[]#strorages the vertices
        self.edges ={}  #store the edges
         
    def create_vertex(self,v):
        """post: creates the edges of the graph."""
        if v!="":
            self.vertices.append(v)
        
    def _create_dict(self):
        """post: creates a dictionary with the edges as a keys and an empty list as values."""
        for i in self.vertices:
            self.edges[i] = []
        
    def create_edge(self,v1,v2):
        """pre: the vertices are already created
        post: create the edges of the graph"""
        
        if len(self.edges)==0: #if the dictionary is empty, add the vertices
            self._create_dict()
            
        if v1 in self.vertices and v2 in self.vertices: # if v1 and v2 are valid verteices
            for i in self.edges:
                if i == v1 and v2 not in self.edges[i]: 
                   self.edges[i].append(v2)#append v2 to the value of the key v1. 
                   self.edges[v2].append(i) #append v1 to the value of the key v2.
                   #it allow me to know the degree of each vertex later
                   return True
                
    def get_degree(self,v):
        """pre: all vertices and adges must be already created. v is a valid vertex.
        post: return the degree of vertex v."""
        if v in self.edges:
            return len(self.edges[v])
        
    def has_circuit(self):
        """post: returns true if the graph has an auler circut or returns False otherwise."""
        for i in self.edges:
            if (self.get_degree(i) == 0) or (self.get_degree(i)% 2!= 0): #If one vertex is not connected or has an odd degree
                return False
        if len(self.vertices)==0:
            return False
        else:
            self.reason =True
            return True
    
    def has_trail(self):
        """post: returns true if the graph has an auler trail or returns False otherwise."""
        odd = 0
        for i in self.edges:
            if (self.get_degree(i)% 2!= 0): #If a vertex  has an odd degree
                odd +=1
        if odd ==2: #Only two vertices can have odd degrees, in order to have aN Euler trail
            return True
        else:
            return False


    def get_file_info(self,filename):
        """post: get the information from the file and storages all the vertices and edges."""
        
        file = open(filename,"r")
        info = {}
        x =0

        while True:#read all the lines
            line = file.readline()
            if line =="": #end of the file
                break
            info[x] =line
            x+=1 #new key

        #I am expecting two lines in the file only. One for the vertices and one for the edges  
        for i in info:
            if i ==0:
                for vertex in info[i]:
                    if vertex.isalpha() or vertex.isdigit():
                        self.create_vertex(vertex)
            elif i == 1:
                for edge in info[i].split():
                    self.create_edge(edge[1],edge[3])


        edges = self.get_the_edges(self.edges)
        return self.vertices, edges


    def get_the_edges(self,edges):
        """post: returns the edges."""
        edge =''
        for i in edges:
            for j in edges[i]:
                if "("+j[0]+","+i[0]+")" not in edge:
                    edge = edge+"("+i[0]+","+j[0]+") "
        return edge[:len(edge)-1]

        
            
    
