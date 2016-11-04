# -*- coding: utf-8 -*-
import re

print '#'*6 + 're.compile(string[,flag])' + '#'*6
print '将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串'

pattern = re.compile(r'hello')


print '#'*6 + 're.match(pattern, string[, flags])' + '#'*6
print '只匹配开头，匹配成功立即终止，不再向后匹配'

# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'hello')

# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo CQC!')
result3 = re.match(pattern, 'helo CQC!')
result4 = re.match(pattern, 'hello CQC!')

# 如果1匹配成功
if result1:
    # 使用Match获得分组信息
    print result1.group()
else:
    print '1匹配失败！'

# 如果2匹配成功
if result2:
    # 使用Match获得分组信息
    print result2.group()
else:
    print '2匹配失败！'

# 如果3匹配成功
if result3:
    # 使用Match获得分组信息
    print result3.group()
else:
    print '3匹配失败！'

# 如果4匹配成功
if result4:
    # 使用Match获得分组信息
    print result4.group()
else:
    print '4匹配失败！'


print '#'*6 + 'Match对象' + '#'*6
print '属性：'
print '1.string: 匹配时使用的文本。'
print '2.re: 匹配时使用的Pattern对象。'
print '3.pos: 文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。'
print '4.endpos: 文本中正则表达式结束搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。'
print '5.lastindex: 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。'
print '6.lastgroup: 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。'
print '方法：'
print '1.group([group1, …]):'
print '获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。'
print '2.groups([default]):'
print '以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。'
print '3.groupdict([default]):'
print '返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。'
print '4.start([group]):'
print '返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。'
print '5.end([group]):'
print '返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。'
print '6.span([group]):'
print '返回(start(group), end(group))。'
print '7.expand(template):'
print '将匹配到的分组代入template中然后返回。template中可以使用\id或\g、\g引用分组，但不能使用编号0。\id与\g是等价的；但\10将被认为是第10个分组，如果你想表达\1之后是字符’0’，只能使用\g0。'

# 一个简单的match实例

# 匹配如下内容：单词+空格+单词+任意字符
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
print "m.group():", m.group()
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')

print '#'*6 + 're.search(pattern, string[, flags])' + '#'*6
print '扫描整个string查找匹配'

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'world')
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match = re.search(pattern,'hello world!')
if match:
    # 使用Match获得分组信息
    print match.group()
### 输出 ###
# world

print '#'*6 + 're.split(pattern, string[, maxsplit])' + '#'*6
print '按照能够匹配的子串将string分割后返回列表。maxsplit用于指定最大分割次数，不指定将全部分割'

pattern = re.compile(r'\d+')
print re.split(pattern, 'one1two2three3four4')

### 输出 ###
# ['one', 'two', 'three', 'four', '']

print '#'*6 + 're.findall(pattern, string[, flags])' + '#'*6
print '搜索string，以列表形式返回全部能匹配的子串。我们通过这个例子来感受一下'

pattern = re.compile(r'\d+')
print re.findall(pattern, 'one1two2three3four4')

### 输出 ###
# ['1', '2', '3', '4']

print '#'*6 + 're.finditer(pattern, string[, flags])' + '#'*6
print '搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器'

pattern = re.compile(r'\d+')
for m in re.finditer(pattern, 'one1two2three3four4'):
    print m.group(),

### 输出 ###
# 1 2 3 4

print '#'*6 + 're.sub(pattern, repl, string[, count])' + '#'*6
print '使用repl替换string中每一个匹配的子串后返回替换后的字符串。'
print '当repl是一个字符串时，可以使用\id或\g、\g引用分组，但不能使用编号0。'
print '当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。'
print 'count用于指定最多替换次数，不指定时全部替换。'

pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print re.sub(pattern, r'\2 \1', s)


def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()


print re.sub(pattern, func, s)

### output ###
# say i, world hello!
# I Say, Hello World!

print '#'*6 + 're.subn(pattern, repl, string[, count])' + '#'*6
print '返回 (sub(repl, string[, count]), 替换次数)'

pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print re.subn(pattern, r'\2 \1', s)


def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()


print re.subn(pattern, func, s)

### output ###
# ('say i, world hello!', 2)
# ('I Say, Hello World!', 2)