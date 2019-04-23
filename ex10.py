tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list :
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#Escape Sequences
# \\ = backslash (\)
# \' = single-quote (')
#\" = Double-quote (")
#\a = ASCII bell (Bel)
#\b = ASCII backspace (BS)
#\f = ASCII formfeed (FF)
#n = ASCII linefeed (LF)
#\N{name} = Character named name in the unicode database (unicode only)
#\r = Carriage Return (CR)
#\t = Horizontal Tab (Tab)
#\uxxxx = Character with 16-bit hex value xxxx (u"string only)
#\uxxxxxxxx = characher with 32-bit hex value xxxxxxxx (u" string only)
#\v = ASCII Vertical tab (VT)
#\ooo = character with octal value ooo
#\xhh = character with hex value hh
