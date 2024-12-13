# numbers to the numbers that must be afer it
num_to_after = {}
middle_vals = 0
middle_vals_part_2 = 0

def goal_test(l):
    # if len(l[1]) == 0:
        for n, i in enumerate(l):
            for j in l[n+1:]:
                if i in num_to_after[j]:
                    return False
        return True
    # return False

def get_next_unassigned_var(l):
    maxl = ''
    maxc = -1
    # look through unassigned
    for i in l[1]:
        # find most constrained variable - one with most elements after it
        c = len(num_to_after[i])
        if c > maxc:
            maxl = i
            maxc = c
    return maxl # returns maximum element

def newst(state, var):
    # returns new list state
    a = state.copy()
    # add to list, pop off unassigned
    a[0]+=(var,)
    a[1] = tuple(i for i in a[1] if i!=var)
    return a

# let state be a list containing the current list and list of remaining elements
def csp_backtracking(state):
    if goal_test(state): 
        return state
    # var = get_next_unassigned_var(state)
    # if var:
    for var in state[1]:
        new_state = newst(state,var)
        result = csp_backtracking(new_state)
        if result != None:
            return result
    return None


for i in open('input.txt').readlines(): 
    i = i.strip()
    # section 1
    if i.find('|') >= 0:
        b = i.split('|')
        if b[0] not in num_to_after:
            num_to_after[b[0]] = {b[1]}
        else:
            num_to_after[b[0]].add(b[1])
    # section 2
    elif i.find(',') >= 0:
        # part 1
        l = i.split(',')
        correct = goal_test(l)
        
        if correct:
            middle_vals += int(l[len(l)//2])
        else:
            # part 2
            # resort?
            while not goal_test(l):
                changed = False
                for n, i in enumerate(l):
                    for j in l[n+1:]:
                        if i in num_to_after[j]:
                            l.remove(i)
                            l.append(i)
                            changed = True
                        if changed:
                            break
                    if changed:
                        break

            # final_list, _ = csp_backtracking([(), tuple(l)]) 
            print(l)
            middle_vals_part_2+=int(l[len(l)//2])
            
# for i in (num_to_after):
#     print(i,'\t',sorted(num_to_after[i]))
print(middle_vals)
print(middle_vals_part_2)