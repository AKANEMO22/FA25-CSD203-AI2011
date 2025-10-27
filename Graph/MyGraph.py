from queue import Queue
class MyGraph:
    def __init__(self):
        self.adj=[]
        self.size=0
        pass
    
    def readData(self, fName):
        with open(fName, 'r') as fIn:
            self.size=int(fIn.readline())
            for _ in range(self.size):
                row=list(map(int, fIn.readline().split()))
                self.adj.append(row)
            for i in range(self.size):
                for j in range(self.size):
                    self.adj[j][i]=self.adj[i][j]
        return self.size, self.adj   
    
    def showGraph(self):
        for i in self.adj:
            print(i)

    def toInt(self, v):
        return ord(v)-65
    
    def toChar(self, i):
        return chr(i+65)
    
    def deg(self, v):
        count=0
        for i in range (self.size):
            if self.adj[i][self.toInt(v)]!=0:
                count+=1
        return count
    
    def visit(self, v):
        print(v,end=' ')
        
    def BFS(self, v):
        visitted=[False]*self.size
        myQ=Queue()
        myQ.put(self.toInt(v))
        while not myQ.empty():
            u=myQ.get()
            self.visit(self.toChar(u))
            visitted[u]=True
            for i in range (self.size):
                if self.adj[i][u]!=0 and not visitted[i]:
                    visitted[i]=True
                    myQ.put(i)
    
    def DFS_visit(self, v, visitted):
        visitted[self.toInt(v)]=True
        self.visit(v)
        for i in range (self.size):
            if self.adj[i][self.toInt(v)]!=0 and not visitted[i]:
                self.DFS_visit(self.toChar(i),visitted)

    def DFS(self, v):
        visitted=[False]*self.size
        self.DFS_visit(v, visitted)
        
myG=MyGraph()
myG.readData("InputGraph.txt")
myG.showGraph()
for i in range (myG.size):
    print(f"Degree of vertex {myG.toChar(i)} is: {myG.deg(myG.toChar(i))}")
print("\n----BFS--------")
myG.BFS('A')
print("\n----DFS--------")
myG.DFS('A')