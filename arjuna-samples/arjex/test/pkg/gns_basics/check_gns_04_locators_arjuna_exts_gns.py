# This file is a part of Arjuna
# Copyright 2015-2020 Rahul Verma

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

@for_test
def wordpress(request):
    # Setup
    wp_url = C("wp.login.url")
    wordpress = GuiApp(url=wp_url, label="ArjunaExtended", gns_dir="gns_basics")
    wordpress.launch()
    yield wordpress

    # Teadown
    wordpress.quit()

@test
def check_arjuna_exts_gns(request, wordpress):

    # Based on partial text
    element = wordpress.gns.lost_pass_text

    # Based on Full Text
    element = wordpress.gns.lost_pass_ftext

    # Based on Title
    element = wordpress.gns.lost_pass_title

    # Based on Value
    element = wordpress.gns.user_value

    # Based on partial match of content of an attribute
    element = wordpress.gns.user_attr
    print(element.source.content.root)

    # Based on full match of an attribute
    element = wordpress.gns.user_fattr
    print(element.source.content.root)

    # Based on tags
    element = wordpress.gns.form_tags_str
    element = wordpress.gns.form_tags_list
    element = wordpress.gns.any_tags_list
    print(element.source.content.root)

    # Based on compound classes
    element = wordpress.gns.button_classes_str
    element = wordpress.gns.button_classes_list

    # Based on Point (location in terms of X,Y co-ordinates)
    element = wordpress.gns.elem_xy

    # With Javascript
    element = wordpress.gns.elem_js

    # With.NODE
    element = wordpress.gns.user_node
    element = wordpress.gns.user_node_tag
    element = wordpress.gns.user_node_multi
    element = wordpress.gns.user_bnode
    element = wordpress.gns.user_bnode_tag
    element = wordpress.gns.user_bnode_multi
    element = wordpress.gns.user_fnode
    element = wordpress.gns.user_fnode_tag
    element = wordpress.gns.user_fnode_multi
    element = wordpress.gns.body_node_1
    element = wordpress.gns.body_node_2