from param_wrapper import TranspTaskInfo
class NorthWestMethod: 
    def getNext(self, parameters: TranspTaskInfo) -> tuple[int, int]:
        '''
        Returns the next cell (row, col) to consider in a transportaion task according to the noth-west method.
        '''
        costs, _, _, blocked_rows, blocked_cols = parameters.unpack()

        res_row = next(x for x in range(len(costs)) if x not in blocked_rows)
        res_col = next(y for y in range(len(costs[0])) if y not in blocked_cols)
        return (res_row, res_col)
