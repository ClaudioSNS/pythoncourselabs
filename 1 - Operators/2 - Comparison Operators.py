
'''
Copyright 2021-2022 Agnese Salutari.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License
'''

x = int(input("x = "))

# print(x > 0)
# print(x < 0)
# print(x == 0)
# print(x != 0)
# print(x >= 0)
# print(x <= 0)
#
# ToDo: Use if statements to make more detailed prints.
# if (x > 0):
#     print(f"{x} > 0")
# if (x < 0):
#     print(f"{x} < 0")
# if (x == 0):
#     print(f"{x} = 0")
# ToDo: Check if x in in one of the following intervals: [-2, 5], (10, 100], (200, 300)
if (x >= -2) and (x <= 5):
    print(f"{x} compreso in [-2, 5]")
if (x > 10) and (x <= 100):
    print(f"{x} compreso in (10, 100]")
if (x > 200) and (x < 300):
    print(f"{x} compreso in (200, 300)")
# if ((x >= -2) and (x <= 5)) or ((x > 10) and (x <= 100)) or ((x > 200) and (x < 300)):
#     print(f"{x} compreso in range")
# else:
#     print(f"{x} non compreso in range")
if -2 <= x <= 5 or 10 < x <= 100 or 200 < x < 300:
    print(f"{x} compreso in range")
else:
    print(f"{x} non compreso in range")