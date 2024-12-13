import sys, re, numpy as np, math
# get all numbers
matches = re.findall(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X\=(\d+), Y\=(\d+)", open(sys.argv[1]).read())
print(matches[:5])

l = [((int(a_x),int(a_y)), (int(b_x),int(b_y)), (int(p_x),int(p_y))) for (a_x,a_y,b_x,b_y,p_x,p_y) in matches]
print(l[:5])

def min_presses(a, b, p, cost_a, cost_b):
    # find all m*a + n*y = p solutions
    # # for each of those solutions, determine the minimum cost
    # solutions = set()
    # # convert tuples to numpy for easier arithmetic
    # np_a = np.array(a)
    # np_b = np.array(b)
    # np_p = np.array(p)

    # min solution
    min_solution = math.inf

    # find all possibilities for x-coordinate
    for m in range((p[0] // a[0]) + 1):
        # if gap can be made up with by pressing b button
        remainder_x = (p[0] - (m * a[0]))
        remainder_y = (p[1] - (m * a[1]))
        if remainder_x % b[0] == 0 and remainder_y % b[1] == 0 and (remainder_x // b[0]) == (remainder_y // b[1]):
            n = remainder_x // b[0]
            # print(a,b,p)
            # print(m, n)
            # print(m*np_a, n*np_b, m*np_a + n*np_b)
            if min_solution > (m*cost_a + n*cost_b):
                min_solution = m*cost_a + n*cost_b
    # impossible: no cost
    if min_solution == math.inf: min_solution = 0
    return min_solution
    # print()

def is_integer(f, tol):
    return abs(f - round(f)) <= tol

TOLERANCE = 0.0001

def numpy_method(a, b, p, cost_a, cost_b):
    coeff_mat = np.array([[a[0],b[0]],
                          [a[1],b[1]]])
    sol = np.linalg.solve(coeff_mat,np.array(p))
    # print(sol,float(sol[0]),float(sol[1]))
    if is_integer(sol[0], TOLERANCE) and is_integer(sol[1], TOLERANCE):
        return round(sol[0] * cost_a + sol[1] * cost_b)
    return 0

# part 1
cost = 0
for _,game in enumerate(l):
    min_cost = min_presses(game[0],game[1],game[2],3,1)
    np_cost = numpy_method(game[0],game[1],game[2],3,1)
    # print(_, min_cost)
    cost += min_cost
print(cost)

# part 2
offset = 10000000000000
cost = 0
for _,game in enumerate(l):
    min_cost = numpy_method(game[0],game[1],(game[2][0] + offset, game[2][1] + offset),3,1)
    # print(_,min_cost)
    cost+=min_cost
print(cost)