nums = [10, 20, 30, 20]

print(nums[0])   # 10
nums[1] = 100
print(nums)      # [10, 100, 30, 20]



#####################################

nums = (10, 20, 30)

print(nums[1])   # 20


##################################
nums = {10, 20, 30, 20}

print(nums)   # {10, 20, 30}
nums.add(40)
print(nums)   # {10, 20, 30, 40}

###################################

student = {
    "name": "Rama",
    "age": 21
}

print(student["name"])   # Rama
student["age"] = 22
print(student)           # {'name': 'Rama', 'age': 22}

######################################


