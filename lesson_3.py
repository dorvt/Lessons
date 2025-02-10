one_line_string = "Hello"
one_more_line_string = "Hi!"
long_text = """Here you can write
all what you won/
And one more
and more
and more!!!!
"""
""" same as before """
apples = 3
banannas = 4
totl = apples + banannas
diff = apples - banannas
mult = apples * banannas
div = apples / banannas
"""
+   -   *   **  /   //  %   @
<<  >>  &   |       ~   :=
<   >   <=  >=  ==  !=
"""
# Keywors
"""
False   await      else     important   pass
None    breake     except   in          raise
True    class      finally  is          return
and     continue   for      lambda      try
as      def        from     nonlocal    while
assert  del        global   not         whith
async   elif       if       or          yield          
"""
print(1 > 2)  # False
print(1 < 2)  # True
print(1 == 2)  # False

red_apples = True
green_apples = True
result = red_apples + green_apples
print(
    f"Can wqe buy red and green if green {green_apples} and red {red_apples}: {result}"
)

red_apples = False
green_apples = True
result = red_apples + green_apples
print(
    f"Can wqe buy red and green if green {green_apples} and red {red_apples}: {result}"
)

red_apples = True
green_apples = False
result = red_apples + green_apples
print(
    f"Can wqe buy red and green if green {green_apples} and red {red_apples}: {result}"
)

red_apples = False
green_apples = False
result = red_apples + green_apples
print(
    f"Can wqe buy red and green if green {green_apples} and red {red_apples}: {result}"
)

red_apples = True
green_apples = True
result = red_apples or green_apples
print(
    f"Can wqe buy red or green if green {green_apples} and red {red_apples}: {result}"
)

red_apples = False
green_apples = True
result = red_apples or green_apples
print(
    f"Can wqe buy red or green if green {green_apples} and red {red_apples}: {result}"
)

red_apples = True
green_apples = False
result = red_apples or green_apples
print(
    f"Can wqe buy red or green if green {green_apples} and red {red_apples}: {result}"
)

red_apples = False
green_apples = False
result = red_apples or green_apples
print(
    f"Can wqe buy red or green if green {green_apples} and red {red_apples}: {result}"
)


calc = (2 + 3) * 4
print("(2 + 3) * 4= ", calc)

numbers = [0, 1, 2, 3]
item = numbers[0]
print("list item", item)

dictionary = {"apple": "яблуко", "ключ": "значення"}
set_elements = {1, 2, 3, "яблуко", "ключ"}

if calc <= 20:
    print("Tra ta ta")

hello = "Greeeteeeng!!!!!"
print(hello)
print(hello.__len__())
print(len(hello))

a = 2
b = 3

# @decorator

decimal = 42
occtal = 0o52
heximal = 0x2A
biar = 0b101010
print("Diff", decimal, occtal, heximal, biar)
long_number = 1_234_312_424_242
print(long_number)

one_float = 1.23000000000000001
sec_float = 12.3000000000000001
sif_float = 2.0e-3
sif_float2 = 2.0e3
print(sif_float, sif_float2)
if one_float == sec_float / 10:  # unexpected result
    print("pass")

hello = "Greeeteeeeeng!!!!"
print(hello[0])
print(hello[1])
print(hello[2])
print(hello[2:7])
for letter in hello:
    print(letter)

my_list = [1, 2, 3, "How are u?"]
print(my_list[3])
print("len for list", len(my_list))

x = min(1, 2, 3)
y = max(1, 2, 3)
print("min and max", x, y)

year = 2016
event = "Referendum"
print(f"Results of the {year} {event}")

for letter in hello:
    print(letter, end=",")

x = min(1, 2, 3)
y = max(1, 2, 3)
print("min and max", x, y, sep="\t")


query_string = "tooltip, what was shows on display and what should to explain, \
                   about code:"
query_string2 = (
    "tooltip, what was shows on display and what should to explain",
    "about code:",
)

varaiable = input(query_string)
print(varaiable)
varaiable = input(query_string2)
print(varaiable)

out = "Result of the {} text {}".format(year, event)
out2 = "Result of the %i text %s" % (year, event)
print(out, out2)



TASK_START_TEMPLATE = "\n\n---Task {0}---\n"

def print_task(task_number):
    """Функция для вывода заголовка задачи"""
    print(TASK_START_TEMPLATE.format(task_number))

# task 01 == Виправте синтаксичні помилки
print_task(1)
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
print_task(2)
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
print_task(3)
for letter in "Hello world!":
    print(letter)