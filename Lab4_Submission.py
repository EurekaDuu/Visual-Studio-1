board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board, old: str, new: str, x: int, y: int):
    """
    Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.
    
    if x<0 or x>=len(input_board) or y<0 or y>=len(input_board[0]):
        return input_board
    if input_board[x][y] != old:
        return input_board
    
    listed = list(input_board[x])
    listed[y] = new
    input_board[x] = "".join(listed)

    input_board = flood_fill(input_board,old,new,x-1,y)
    input_board = flood_fill(input_board,old,new,x,y-1)
    input_board = flood_fill(input_board,old,new,x+1,y)
    input_board = flood_fill(input_board,old,new,x,y+1)
    return input_board

modified_board = flood_fill(board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)