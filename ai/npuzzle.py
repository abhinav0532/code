import random
class State:

    def __init__(self, nsize):
        self.nsize = nsize
        self.tsize = pow(self.nsize, 2)
        self.goal = list(range(1, self.tsize))
        self.goal.append(0)

    def printst(self, st):
        for (index, value) in enumerate(st):
            print(' %s ' % value, end=' ') 
            if index in [x for x in range(self.nsize - 1, self.tsize, 
                         self.nsize)]:
                print() 
        print() 

    def getvalues(self, key):
        values = [1, -1, self.nsize, -self.nsize]
        valid = []
        for x in values:
            if 0 <= key + x < self.tsize:
                if x == 1 and key in range(self.nsize - 1, self.tsize, 
                        self.nsize):
                    continue
                if x == -1 and key in range(0, self.tsize, self.nsize):
                    continue
                valid.append(x)
        return valid

    def expand(self, st):
        pexpands = {}
        for key in range(self.tsize):
            pexpands[key] = self.getvalues(key)
        pos = st.index(0)
        moves = pexpands[pos]
        expstates = []
        for mv in moves:
            nstate = st[:]
            (nstate[pos + mv], nstate[pos]) = (nstate[pos], nstate[pos + 
                    mv])
            expstates.append(nstate)
        return expstates

    def one_of_poss(self, st):
        exp_sts = self.expand(st)
        rand_st = random.choice(exp_sts)
        return rand_st

    def start_state(self, seed=1000):
        start_st = (self.goal)[:]
        for sts in range(seed):
            start_st = self.one_of_poss(start_st)
        return start_st

    def goal_reached(self, st):
        return st == self.goal

    def manhattan_distance(self, st):
        mdist = 0
        for node in st:
            if node != 0:
                gdist = abs(self.goal.index(node) - st.index(node))
                (jumps, steps) = (gdist // self.nsize, gdist % self.nsize)
                mdist += jumps + steps
        return mdist

    def huristic_next_state(self, st):
        exp_sts = self.expand(st)
        mdists = []
        for st in exp_sts:
            mdists.append(self.manhattan_distance(st))
        mdists.sort()
        short_path = mdists[0]
        if mdists.count(short_path) > 1:
            least_paths = [st for st in exp_sts if self.manhattan_distance(st) == short_path]
            return random.choice(least_paths)
        else:
            for st in exp_sts:
                if self.manhattan_distance(st) == short_path:
                    return st

    def solve_it(self, st):
        while not self.goal_reached(st):
            st = self.huristic_next_state(st)
            self.printst(st)


if __name__ == '__main__':
    print('N-Puzzle Solver!')
    print(10 * '-')
    state = State(3)
    print('The Starting State is:')
    start = state.start_state(5)
    state.printst(start)
    print('The Goal State should be:')
    state.printst(state.goal)
    print('Here it Goes:')
    state.printst(start)
    state.solve_it(start)

