from param_wrapper import TranspTaskInfo
class RusselMethod:
    def getAvailableIndexes(self, n: int, blocked: list[int]) -> list[int]:
        '''
        Returns the list of indexes in [0, n) that aren't blocked.
        '''
        return [i for i in range(n) if i not in blocked]



    def getNext(self, parameters: TranspTaskInfo) -> tuple[int, int]:
        '''
        Returns the next cell to consider in a transportaion task according to the russel's method.
        '''
        costs, _, _, blocked_rows, blocked_cols = parameters.unpack()
        n = len(costs)
        m = len(costs[0])

        available_rows = self.getAvailableIndexes(n, blocked_rows)
        available_cols = self.getAvailableIndexes(m, blocked_cols)

        U_vector,V_vector = [0] * len(costs), [0] * len(costs[0])
        for row in available_rows:
            cur_row = costs[row]
            U_vector[row] = max(cur_row[col] for col in available_cols)

        transposed_costs = list(zip(*costs))
        for col in available_cols:
            cur_col = transposed_costs[col]
            V_vector[col] = max(cur_col[row] for row in available_rows)


        res_row = available_rows[0]
        res_col = available_cols[0]
        max_val = costs[res_row][res_col]
        for row in available_rows:
            for col in available_cols:
                value = U_vector[row] + V_vector[col] - costs[row][col]
                if max_val < value:
                    res_row = row
                    res_col = col
                    max_val = value

        return (res_row, res_col)
