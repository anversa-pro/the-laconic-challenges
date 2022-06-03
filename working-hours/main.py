
def findLongestSingleSlot(leaveTimes):
    idList = [0] * 26
    if len(leaveTimes) == 1:
        return chr(leaveTimes[0][0] + 97)
    previousSlot = 0
    for worker in leaveTimes:
        employeeId = int(worker[0])
        timeSlot = int(worker[1] - previousSlot)
        idList[employeeId] += timeSlot
        previousSlot = int(worker[1])

    employeeId = idList.index(max(idList))
    return chr(employeeId + 97)


if __name__ == '__main__':
    leaveTimesMatrix = [[0, 1], [0, 3], [4, 5], [5, 6], [4, 10]]
    print(findLongestSingleSlot(leaveTimesMatrix))
    leaveTimesMatrix2 = [[0, 3], [20, 5], [2, 6], [15, 7], [9, 8], [19, 9], [24, 10], [4, 12], [3, 13]]
    print(findLongestSingleSlot(leaveTimesMatrix2))
