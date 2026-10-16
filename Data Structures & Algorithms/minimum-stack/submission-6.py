class MinStack:

    def __init__(self):
        self.__cont = deque(tuple())
        self.__curr_min = 2 ** 31


    def push(self, val: int) -> None:
        if val < self.__curr_min:
            self.__cont.append((val, val))
            self.__curr_min = val
        else:
            self.__cont.append((val, self.__curr_min))


    def pop(self) -> None:
        holder = self.top()
        self.__cont.pop()
        if holder == self.__curr_min:
            self.__curr_min = self.__cont[-1][1] if self.__cont else 2 ** 31

        

    def top(self) -> int:
        return self.__cont[-1][0]

    def getMin(self) -> int:
        return self.__curr_min
