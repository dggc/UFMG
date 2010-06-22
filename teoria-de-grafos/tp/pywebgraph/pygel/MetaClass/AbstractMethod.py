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

class AbstractMethod (object):
    def __init__(self, func):
        self._function = func

    def __get__(self, obj, type):
        return self.AbstractMethodHelper(self._function, type)

    class AbstractMethodHelper (object):
        def __init__(self, func, cls):
            self._function = func
            self._class = cls

        def __call__(self, *args, **kwargs):
            raise TypeError('Abstract method `' + self._class.__name__ \
                            + '.' + self._function + '\' called')

        
