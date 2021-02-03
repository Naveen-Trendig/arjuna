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

import abc
from arjuna import GuiPage

from .sections.topnav import TopNav
from .sections.leftnav import LeftNav, LeftNavCodedRootLabel, LeftNavCodedRootLocator


class WPBaseGuiPage(GuiPage, metaclass=abc.ABCMeta):

    def __init__(self, source_gui):
        super().__init__(source_gui=source_gui, gns_dir="gns_adv/app_page_section")


class WPFullGuiPage(WPBaseGuiPage, metaclass=abc.ABCMeta):

    def __init__(self, source_gui):
        super().__init__(source_gui=source_gui)

    @property
    def top_nav(self):
        return TopNav(self)

    @property
    def left_nav(self):
        return LeftNav(self)

    @property
    def left_nav_coded_root_label(self):
        return LeftNavCodedRootLabel(self)

    @property
    def left_nav_coded_root_locator(self):
        return LeftNavCodedRootLocator(self)

