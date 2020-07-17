sol = []

def btrec(List, n):
    List.append(-1)
    for i in range(0, n):
        List[len(List)-1] = i
        if steady(List):
            if solution(List, n):
                if ok(convert(List)):
                    if convert(List) not in sol:
                        sol.append(convert(List))
                        solutionfound(convert(List))
            else:
                btrec(List[:], n)

def solution(List, n):
    return len(List) == n

def solutionfound(List):
    print(List)

def steady(List):
    for i in range(len(List)-1):
        if List[i] == List[len(List)-1]:
            return False
    return True

def ok(List):
    endpos = List.find(")")
    startpos = List[:endpos].rfind("(")
    if len(List) == 0:
        return True
    if endpos == -1 or startpos == -1:
        return False
    else:
        return ok(List[:startpos] + List[endpos + 1:])

def convert(List):
    d = ""
    for i in range(0, len(List)):
        if List[i] % 2 == 0:
            d += "("
        elif List[i] % 2 == 1:
            d += ")"

    return d

def btite(n):

    while len(List) > 0:
        selected = False
        while not selected and List[len(List) - 1] < n - 1:
            List[len(List) - 1] += 1
            selected = steady(List)
        if selected:
            if solution(List, n):
                if ok(convert(List)):
                    if convert(List) not in sol:
                        sol.append(convert(List))
                        solutionfound(convert(List))
            else:
                List.append(-1)
        else:
            List = List[:-1]

btrec([], 6)
btite(8)



