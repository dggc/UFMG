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



from AbstractMethod import *

class MetaClass (type):
    def __init__(cls, name, bases, *args, **kwargs):
        type.__init__(cls, name, bases, *args, **kwargs)
        cls.__new__ = staticmethod(cls.new)

        abstractmethods = []
        ancestors = list(cls.__mro__)
        ancestors.reverse()
        for ancestor in ancestors:
            for clsname, clst in ancestor.__dict__.items():
                if isinstance(clst, AbstractMethod):
                    abstractmethods.append(clsname)
                else:
                    if clsname in abstractmethods:
                        abstractmethods.remove(clsname)

        abstractmethods.sort()
        setattr(cls, '__abstractmethods__', abstractmethods)

    def new(self, cls, *args, **kwargs):
        if len(cls.__abstractmethods__):
            raise NotImplementedError('Can\'t instantiate class `' + \
                                      cls.__name__ + '\';\n' + \
                                      'Abstract methods: ' + \
                                      ", ".join(cls.__abstractmethods__))

        return object.__new__(self)


    
