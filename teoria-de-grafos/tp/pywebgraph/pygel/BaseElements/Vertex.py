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


from AbstractVertex import *

class Vertex(AbstractVertex):
    """ Represents graph vertex

        \ingroup BaseElements

    """
    def __init__(self,vertexNumber):
        """ Constructs graph vertex given a vertex number

            @param vertexNumber Vertex number to be assigned to the created vertex
        """

        ## Vertex number
        self.vertexNumber = vertexNumber
        
    def getVertexNumber(self):
        """ Get vertex number

            @return vertexNumber Vertex number of this vertex
        """
        return self.vertexNumber
    
    def setVertexNumber(self,vertexNumber):
        """ Set vertex number

            @param vertexNumber New vertex number
        """
        self.vertexNumber = vertexNumber
