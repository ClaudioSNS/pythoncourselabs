
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

# print('p' in 'python')
# print('a' in 'python')
# print('py' in 'python')
# print('pn' not in 'python')
#
# test
# s = 'python'
# if ('p' in s) and ('n' in 'python'):
#     print("pn in python")

from functools import reduce

a = [1, 2, 3, 4]
def sum(a1,a2):
    return a1 + a2

# for x in a:
#     print(x)


res = reduce(sum, a)
print (res)
