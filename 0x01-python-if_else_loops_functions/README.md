# 0x01. Python - if/else, loops, functions
___
#### More Control Flow Tools
> match Statements: If you’re comparing the same value to several constants, or checking for specific types or attributes

> The break statement breaks out of the innermost enclosing for or while loop.

> In a for loop, the else clause is executed after the loop reaches its final iteration.

> In a while loop, it’s executed after the loop’s condition becomes false.

> In either kind of loop, the else clause is not executed if the loop was terminated by a break.

**3-print_alphabt.py**
```sh
print('{:c}'.format(i if i != 101 and i != 113 else 0), end='')
```

**5-print_comb2.py**
```sh
for i in range(100):
	end = ', ' if i != 99 else '\n'
	print(f'{i:0>2d}', end=', ')  
```
