Evaluation Method: 
Fitness function is sum of squared errors for each test sample.
Therefore, the lower the fitness the better the function.
Thus, 0.0 fitness represents a function which outputs the correct value for every test.
All calculation regesters (r0, r3, r4) are initialized as x_1
Specific method found in comments.

Parent Select:
Tournament style selection of parents and replacements.
Chooses 6 random unique individuals from the population.
Chooses the most fit and least fit individual from the first 3 individuals,
and most fit and least fit from the second 3 individuals
Returns the most fit as the parents and the least fit as the replacements

All other relavent descriptions and methods are in comments of methods.


Final Returned Function:

individual: [['r4', 'r4', '*', 'r3'], ['r0', 'r2', '+', 'r2'], ['r0', 'r0', '+', '1'], ['r0', 'r4', '+', 'r0']]
r4 = x_1 * x_1
r0 = x_2 + x_2
r0 = x_2 + x_2 + 1
r0 = x_1 * x_1 + 2x_2 + 1
function: x_1^2 + 2x_2 + 1
fitness: 0.0


Total Output:

generation 0 : best fitness 41.47 average fitness inf
generation 100 : best fitness 12.77 average fitness 97.16400000000002
generation 200 : best fitness 5.07 average fitness inf
generation 300 : best fitness 5.07 average fitness 1.7976931348623156e+306
generation 400 : best fitness 5.07 average fitness 78.91400000000012
generation 500 : best fitness 5.07 average fitness 61.0154000000001
generation 600 : best fitness 5.07 average fitness 51.291000000000025
generation 700 : best fitness 5.07 average fitness 29.854000000000006
generation 800 : best fitness 5.07 average fitness 90.155
generation 900 : best fitness 5.07 average fitness 20.428000000000004
generation 1000 : best fitness 5.07 average fitness 21.49899999999999
generation 1100 : best fitness 5.07 average fitness 20.76399999999999
generation 1200 : best fitness 5.07 average fitness 1.7976931348623156e+306
generation 1300 : best fitness 5.07 average fitness 22.735000000000014
generation 1400 : best fitness 5.07 average fitness 22.57699999999998
generation 1500 : best fitness 5.07 average fitness 15.59820000000001
generation 1600 : best fitness 5.07 average fitness 21.033299999999986
generation 1700 : best fitness 5.07 average fitness 68.3910999999998
generation 1800 : best fitness 5.07 average fitness 25.95190000000002
generation 1900 : best fitness 5.07 average fitness inf
generation 2000 : best fitness 5.07 average fitness 16.848999999999993
generation 2100 : best fitness 5.07 average fitness 39.141200000000055
generation 2200 : best fitness 5.07 average fitness 24.22719999999998
generation 2300 : best fitness 5.07 average fitness 21.918000000000024
generation 2400 : best fitness 5.07 average fitness 12.37800000000001
generation 2500 : best fitness 5.07 average fitness 22.11499999999999
generation 2600 : best fitness 5.07 average fitness 13.008000000000012
generation 2700 : best fitness 5.07 average fitness 16.893
generation 2800 : best fitness 5.07 average fitness 20.5303
generation 2900 : best fitness 5.07 average fitness 26.292000000000012
generation 3000 : best fitness 5.07 average fitness 13.775100000000004
generation 3100 : best fitness 5.07 average fitness 29.413600000000084
generation 3200 : best fitness 5.07 average fitness 19.758299999999988
generation 3300 : best fitness 5.07 average fitness 27.813000000000038
generation 3400 : best fitness 5.07 average fitness 27.271899999999995
generation 3500 : best fitness 5.07 average fitness 20.08699999999998
generation 3600 : best fitness 5.07 average fitness 16.619999999999976
generation 3700 : best fitness 5.07 average fitness 14.085999999999997
generation 3800 : best fitness 5.07 average fitness 15.47199999999999
generation 3900 : best fitness 5.07 average fitness 29.2053
generation 4000 : best fitness 5.07 average fitness 19.40999999999999
generation 4100 : best fitness 5.07 average fitness 31.31300000000001
generation 4200 : best fitness 5.07 average fitness 1.7976931348623156e+306
generation 4300 : best fitness 5.07 average fitness 17.015099999999983
generation 4400 : best fitness 5.07 average fitness 34.256300000000024
generation 4500 : best fitness 5.07 average fitness 18.837899999999976
generation 4600 : best fitness 5.07 average fitness 1.7976931348623156e+306
generation 4700 : best fitness 5.07 average fitness 28.301500000000047
generation 4800 : best fitness 5.07 average fitness 16.423999999999992
generation 4900 : best fitness 5.07 average fitness 24.5783
generation 5000 : best fitness 5.07 average fitness 18.50519999999999
generation 5100 : best fitness 5.07 average fitness 33.54760000000001
generation 5200 : best fitness 5.07 average fitness 21.357499999999995
generation 5300 : best fitness 5.07 average fitness 15.898300000000008
generation 5400 : best fitness 5.07 average fitness 16.679999999999982
generation 5500 : best fitness 5.07 average fitness 1.7976931348623156e+306
generation 5600 : best fitness 5.07 average fitness 15.152899999999983
generation 5700 : best fitness 5.07 average fitness 17.99999999999999
generation 5800 : best fitness 5.07 average fitness 33.30610000000008
generation 5900 : best fitness 5.07 average fitness 22.567300000000014
generation 6000 : best fitness 5.07 average fitness 16.2613
generation 6100 : best fitness 5.07 average fitness 20.12849999999998
generation 6200 : best fitness 5.07 average fitness 40.95660000000003
generation 6300 : best fitness 5.07 average fitness 38.64340000000007
generation 6400 : best fitness 5.07 average fitness 29.7384
generation 6500 : best fitness 5.07 average fitness 27.68610000000004
generation 6600 : best fitness 5.07 average fitness 29.932300000000044
generation 6700 : best fitness 5.07 average fitness 63.16300000000007
generation 6800 : best fitness 5.07 average fitness 24.94130000000002
generation 6900 : best fitness 5.07 average fitness 28.53160000000001
generation 7000 : best fitness 5.07 average fitness 45.86159999999993
generation 7100 : best fitness 5.07 average fitness 52.84300000000002
generation 7200 : best fitness 3.72 average fitness 30.3484
generation 7300 : best fitness 3.72 average fitness 19.86429999999999
generation 7400 : best fitness 3.72 average fitness 33.494200000000056
generation 7500 : best fitness 3.0 average fitness 16.831400000000006
generation 7600 : best fitness 2.93 average fitness 1.7976931348623156e+306
generation 7700 : best fitness 2.93 average fitness 1.7976931348623156e+306
generation 7800 : best fitness 2.93 average fitness 34.61550000000004
generation 7900 : best fitness 2.67 average fitness 9.45070000000001
generation 8000 : best fitness 2.66 average fitness 56.88899999999994
generation 8100 : best fitness 0.0 average fitness 31.289
generation 8200 : best fitness 0.0 average fitness 17.971500000000002
generation 8300 : best fitness 0.0 average fitness 16.0679
generation 8400 : best fitness 0.0 average fitness 21.7289
generation 8500 : best fitness 0.0 average fitness 44.47970000000001
generation 8600 : best fitness 0.0 average fitness 18.27470000000001
generation 8700 : best fitness 0.0 average fitness 6117.823400000001
generation 8800 : best fitness 0.0 average fitness 24.2766
generation 8900 : best fitness 0.0 average fitness 56.709999999999994
generation 9000 : best fitness 0.0 average fitness 20.4046
generation 9100 : best fitness 0.0 average fitness 16.532899999999998
generation 9200 : best fitness 0.0 average fitness 25.710800000000003
generation 9300 : best fitness 0.0 average fitness 34.1534
generation 9400 : best fitness 0.0 average fitness 30.181000000000004
generation 9500 : best fitness 0.0 average fitness 8748.542499999994
generation 9600 : best fitness 0.0 average fitness 673.8591000000004
generation 9700 : best fitness 0.0 average fitness 21.5513
generation 9800 : best fitness 0.0 average fitness 40.1171
generation 9900 : best fitness 0.0 average fitness 43.3157
generation 10000 : best fitness 0.0 average fitness 31.514400000000002
best individual: [['r4', 'r4', '*', 'r3'], ['r0', 'r2', '+', 'r2'], ['r0', 'r0', '+', '1'], ['r0', 'r4', '+', 'r0']]
best fitness: 0.0