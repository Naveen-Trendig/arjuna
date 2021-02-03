# This file is a part of Arjuna
# Copyright 2015-2021 Rahul Verma

# Website: www.RahulVerma.net

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from arjuna import *

class WordPress(GuiApp):

    def __init__(self, *, section_dir):
        url = C("wp.login.url")
        super().__init__(url=url)
        self.__section_dir = section_dir

    @property
    def section_dir(self):
        return self.__section_dir

    def launch(self):
        super().launch()

        from .pages.home import Home
        return Home(self)