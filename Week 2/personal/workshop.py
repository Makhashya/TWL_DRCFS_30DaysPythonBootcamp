#Import the module directly
import constant
print ('There are currently ' + str(constant.CURRENT_STUDENT_COUNT) + ' numbers of students')
print('There are currently' , constant.CURRENT_STUDENT_COUNT, 'no of students')
print ('There are currently ' + str(constant.CURRENT_MENTOR_COUNT) + ' numbers of mentors')

#import variables from constant
from constant import CURRENT_MENTOR_COUNT, CURRENT_STUDENT_COUNT 
