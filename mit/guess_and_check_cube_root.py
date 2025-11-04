# Guess and Check algorithm to find if an input number is a perfect square, using also boolean flags.

cube = int(input("Enter a number: "))
print(f"Let's check if {cube} is a perfect cube.")
print("Loading...........")

i = 1
while i**3 < N:
    i += 1
if i**3 == N:
    print(i)
else:
    print('error')

# found = False
# for i in range(abs(cube)+1):
#     if i**3 == abs(cube):
#         if cube < 0:       
#             i = -i 
#         print(f"{cube} is a perfect cube and its cube root is {i}.")
#         found = True
#         break
#     elif i**3 > cube:
#         break

# if not found:
#     print(f"{cube} is not a perfect cube!")

