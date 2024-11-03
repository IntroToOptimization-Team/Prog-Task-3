class TranspTaskInfo:
    '''
    A wrapper for given variables of transporation problem.
    '''

    def __init__(self, costs: list[list[int]],
                 supply: list[int],
                 demand: list[int],
                 blocked_rows: list[int] = [],
                 blocked_cols: list[int] = []) -> None:
        self.costs = costs
        self.supply = supply
        self.demand = demand

        #Indicate that a row is out of consideration
        self.blocked_rows = blocked_rows
        #Indicate that a column is out of consideration
        self.blocked_cols = blocked_cols



    def unpack(self):
        '''
        Returns a tuple of costs, supply, demand, blocked_rows, blocked_cols.
        '''
        return (self.costs, self.supply, self.demand,
                self.blocked_rows, self.blocked_cols)
