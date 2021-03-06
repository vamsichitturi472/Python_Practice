"""
this will find mean value and standard deviation 
    and finds minimum values and maximum values based on those. 
any point greater then maximum or lesser then minimum will be an outlier
"""

from matplotlib.pyplot import legend, plot, scatter, show, title
from numpy import append, array, mean, std
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":
    HEIGHT = array([
        58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
        76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86
    ])
    WEIGHT = array([
        115, 117, 120, 123, 126, 129, 132, 135, 139, 142, 146, 150, 154, 159,
        164, 164, 168, 171, 175, 178, 182, 185, 188, 192, 195, 199, 202, 206,
        209
    ])

    HEIGHT_MEAN = mean(HEIGHT)
    HEIGHT_STD = std(HEIGHT)
    HEIGHT_UPPER_BOUND = HEIGHT_MEAN + HEIGHT_STD
    HEIGHT_LOWER_BOUND = HEIGHT_MEAN - HEIGHT_STD

    WEIGHT_MEAN = mean(WEIGHT)
    WEIGHT_STD = std(WEIGHT)
    WEIGHT_UPPER_BOUND = WEIGHT_MEAN + WEIGHT_STD
    WEIGHT_LOWER_BOUND = WEIGHT_MEAN - WEIGHT_STD

    valid_points = array([], dtype='int')
    invalid_points = array([], dtype='int')

    for i in range(len(HEIGHT)):
        if ((HEIGHT_LOWER_BOUND < HEIGHT[i] < HEIGHT_UPPER_BOUND)
                and (WEIGHT_LOWER_BOUND < WEIGHT[i] < WEIGHT_UPPER_BOUND)):
            valid_points = append(valid_points, [[HEIGHT[i], WEIGHT[i]]])
        else:
            invalid_points = append(invalid_points, [[HEIGHT[i], WEIGHT[i]]])

    valid_points.shape = (int(len(valid_points) / 2), 2)
    invalid_points.shape = (int(len(invalid_points) / 2), 2)

    scatter(
        valid_points[:, 0],
        valid_points[:, 1],
        marker="o",
        color="blue",
        label="Valid Points")
    scatter(
        invalid_points[:, 0],
        invalid_points[:, 1],
        marker="*",
        color="red",
        label="Invalid Points")

    valid_x = valid_points[:, 0]
    valid_x.shape = (len(valid_x), 1)
    valid_y = valid_points[:, 1]

    Linear_Model = LinearRegression()
    Linear_Model.fit(valid_x, valid_y)

    coef = Linear_Model.coef_
    intercept = Linear_Model.intercept_

    plot(
        valid_x,
        Linear_Model.predict(valid_x),
        color="blue",
        label="Valid Line")

    Experimental_Boundary_Points = array(
        [[min(valid_x), min(valid_x * coef + intercept * 0.5)], [
            min(valid_x), min(valid_x * coef + intercept * 1.5)
        ], [max(valid_x), max(valid_x * coef + intercept * 1.5)],
         [max(valid_x), max(valid_x * coef + intercept * 0.5)],
         [min(valid_x), min(valid_x * coef + intercept * 0.5)]])

    plot(
        Experimental_Boundary_Points[:, 0],
        Experimental_Boundary_Points[:, 1],
        color="grey",
        label="Experimental Boundary")

    Boundary_Points = array([[HEIGHT_LOWER_BOUND, WEIGHT_LOWER_BOUND], [
        HEIGHT_UPPER_BOUND, WEIGHT_LOWER_BOUND
    ], [HEIGHT_UPPER_BOUND,
        WEIGHT_UPPER_BOUND], [HEIGHT_LOWER_BOUND, WEIGHT_UPPER_BOUND],
                             [HEIGHT_LOWER_BOUND, WEIGHT_LOWER_BOUND]])

    plot(
        Boundary_Points[:, 0],
        Boundary_Points[:, 1],
        color="red",
        label="Working Boundary")
    plot(
        [HEIGHT_MEAN, HEIGHT_MEAN], [WEIGHT_LOWER_BOUND, WEIGHT_UPPER_BOUND],
        color="orange",
        label="Mean Lines")
    plot(
        [HEIGHT_LOWER_BOUND, HEIGHT_UPPER_BOUND], [WEIGHT_MEAN, WEIGHT_MEAN],
        color="orange",
        label="Mean Lines")

    title("Anomaly Detection")
    legend()
    show()
