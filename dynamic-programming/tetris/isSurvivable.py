columns = 10
def isSequenceSurvivable(piecesLeft, boardState):
    if boardState.isGameOver(): # rows exceeded would check if game is over
        return False
    if len(piecesLeft) == 0:
        return True
    
    survivable = True
    for c in range(columns):
        for i, piece in enumerate(piecesLeft):
            for rotation in {0, 1, 2, 3}:
                move = (c, piece, rotation)
                boardState.make_move(move)
                updatedPieces = piecesLeft[i+1:]
                survivable &= isSequenceSurvivable(updatedPieces, boardState)

    return survivable