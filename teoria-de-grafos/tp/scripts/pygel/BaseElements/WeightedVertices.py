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
# $LastChangedDate: 2007-07-31 17:42:11 +0200 (Tue, 31 Jul 2007) $
# $LastChangedRevision: 56 $
#
#


class WeightedVertices:
    """  Represents a collection of weighted vertices of type BaseElements::WeightedVertices

         \ingroup BaseElements
    
    """
    
    def __init__(self):
        """ Initialize an empty collection

        """
        ## A dictonary of weighted vertices indexed by vertex numbers and values of type BaseElements::WeightedVertex
        self.weightedVertices = {}
        
    def addVertex(self, weightedVertex):
        """ Add vertex to the collection

            @param weightedVertex Weighted vertex to be added. Should be of type BaseElements::WeightedVertex
        """
        self.weightedVertices[weightedVertex.vertexNumber] = weightedVerticex

    def delVertex(self, vertexNumber):
        """ Delete vertex from the collection

            @param vertexNumber Vertex number of the vertex to be deleted
        """
        del self.weightedVertices[vertexNumber]
        
    def getVertices(self):
        """ Get all vertices from the collection

            @return weightedVertices A dict of all weighted vertices indexed by vertex number
        """
        return self.weightedVertices
    
    def findVertex(self,vertexNumber):
        """ Find vertex in the collection

            @param vertexNumber Vertex number to be found
            @throws PackageExceptions::VertexError
            @return weightedVertex Found weighted vertex of type BaseElements::WeightedVertex
            
        """
        try:
            return self.weightedVertices[vertexNumber]
        except KeyError:
            raise VertexError(vertexNumber, ErrorMessages.vertexNotFound)


    def findWeight(self,vertexNumber):
        """ Find weight of a given vertex

           @param vertexNumber Vertex number of the vertex whose weight is to be found
           @return vertexWeight Weight of vertex
        """
        try:
            weightedVertex = self.findVertex(vertexNumber)
            return weightedVertex.vertexWeight
        except VertexError, e:
            print e.message

    
    def hasVertex(self, vertexNumber):
        """ Checks if vertex is present

            @param vertexNumber Vertex number to be checked
            @return 0 if vertex is found. Otherwise 1
        """
        try:
            rs = self.findVertex(vertexNumber)
            return 0
        except VertexError, e:
            return 1

