def listToJSON(manyunya):
    buffer = []
    for playersss in manyunya:
        buffer.append(playersss.toJSON())
    return buffer

