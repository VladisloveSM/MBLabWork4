import numpy as np
import matplotlib.pyplot as plt

points = []
amount = 12000

def deCasteljau(points, t):
    if(len(points) == 1):
        return points[0]
    B1 = [0] * (len(points) - 1)
    B2 = [0] * len(B1)
    for i in range(len(B1)):
        B1[i] = points[i]
        B2[i] = points[i+1]
    return (1-t)*deCasteljau(B1, t) + t*deCasteljau(B2, t)


if __name__ == '__main__':

    with open("data.txt", "r") as file:
        for line in file:
            points.append(line.split())

    x = [0] * len(points)
    y = [0] * len(points)

    for i in range(len(points)):
        points[i][0] = float(points[i][0])
        points[i][1] = float(points[i][1])
        x[i] = points[i][0]
        y[i] = points[i][1]

    plt.plot(x, y, '--', color='black')
    plt.scatter(x, y, color='blue')

    step = 1 / amount
    value = 0

    answerX = [0] * (amount + 1)
    answerY = [0] * len(answerX)

    for i in range(amount+1):
        answerX[i] = deCasteljau(x, value)
        answerY[i] = deCasteljau(y, value)
        value += step

    plt.plot(answerX, answerY, color='red')

    plt.show()

