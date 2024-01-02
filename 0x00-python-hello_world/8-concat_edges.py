#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = " ".join(
        [str[str.index('object'):str.index('programming')+len('programming')],
            str[str.index('with'):str.index('with')+len('with')],
            str[:6]])
print(str)
