"""
Jumping statements
used to alter the flow of loops

1. break statement
    to break out of a loop
    when encounter a loop the execution of loop breaks and program control comes out of the loop

"""
sum = 0
for i in range(1, 100):
    if sum >= 100:
        break
    sum += i
print(i)

"""
2. continue
to skip an execution of a loop
if encounters a continue statement, the exection skips the rest of the code under that continue statement inide the loop and 
jumps to the next iteration of the loop
"""
for i in range(1, 10):
    if i == 5:
        continue 
    print(i)