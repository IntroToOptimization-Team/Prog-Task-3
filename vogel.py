from param_wrapper import TranspTaskInfo
class VogelMethod:
    
    def getAvailableIndexes(self, n: int, blocked: list[int]) -> list[int]:
        '''
        Returns the list of indexes in [0, n) that aren't blocked.
        '''
        return [i for i in range(n) if i not in blocked]
            


    def getMaxRow(self, costs, available_rows, available_cols) -> tuple[int, int, int]:
        '''
        Returns the maximum row penalty, the row where this penalty is reached, and the column of the minimum element in that row.
        '''
        max_row_penalty, max_row, min_elem_col = -1, -1, len(costs[0])
        for row in available_rows:
            cur_row = costs[row]

            sorted_ = sorted(cur_row[col] for col in available_cols)
            penalty = 0

            #If not last available element in a row -> take 2 minimum ones
            if len(sorted_) > 1:
                penalty = sorted_[1] - sorted_[0]
            
            if max_row_penalty < penalty:
                max_row_penalty = penalty
                max_row = row
                min_elem_col = cur_row.index(sorted_[0])

        return (max_row_penalty, max_row, min_elem_col)
    


    def getNext(self, parameters: TranspTaskInfo) -> tuple[int, int]:
        '''
        Returns the next cell to consider in a transportaion task according to the vogel's method.
        '''
        costs, _, _, blocked_rows, blocked_cols = parameters.unpack()
        n = len(costs)
        m = len(costs[0])

        available_rows = self.getAvailableIndexes(n, blocked_rows)
        available_cols = self.getAvailableIndexes(m, blocked_cols)

        #I have no any idea how to name these indexes :(
        max_row_penalty, r_row_index, r_col_index = self.getMaxRow(costs, available_rows, available_cols)

        transposed_costs = list(zip(*costs))
        max_col_penalty, c_col_index, c_row_index = self.getMaxRow(transposed_costs, available_cols, available_rows)

        if max_row_penalty > max_col_penalty:
            return (r_row_index, r_col_index)
        else:
            return (c_row_index, c_col_index)

