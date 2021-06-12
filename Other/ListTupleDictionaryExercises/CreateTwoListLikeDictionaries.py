student_list = ["Apple", "Banana", "Cherry"]
student_dict_1={}
student_dict_2={}

#Your code here

#Update the above two dictionaries so they're similar to lists where you can access the values 
#Via positive and negative integers

student_dict_1[0]=student_list[0]
student_dict_1[1]=student_list[1]
student_dict_1[2]=student_list[2]

student_dict_2[-3]=student_list[0]
student_dict_2[-2]=student_list[1]
student_dict_2[-1]=student_list[2]

#This should work
print(student_dict_1[0]) #prints “Apple”
print(student_dict_2[-1]) #prints “Banana”



