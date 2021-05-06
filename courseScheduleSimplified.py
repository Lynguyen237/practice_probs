'''
Find the middle course given a nested array of classes. Each subarr is a pair of classes
where the first class the the prerequisite of the second class.

prereq = [
	    ["Data", "Algo"],
        ["Prep", "Data"],
        ["Algo", "Graduate"]
]
A student would need to finish the course in this order: Prep, Data, Algo, Graduate
Given that a student is midway thru the course, what's the course they should be taking now.
If there are two mid courses, return the first one.

The input will have at least one pair of classes

Related challenge: https://leetcode.com/problems/course-schedule/
'''
prereq = [
	    ["Data", "Algo"],
        ["Prep", "Data"],
        ["Algo", "Graduate"]
]

def findMidClass(prereq):

    classDict = {}
    beg_end_classes = set()

    for classPair in prereq:
        firstClass, secondClass = classPair[0], classPair[1]
        classDict[firstClass] = secondClass

        if firstClass not in beg_end_classes:
            beg_end_classes.add(firstClass)
        else:
            beg_end_classes.remove(firstClass)
        if secondClass not in beg_end_classes:
            beg_end_classes.add(secondClass)
        else:
            beg_end_classes.remove(secondClass)

    firstClass = beg_end_classes.pop()
    if firstClass not in classDict:
        firstClass = beg_end_classes.pop()

    mid_idx = (len(classDict)+1)//2 - 1

    track = [firstClass]
    count = 0
    while track[-1] in classDict and count < mid_idx:
        count += 1
        track.append(classDict[track[-1]])

    return track[-1]

print(findMidClass(prereq)) #Prep, Data, Algo, Graduate