#Wes-McKinney : Python for Data Analysis --- Data Wrangling with pandas NumPy and Jupyter OReilly Media (2022)
#Chapter 2







#This is not allowed
#   "5"+5











#####The attributes and methods of an object in Python#####


# Example(do this in Jupyter)       Note: Jupyter automatically operates display the return of the last line if it's a expression, while interpreters like vscode doesn't do this.
a = "foo"
#a.  #<Press Tab> here, and you'll see the attributes and methods



###Boolean tests###

"123".isdigit()     # True   #whether all digits
"abc".isalpha()     # True   #whether all letters
"abc123".isalnum()  # True   #wheter all digits/letters
"   ".isspace()     # True   #wheter all whitespaces
"1D".isdecimal()    # False  #wheter decimal十进制数
"1".isdecimal()    # True
"12a".isnumeric()    # False  #wheter all numeric数值字符
"12".isnumeric()    # True

"Abc".islower()     #是否全小写
"Abc".isupper()	#是否全大写
"Hello world".istitle()	#是否是 title 格式

"var_name".isidentifier()  # True   #valid identifier;是否是合法 Python 变量名











###Searching & Replacement###

"hello".find("l")   # 2     from left to right and find the lowest index of substring
"hello".find("a")   # -1
"hello".rfind("l")  # 3     from right to left

"hello".index("l")  # 2
"hello".rindex("l")  # 3

"banana".count("a")  # 3

"hello.py".startswith("h")  # True
"hello.py".endswith(".py")  # True

a="hello world"
b=a.replace("world", "Python")  #replace world with Python, return the new one, keep a unchanged
print(a,b)

"unhappy".removeprefix("un")        #happy
"unhappy.py".removesuffix(".py")        #unhappy











###Whitespace trimming 去空白 & Alignment(对齐与补充)###

"  hi  ".strip()  # 'hi'
"  hi  ".lstrip()  # 'hi  '
"  hi  ".rstrip()  # '  hi'

"hi".center(10, "-")        #'----hi----'
"hi".ljust(10, "-")         #'hi--------'
"hi".rjust(10, "-")         #'--------hi'










###Split & Join###

"a,b,c".split(",")      #['a', 'b', 'c']
"a,b,c".split(",",1)      #['a', 'b,c']
"a,b,c".rsplit(",")      #['a', 'b', 'c']
"a,b,c".rsplit(",",1)      #['a,b', 'c']


"text\ntext".splitlines()       #['text', 'text']

"a=b=c".partition("=")      # ('a', '=', 'b=c')     #split the string at the first occurrence of sep
"a=b=c".rpartition("=")      # ('a=b', '=', 'c')

",".join(["a", "b", "c"])       #'a,b,c'











###Encoding & Formatting###

"Abc".upper()   # 'ABC'
"Abc".lower()   # 'abc'

"hello world".capitalize()  # 'Hello world'

"hello world".title()   # 'Hello World'

"AbC".swapcase()    # 'aBc'

"ß".casefold()      #ss     #aggressive lowercase for comparisons

"你好".encode("utf-8")      #b'\xe4\xbd\xa0\xe5\xa5\xbd'        #str -> bytes

table = str.maketrans("abc", "123")         #table = {97: 49, 98: 50, 99: 51}
"abc".translate(table)          #'123'
"bc".translate(table)          #'23'        #translate according to the table


"Hello {}".format("world")          #"Hello {}" is a template string; fill {} with world
"{1} {0}".format("world", "Hello")      #"Hello world"
"{} + {} = {}".format(1, 2, 3)      #"1 + 2 = 3"

val = "español"
val_utf8 = val.encode("utf-8")      # b'espa\xc3\xb1ol'
val_utf8.decode("utf-8")










###Binary Operators

int(False)      # 0
bool(0j)        # False         only numeric zero(0.0 / 0j / 0), empty string, empty containers(len==0), None, False become False
#But!!!
bool("False")        # True
bool("True")        # True

a is b      #True if a and b reference the same Python object

5 // 2     # 2      #floor division
-5 // 2    # -3 （不是 -2）

2 ** 3     # 8
4 ** 0.5   # 2.0
2 ** -1    # 0.5

#bitwise AND
a = 6      # 110
b = 3      # 011
a & b      # 2  (010)

#bitwise OR
a = 6   # 110
b = 3   # 011
a | b   # 7 (111)

#Boolean XOR
True ^ True     # False
True ^ False    # True
False ^ True    # True
False ^ False   # False

#bitwise XOR
a = 6   # 110
b = 3   # 011
a ^ b   # 5 (101)

###Note: and/or --- shortcircuit evaluation
a and b         #if a is false, return false, care not about b













#For multiline strings with line breaks, you can use triple quotes, either ''' or """:

c = """
This is a longer string that
spans multiple lines
"""         # this string c actually contains four lines of text
c.count("\n")           # 3


#Python strings are immutable;

a = "this is a string"
#a[10]="f"           # TypeError: 'str' object does not support item assignment

b = a.replace("string", "longer string")
print(b)   # this is a longer string

a = 5.63     #integer
s=str(a)        #string
type(s)
list(s)     #['5', '.', '6', '3']
s[:3]       #'5.6'      #slicing

#escape character

s = "12\\34"        # 12\34
s = "12\%34"        # 12%34


s = r"this\has\no\special\characters"       # this\has\no\special\characters

template = "{0:.2f} {1:s} are worth US${2:d}"
template.format(88.46, "Argentine Pesos", 1)        # '88.46 Argentine Pesos are worth US$1'
















##### Dates and times #####

from datetime import datetime, date, time

dt = datetime(2026, 1, 15, 20, 26, 36)      # datetime.datetime is an immutable type
print(dt.minute)

date = dt.date()
time = dt.time()

dt.strftime("%Y-%m-%d %H:%M")       # '2026-01-15 20:26'

dt2 = datetime.strptime("20251001", "%Y%m%d")

ddt = dt - dt2      # 106 days, 20:26:36   (106 days and 20 hours and 26 minutes and 36 seconds)

dt3 = dt + ddt      # 2026-05-02 16:53:12















#####Control Flow#####

# if - elif - else
# for - if - break
# for i in range
# range(0,10)         0,1,...,9
# for value in list
# while - break

# Since Python uses whitespace to delimit blocks, we need "pass" as a placeholder. Pass = do nothing

x=0
if x < 0:
 print("negative!")
elif x == 0:
 # TODO: put something smart here
 pass
else:
 print("positive!")











