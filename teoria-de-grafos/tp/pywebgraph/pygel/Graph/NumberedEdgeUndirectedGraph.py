#!/usr/bin/python
#
# Copyright (C) 2007 Saket Sathe
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#
# $LastChangedBy: xaeroman $
# $LastChangedDate: 2007-12-09 01:41:33 +0100 (Sun, 09 Dec 2007) $
# $LastChangedRevision: 72 $
#
#


from AbstractGraph import *
from sets import Set
from random import randint, choice
from pygel.BaseElements.Edge import *
from pygel.BaseElements.Vertex import *
from pygel.Exceptions.Exceptions import *
from pygel.System.PyGelLogging import *
import time


class NumberedEdgeUndirectedGraph(AbstractGraph):

    """ Represents a numbered edge graph. Numbered edges are required to distinguish multiple edges between
        same set of vertices. This class also provides an indexed vertex and edge sets. These indices have certain advantages
        while computing in-degree and out-degree distributions.

        \ingroup Graph        
    """

    
    
    def __init__(self):
        """ Constructs a numbered edge graph
        """
        ## Dictionary of edges, indexed by edge number
        self.edgeIndex = {}

        ## Dictionary of vertices, indexed by vertex number
        self.vertexIndex = {}

        ## Dictionary of vertices, indexed by parent
        self.parentIndex = {}

        ## Dictionary of vertices and edge numbers, indexed by parent
        self.parentEdgeIndex = {}        
        
        ## Last edge number assigned
        self.__lastEdgeNumber = -1

        ## Dictionary of degree counts. Used for efficiently computing degree distribution
        self.__degreeCount = {}

        ## Logger instance
        self.logger = PyGelLogging().getLogger()

    def addEdge(self, edge):
        """ Adds an edge to a graph. It also updates the vertex and edge indices. 

            @param edge Edge of type BaseElements::Edge to be added to the graph
        """

        startVertex = edge.startVertex
        endVertex = edge.endVertex

        startVertexNumber = startVertex.vertexNumber
        endVertexNumber = endVertex.vertexNumber
        
        vertexIndex = self.vertexIndex
        parentIndex = self.parentIndex
        parentEdgeIndex = self.parentEdgeIndex

        if startVertexNumber == endVertexNumber:
            raise EdgeError(startVertexNumber, endVertexNumber, ErrorMessages.noSelfLoops)

        try:
            parentIndex[startVertexNumber].index(endVertexNumber)
            raise EdgeError(startVertexNumber, endVertexNumber, ErrorMessages.edgeAlreadyExists)
        except (ValueError, KeyError):
            self.__lastEdgeNumber += 1
            self.edgeIndex[self.__lastEdgeNumber] = edge
        
            if startVertexNumber not in vertexIndex:
                vertexIndex[startVertexNumber] = startVertex

            if endVertexNumber not in vertexIndex:
                vertexIndex[endVertexNumber] = endVertex

            if startVertexNumber not in parentIndex:
                parentIndex[startVertexNumber] = [endVertexNumber]
            else:
                parentIndex[startVertexNumber].append(endVertexNumber)

            if endVertexNumber not in parentIndex:
                parentIndex[endVertexNumber] = [startVertexNumber]
            else:
                parentIndex[endVertexNumber].append(startVertexNumber)

            if startVertexNumber not in parentEdgeIndex:
                parentEdgeIndex[startVertexNumber] = [[endVertexNumber, self.__lastEdgeNumber]]
            else:
                parentEdgeIndex[startVertexNumber].append([endVertexNumber, self.__lastEdgeNumber])

            if endVertexNumber not in parentEdgeIndex:
                parentEdgeIndex[endVertexNumber] = [[startVertexNumber, self.__lastEdgeNumber]]
            else:
                parentEdgeIndex[endVertexNumber].append([startVertexNumber, self.__lastEdgeNumber])
            
            try:
                self.__degreeCount[startVertexNumber] += 1
            except KeyError:
                self.__degreeCount[startVertexNumber] = 1
            
            try:
                self.__degreeCount[endVertexNumber] += 1
            except KeyError:
                self.__degreeCount[endVertexNumber] = 1
        
            
    def deleteEdge(self, edgeNumber):
        """ Delete an edge

            @param edgeNumber Edge number to be deleted
        """
        
        edge = self.edgeIndex[edgeNumber]
        startVertex = edge.startVertex
        endVertex = edge.endVertex

        startVertexNumber = startVertex.vertexNumber
        endVertexNumber = endVertex.vertexNumber

        vertexIndex = self.vertexIndex
        parentIndex = self.parentIndex
        parentEdgeIndex = self.parentEdgeIndex

        if startVertexNumber in parentIndex:
            # TODO: throws exception
            parentIndex[startVertexNumber].remove(endVertexNumber)

        if endVertexNumber in parentIndex:
            # TODO: throws exception
            parentIndex[endVertexNumber].remove(startVertexNumber)

        if startVertexNumber in parentEdgeIndex:
            # TODO: throws exception
            parentEdgeIndex[startVertexNumber].remove([endVertexNumber, edgeNumber])

        if endVertexNumber in parentEdgeIndex:
            # TODO: throws exception
            parentEdgeIndex[endVertexNumber].remove([startVertexNumber, edgeNumber])
            
        try:
            self.__degreeCount[startVertexNumber] -= 1
        except KeyError:
            pass
            
        try:
            self.__degreeCount[endVertexNumber] -= 1
        except KeyError:
            pass
        
        del self.edgeIndex[edgeNumber]

    def addVertex(self, vertexNumber):
        """ Adds a vertex. Should be used with care

            @param vertexNumber Vertex number of vertex to be added
            @throws PackageExceptions::VertexError
        """
        try:
            self.vertexIndex[vertexNumber]
            raise VertexError(vertexNumber, ErrorMessages.vertexAlreadyExists)
        except KeyError:
            self.vertexIndex[vertexNumber] = Vertex(vertexNumber)
            return 

    def deleteVertex(self, vertexNumber):
        """ Deletes a vertex. Should be used with care

            @param vertexNumber Vertex number to be deleted
        """
        del self.vertexIndex[vertexNumber]

    def getEdges(self):
        """ Get all graph edges

            @return edgeIndex Dictionary of edges, indexed by edge number
        """
        return self.edgeIndex

    def getVertices(self):
        """ Get all graph vertices

            @return vertexIndex Dictionary of vertices, indexed by vertex number
        """
        return self.vertexIndex

    def getVertexNumbers(self):
        """ Get all graph vertex numbers

            @return an array consisting of all the vertices numbers
        """
        return self.vertexIndex.keys()

    def getLastEdgeNumber(self):
        """ Get the last edge number

            @return __lastEdgeNumber the last edge number assigned to edges. 
        """
        return self.__lastEdgeNumber

    def getNeighbors(self, vertexNumber):
        """ Get neighbors for a vertex

            @param vertexNumber Vertex number for which neighbors have to be obtained
            @return neighbors List of neighbors. Each element of type BaseElements::Vertex
        """
        parentIndex = self.parentIndex
        neighborNumbers = parentIndex[vertexNumber]

        neighbors = []
        
        for neighborNumber in neighborNumbers:
            neighbors.append(Vertex(neighborNumber))
        return neighbors


    def getNumberOfNeighbors(self, vertexNumber):
        """ Get number of neighbors for a vertex

            @param vertexNumber Vertex number for which number of neighbors have to be obtained
            @return Number of neighbors
        """ 

        return self.__degreeCount[vertexNumber]


    def getDegreeDistribution(self):
        """ Get degree distribution

            @return degreeDistribution Dictionary indexed on degree. Values are the number of nodes for a degree
        """
        degreeDistribution = {}
        degreeCount = self.__degreeCount
        vertexNumbers = self.vertexIndex.keys()
        
        for vertexNumber in vertexNumbers:
            try:
                numberOfNeighbors = degreeCount[vertexNumber]
            except KeyError:
                numberOfNeighbors = 0


                
            try:
                degreeDistribution[numberOfNeighbors] += 1
            except KeyError:
                degreeDistribution[numberOfNeighbors] = 1
        return degreeDistribution
    
    def getSCComponents(self, getLargest):
        """ Gets the strongly connected components of a graph. It uses <A HREF="http://en.wikipedia.org/wiki/Tarjan's_strongly_connected_components_algorithm">Tarjan's strongly connected components algorithm.</A>

        
            @param getLargest If greater than 0, only returns the largest connected component
            @return allSCC List of a List of connected components
        """

        vertexTracker = {}  # vertexVisited or vertexTaken

        allSCC = []

        allVertices = self.vertexIndex
        parentIndex = self.parentIndex

        connComponent = []
        
        largestComponentSize = 0
                
        def visit(vertexNumber, connComponent, parentIndex):
            connComponent.append(vertexNumber)

            vertexTracker[vertexNumber] = 1

            children = []
            try:
                children = parentIndex[vertexNumber]
            except KeyError:
                pass
            
            for child in children:
                visited = vertexTracker[child]
                if visited == int(0):
                    visit(child, connComponent, parentIndex)

        for vertexNumber in allVertices:
            vertexTracker[vertexNumber] = 0

        for vertexNumber in allVertices:
            if vertexTracker[vertexNumber] == 0:
                visit(vertexNumber, connComponent, parentIndex)
                if getLargest > 0:
                   if len(connComponent) > largestComponentSize:
                       largestComponentSize = len(connComponent)
                       if len(allSCC) == 1: del allSCC[0]
                       allSCC.append(connComponent)
                elif getLargest == 0:
                    allSCC.append(connComponent)
                connComponent = []
        return allSCC

    def writeCC(self, fileName, allSCC):
        """ Write the connected components to a file

        
            @param fileName File name to store the connected components
            @param allSCC List of list of connected components
        """
        f = open(fileName,'w')

        for compNumber in range(0,len(allSCC)):
            f.write("Component number %s: " % (compNumber))
            f.write("%s\n" % (str(allSCC[compNumber])))
        f.close()
        

    def writeEdges(self, fileName, format):
        """ Write edges to file

            @param fileName File name to store edges in
            @param format Format of output file. Can take values: <br>
                          'simple' = simple format <br>
                          'dot' = format compatible with 'dot' command
                          
        """
        edges = self.edgeIndex.values()
        if format == 'simple':
            f = open(fileName,'w')
            for edge in edges:
                f.write("%s -- %s\n" % (edge.startVertex.vertexNumber, edge.endVertex.vertexNumber))
            f.close()
        elif format == 'dot':
            f = open(fileName,'w')
            f.write("graph G { \n")
            for edge in edges:
                f.write("%s -- %s;\n" % (edge.startVertex.vertexNumber, edge.endVertex.vertexNumber))
            f.write("} \n")
            f.close()

    def readEdges(self, fileName, format):
        """ Read edges from file

            @param fileName File name to read edges from
            @param format Format of input file. Can take values: <br>
                          'simple' = simple format
        """
        f = open(fileName)
        if format == 'simple':
            edgesRaw = f.read().split("\n")

            if edgesRaw[-1] == '': edgesRaw = edgesRaw[:-1]

            for edge in edgesRaw:
                [startVertex, endVertex] = edge.split("--")
                newEdge = Edge(Vertex(int(startVertex)), Vertex(int(endVertex)))
                self.addEdge(newEdge)

    def findEdge(self, edgeNumber):
        """ Find edge with a given edge number

            @param edgeNumber Edge number to look for
            @throws PackageExceptions::EdgeError
            @return Matched edge of type BaseElements::Edge
            
        """
        try:
            return self.edgeIndex[edgeNumber]
        except KeyError:
            raise EdgeError(edgeNumber, ErrorMessages.edgeNotFound)
    
    def findVertex(self, vertexNumber):
        """ Find vertex with a given vertex number

            @param vertexNumber Vertex number to look for
            @throws PackageExceptions::VertexError
            @return Matched vertex of type BaseElements::Vertex
        """
        try:
            return self.vertexIndex[vertexNumber]
        except KeyError:
            raise VertexError(vertexNumber, ErrorMessages.vertexNotFound)

    def hasVertex(self, vertexNumber):
        """ Checks if vertex is present

            @param vertexNumber Vertex number of the vertex to check
            @return 0 if found. 1 if not found
        """
        try:
            rs = self.findVertex(vertexNumber)
            return 0
        except VertexError, e:
            return 1

