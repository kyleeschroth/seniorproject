#Kylee Senior Project Data

from ortools.linear_solver import pywraplp

#Create the Data
def create_data_model():
    data = {}
    data['constraint_coeffs'] = [
        #1
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],

        #2
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -12000],

        #3
        [1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, -12000],
        [1, 1, 1, 1, 1, 1, -12000],

        #4
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -2000],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -2000],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -2000],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -2000],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -2000],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -2000],

        #5
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -6000],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -6000],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -6000],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -6000],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -6000],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -6000]
    ]

    data['bounds'] = [
        #1
        -7000,
        -4500,
        -8000,
        -12000,
        -6000,
        -9000,
        -10000,
        -3000,
        -7000,
        -8000,
        -7500,
        -10000,

        #2
        0,
        0,
        0,
        0,
        0,
        0,

        #3
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,

        #4
        0,
        0,
        0,
        0,
        0,
        0,

        #5
        0,
        0,
        0,
        0,
        0,
        0
    ]

    data['obj_coeffs'] = [
        #1
        40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
        40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
        40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
        40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
        40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
        40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40,

        #2
        52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52,
        55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55,
        51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51,
        51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51,
        53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53,
        51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51,

        #3
        60, 60, 60, 60, 60, 60,
        52, 52, 52, 52, 52, 52,
        60, 60, 60, 60, 60, 60,
        55, 55, 55, 55, 55, 55,
        51, 51, 51, 51, 51, 51,
        51, 51, 51, 51, 51, 51,
        60, 60, 60, 60, 60, 60,
        60, 60, 60, 60, 60, 60,
        53, 53, 53, 53, 53, 53,
        51, 51, 51, 51, 51, 51,
        55, 55, 55, 55, 55, 55,
        60, 60, 60, 60, 60, 60,

        #4
        1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500,

        #5
        20000,
        20000,
        20000,
        28000,
        20000,
        28000,

        #6
        11.5, 11.5, 11.5, 11.5, 11.5, 11.5, 11.5, 11.5, 11.5, 11.5, 11.5, 11.5,
        12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5, 12.5,
        9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
        16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,
        6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
        14.5, 14.5, 14.5, 14.5, 14.5, 14.5, 14.5, 14.5, 14.5, 14.5, 14.5, 14.5,

        #7
        5.75, 5.75, 5.75, 5.75, 5.75, 5.75, 5.75, 5.75, 5.75, 5.75, 5.75, 5.75,
        6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25,
        4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5,
        8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        7.25, 7.25, 7.25, 7.25, 7.25, 7.25, 7.25, 7.25, 7.25, 7.25, 7.25, 7.25,

        #8
        3.5, 0, 2, 2, 3, 7, 5.5, 6, 7.5, 8, 5.5, 11,
        6, 2, 4, 0, 6, 4, 7.5, 3, 9, 5, 3.5, 6,
        1.5, 3, 5, 6, 0, 8.5, 4.3, 7.5, 3.2, 9.5, 7.5, 6.5,
        8, 7, 5, 4, 8.5, 0, 9.5, 1, 12.5, 1, 1, 6.5,
        3, 7.5, 8, 9, 3.2, 12.5, 2, 11.5, 0, 13.5, 11.5, 15,
        9, 8, 6, 5, 9.5, 1, 10.5, 1.5, 13.5, 0, 1.8, 5.5,

        #9
        1.75, 0, 1, 1, 1.5, 3.5, 2.75, 3, 3.75, 4, 2.75, 5.5,
        3, 1, 2, 0, 3, 2, 3.75, 1.5, 4.5, 2.5, 1.75, 3,
        0.75, 1.5, 3.5, 3, 0, 4.25, 2.15, 3.75, 1.6, 4.75, 3.75, 5.5,
        4, 3.5, 2.5, 2, 4.25, 0, 4.75, 0.5, 6.25, 0.5, 0.5, 3.25,
        1.5, 3.75, 4, 4.5, 1.6, 6.25, 1, 5.75, 0, 6.75, 5.75, 7.5,
        4.5, 4, 3, 2.5, 4.75, 0.5, 5.25, 0.75, 6.75, 0, 0.9, 2.75
    ]

    data['num_i'] = 6
    data['num_j'] = 12
    data['num_constraints'] = 42

    return data

def main():
    data = create_data_model()

    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Define the variables
    infinity = solver.infinity()

    y = {} #72 total
    y2 = {} #72 total
    y3 = {} #72 total
    t = {} #is 6 total
    tt = {} #is 6 total
    z = {} #js 12 total
    for i in range(1, data['num_i']+1):
        y[i] = {}
        y2[i] = {}
        y3[i] = {}
        t[i] = solver.IntVar(0.0, infinity, 't[%i]' % i)
        tt[i] = solver.IntVar(0.0, infinity, 'tt[%i]' % i)
        for j in range(1, data['num_j']+1):
            y[i][j] = solver.IntVar(0.0, infinity, 'y[%i][%i]' % (i, j))
            y2[i][j] = solver.IntVar(0.0, infinity, 'y2[%i][%i]' % (i, j))
            y3[i][j] = solver.IntVar(0.0, infinity, 'y3[%i][%i]' % (i, j))

    for j in range(1, data['num_j']+1):
        z[j] = solver.IntVar(0.0, infinity, 'z[%i]' % j)

    print('Number of variables =', solver.NumVariables())

    #Define the constraints
    #constraint 1 with 12 constraints with 18 decision variables each
    numj = 12
    numi = 6
    for j in range(numj):
        k = 0
        constraint = solver.RowConstraint(data['bounds'][j], 0, '%i+1' %(k+1))
        for i in range(numi):
            constraint.SetCoefficient(y[i+1][j+1], data['constraint_coeffs'][j][k])
            k += 1
            constraint.SetCoefficient(y2[i+1][j+1], data['constraint_coeffs'][j][k])
            k += 1
            constraint.SetCoefficient(y3[i+1][j+1], data['constraint_coeffs'][j][k])
            k += 1
    current = solver.NumConstraints()

    #constraint 2 with 6 constraints with 13 decision variables
    for i in range(numi):
        constraint = solver.RowConstraint(0, data['bounds'][i+current], '%i+1' %(k+1))
        for j in range(numj):
            constraint.SetCoefficient(y2[i+1][j+1], data['constraint_coeffs'][i+current][j])
        constraint.SetCoefficient(z[i+1], data['constraint_coeffs'][i+current][numj])
    current = solver.NumConstraints()

    #constraint 3 with 12 constraints with 7 decision variables
    for j in range(numj):
        constraint = solver.RowConstraint(0, data['bounds'][j+current], '%i+1' %(k+1))
        for i in range(numi):
            constraint.SetCoefficient(y3[i+1][j+1], data['constraint_coeffs'][j+current][i])
        constraint.SetCoefficient(z[j+1], data['constraint_coeffs'][j+current][numi])
    current = solver.NumConstraints()

    #constraint 4 with 6 constraints with 13 decision variables
    for i in range(numi):
        constraint = solver.RowConstraint(0, data['bounds'][current+i], '%i+1' %(k+1))
        for j in range(numj):
            constraint.SetCoefficient(y[i+1][j+1], data['constraint_coeffs'][i+current][j])
        constraint.SetCoefficient(t[i+1], data['constraint_coeffs'][i+current][numj])
    current = solver.NumConstraints()

    #constraint 5 with 6 constraints with 25 decision variables
    for i in range(numi):
        constraint = solver.RowConstraint(0, data['bounds'][current+i], '%i+1' %(k+1))
        k = 0
        for j in range(numj):
            constraint.SetCoefficient(y2[i+1][j+1], data['constraint_coeffs'][current+i][k])
            k += 1
            constraint.SetCoefficient(y3[i+1][j+1], data['constraint_coeffs'][current+i][k])
            k += 1
        constraint.SetCoefficient(tt[i+1], data['constraint_coeffs'][i+current][k])

    print('Number of constraints = ', solver.NumConstraints())

    #Define the objective function

    objective = solver.Objective()

    m = 0
    #1
    for i in range(numi):
        for j in range(numj):
            objective.SetCoefficient(y[i+1][j+1], data['obj_coeffs'][m])
            k +=1

    #2
    for i in range(numi):
        for j in range(numj):
            objective.SetCoefficient(y2[i+1][j+1], data['obj_coeffs'][m])
            k +=1

    #3
    for j in range(numj):
        for i in range(numi):
            objective.SetCoefficient(y3[i+1][j+1], data['obj_coeffs'][m])
            k +=1

    #4
    for j in range(numj):
        objective.SetCoefficient(z[j + 1], data['obj_coeffs'][m])
        k += 1

    #5
    for i in range(numi):
        objective.SetCoefficient(t[i+1], data['obj_coeffs'][m])
        objective.SetCoefficient(tt[i+1], data['obj_coeffs'][m])
        k += 1

    #6
    for i in range(numi):
        for j in range(numj):
            objective.SetCoefficient(y[i+1][j+1], data['obj_coeffs'][m])
            k += 1

    #7
    for i in range(numi):
        for j in range(numj):
            objective.SetCoefficient(y2[i+1][j+1], data['obj_coeffs'][m])
            objective.SetCoefficient(y3[i+1][j+1], data['obj_coeffs'][m])
            k+=1

    #8
    for i in range(numi):
        for j in range(numj):
            objective.SetCoefficient(y[i+1][j+1], data['obj_coeffs'][m])
            objective.SetCoefficient(y2[i+1][j+1], data['obj_coeffs'][m])
            k += 1

    #9
    for i in range(numi):
        for j in range(numj):
            objective.SetCoefficient(y3[i+1][j+1], data['obj_coeffs'][m])
            k += 1

    objective.SetMaximization()

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Objective value =', solver.Objective().Value())
        for i in range(numi):
            for j in range(numj):
                print(y[i+1][j+1], ' = ', y[i+1][j+1].solution_value())
                print(y2[i+1][j+1], ' = ', y2[i+1][j+1].solution_value())
                print(y3[i+1][j+1], ' = ', y3[i+1][j+1].solution_value())
        for j in range(numj):
            print(z[j+1], ' = ', z[j+1].solution_value())

        print()
        print('Problem solved in %f milliseconds' % solver.wall_time())
        print('Problem solved in %d iterations' % solver.iterations())
        print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
  main()




