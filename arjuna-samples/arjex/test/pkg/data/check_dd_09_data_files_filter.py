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

@test(drive_with=data_file("input_exclude.xls"))
def check_drive_with_excel(request, data):
    request.asserter.assert_equal(int(data.left) + int(data.right), int(data.sum), "Calculation failed.")

@test(drive_with=data_file("input_exclude.txt"))
def check_drive_with_tsv(request, data):
    request.asserter.assert_equal(int(data.left) + int(data.right), int(data.sum), "Calculation failed.")

@test(drive_with=data_file("input_exclude.ini"))
def check_drive_with_ini(request, data):
    request.asserter.assert_equal(int(data.left) + int(data.right), int(data.sum), "Calculation failed.")
