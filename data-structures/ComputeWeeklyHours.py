'''
Each records an employees 7 day work week
7 columns


'''

def main():


    workHours = [
        [2,4,3,4,5,8,8]
        [5,6,9,8,4,2,1]
        [5,3,6,2,1,4,5]
        [5,1,4,2,3,6,2]
        [5,2,5,6,9,5,2]
        [2,3,6,5,4,1,2]
        [5,2,1,0,3,6,5]
        [1,2,3,6,5,4,2]]

        weeklyHours = []

        for i in range(len(workHours)):

            weeklyHours.append([sum(workHours[i]),i))

            weeklyHours.sort()


        for employeeHours in weeklyHours:
            print(f" Employee ID# {employeeHours[1]}: Hours: {emplyeeHours[0]}")

main()
