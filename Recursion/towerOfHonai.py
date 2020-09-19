def moveTower(height, fromPole, toPole, withPole):

    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, fromPole, toPole, withPole)

def moveDisk(fp, tp):
    print("Moving from {} to {}".format(fp,tp))


moveTower(3,"A", "B", "C")