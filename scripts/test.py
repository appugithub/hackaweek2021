import sys
n = len(sys.argv)
print("Total arguments passed:", n)
print("\n Sys.argv[1]", sys.argv[1])
# Arguments passed
print("\nName of Python script:", sys.argv[0])
print('test1') 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")



