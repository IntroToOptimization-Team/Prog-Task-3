from param_wrapper import TranspTaskInfo
from formater import Formater
from north_west import NorthWestMethod
from vogel import VogelMethod
from russel import RusselMethod


def isBalanced(supply: list[int], demand: list[int]) -> bool:
    '''
    Checks whether a sum of supply equals a sum of demand(i.e. balanced task).
    '''
    return sum(supply) == sum(demand)



def transportationTask(parameters: TranspTaskInfo,
                       approach: NorthWestMethod | VogelMethod | RusselMethod) -> list[list[int]]:
    '''
    Solves a transportation task for given variables. A caller sets the approach for choosing a next cell.

    Returns a matrix where matrix[i][j] - number of products from i-th source to j-th destination.

    If the task is unsolvable(e.g. not balanced), raises the Exception with an appropriate message.
    '''
    costs, supply, demand, blocked_rows, blocked_cols = parameters.unpack()

    n = len(costs)
    m = len(costs[0]) if n > 0 else 0

    if n == 0 or not all(len(costs[i]) > 0 for i in range(n)) :
        raise Exception(Formater.notApplicable())

    if not isBalanced(supply, demand):
        raise Exception(Formater.notBalanced())

    res_matrix = [[0 for y in range(m)] for i in range(n)]

    while sum(supply) != 0:
        row, col = approach.getNext(TranspTaskInfo(costs, supply, demand, 
                                                   blocked_rows, blocked_cols))

        num_of_product = min(supply[row], demand[col])
        supply[row] -= num_of_product
        demand[col] -= num_of_product

        res_matrix[row][col] += num_of_product

        if supply[row] == 0:
            blocked_rows.append(row)
        if demand[col] == 0:
            blocked_cols.append(col)

    return res_matrix
