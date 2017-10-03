import pandas as pd

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])

staff_df = staff_df.set_index('Name')

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])

student_df = student_df.set_index('Name')


outer_join = pd.merge(staff_df,student_df,how = 'outer',left_index = True, right_index = True );


print outer_join

inner_join = pd.merge(staff_df,student_df,how = 'inner',left_index = True, right_index = True );

print '-' * 50
print inner_join

left_join = pd.merge(staff_df,student_df,how = 'left',left_index = True, right_index = True );

print '-' * 50
print left_join

right_join = pd.merge(staff_df,student_df,how = 'right',left_index = True, right_index = True );

print '-' * 50
print right_join



staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR','Location': 'abc' },
                         {'Name': 'Sally', 'Role': 'Course liasion','Location': 'xyz'},
                         {'Name': 'James', 'Role': 'Grader','Location': 'syz'}])

#staff_df = staff_df.reset_index()

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business','Location': 'syz'},
                           {'Name': 'Mike', 'School': 'Law','Location': 'kkk'},
                           {'Name': 'Sally', 'School': 'Engineering','Location': 'xyz'}])

#student_df = student_df.reset_index()


# Join/Merging using column

left_join = pd.merge(staff_df,student_df,how = 'left',left_on = 'Name', right_on = 'Name' );



print '-' * 50
print left_join