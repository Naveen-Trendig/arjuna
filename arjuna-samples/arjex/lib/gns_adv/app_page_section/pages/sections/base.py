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
from arjuna import GuiSection

class WPBaseGuiSection(GuiSection, metaclass=abc.ABCMeta):

    def __init__(self, page, label=None, root=None):
        super().__init__(parent_gui=page, label=label, root=root, gns_dir="gns_adv/app_page_section/sections/{}".format(page.app.section_dir))