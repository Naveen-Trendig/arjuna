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
from arjex.lib.gns_adv.app_page_section.app import WordPress

@for_module
def dashboard(request):
    # Setup
    wordpress = WordPress(section_dir="simple_maxwait")
    home = wordpress.launch()
    dashboard = home.login_with_default_creds()
    yield dashboard

    # Teadown
    dashboard.top_nav.logout()
    wordpress.quit()

@test
def check_absent_gns_1_max_wait(request, dashboard):
    try:
        b = time.time()
        dashboard.left_nav.gns.wait_until_absent("settings")
    except GuiWidgetForLabelPresentError:
        print(time.time() - b)
        assert time.time() - b > 3
        assert time.time() - b < 5

    try:
        b = time.time()
        dashboard.left_nav.gns.wait_until_absent("settings_max_wait")
    except GuiWidgetForLabelPresentError:
        print(time.time() - b)
        assert time.time() - b > 10
        assert time.time() - b < 12

@test
def check_absent_gns_2_max_wait(request, dashboard):
    try:
        b = time.time()
        dashboard.left_nav.wait_until_absent(link="Settings")
    except GuiWidgetPresentError:
        print(time.time() - b)

    try:
        b = time.time()
        dashboard.left_nav.wait_until_absent(link="Settings", max_wait=10)
    except GuiWidgetPresentError:
        print(time.time() - b)

@test
def check_contains_max_wait_gns_1(request, dashboard):
    b = time.time()
    dashboard.left_nav.gns.contains("non_existing")
    print(time.time() - b)

    b = time.time()
    dashboard.left_nav.gns.contains("non_existing_max_wait")
    print(time.time() - b)

@test
def check_contains_max_wait_gns_2(request, dashboard):
    b = time.time()
    dashboard.left_nav.contains(link="non_existing")
    print(time.time() - b)

    b = time.time()
    dashboard.left_nav.contains(link="non_existing_max_wait", max_wait=10)
    print(time.time() - b)