
def findLowestStartingStair(jumps):
    staringStair = 1
    endingStair = 0
    while endingStair < 1:
        endingStair = staringStair
        for jump in jumps:
            endingStair += jump
            if endingStair < 1:
                pass
        staringStair += 1

    return staringStair


if __name__ == '__main__':
    jumpsList = [10, -5, 4, -2, 3, 1, -1, -6, -1, 0, 5]
    print(findLowestStartingStair(jumpsList))
