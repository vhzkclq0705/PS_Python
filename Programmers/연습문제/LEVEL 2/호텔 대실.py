# LEVEL 2

def solution(book_time):
    for i in book_time:
        for j in range(2):
            i[j] = int(i[j][:2]) * 60 + int(i[j][3:])

    book_time.sort(key=lambda x:(x[0], x[1]))
    rooms = []

    for s, e in book_time:
        if not rooms:
            rooms.append(e)
        else:
            for i in range(len(rooms)):
                if s - rooms[i] >= 10:
                    rooms[i] = e
                    break
            else:
                rooms.append(e)   

    return len(rooms)