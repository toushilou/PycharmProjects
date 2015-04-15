from string import Template
s = Template('There are ${howmany} ${lang} Quotation Symbols')
print s.substitute(lang='Python', howmany=3)

user_input = raw_input("Enter your name: ")
print user_input

shoplist = ['apple', 'mango', 'carrot', 'banana']
test = shoplist.pop(1)
print test;
print shoplist