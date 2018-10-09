class Heap:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)
        self.__bubble_up(len(self.items)-1)

    def extract_max(self):
        max = self.items[0]
        self.items[0] = self.items[len(self.items)-1]
        self.items = self.items[:-1]
        self.__bubble_down(0)
        return max

    def heap_sort(self):
        sorted_list = []
        for i in range(len(self.items)):
            sorted_list.append(self.extract_max())
        return sorted_list

    def __bubble_up(self, index):
        again = False
        if (len(self.items)>=2):
            if (self.items[index]>self.items[(index-1)//2]):
                again = True
            while (again):
                temp = self.items[(index-1)//2]
                self.items[(index-1)//2] = self.items[index]
                self.items[index]=temp
                index = (index-1)//2

                if (index==0):
                    again = False
                if (self.items[index]<self.items[(index-1)//2]):
                    again = False

    def __bubble_down(self, index):
        again = False
        largest_index =-1
        if (len(self.items)>2):
            if ((self.items[index]<self.items[2*index+1]) or (self.items[index]<self.items[2*index+2])):
                again = True
                largest_index = 2*index+2
                if (self.items[2*index+1]>self.items[2*index+2]):
                    largest_index = 2*index+1

            while (again):
                temp = self.items[largest_index]
                self.items[largest_index] = self.items[index]
                self.items[index]=temp

                index = largest_index
                if (index>=(len(self.items)//2)) or ((2*index+2)>=len(self.items)):
                    again=False
                else:
                    if ((self.items[index]>self.items[2*index+1]) and (self.items[index]>self.items[2*index+2])):
                        again = False
                    else:
                        largest_index = 2*index+2
                        if (self.items[2*index+1]>self.items[2*index+2]):
                            largest_index = 2*index+1

        if (len(self.items)==2):
            if (self.items[0]<self.items[1]):
                temp = self.items[0]
                self.items[0] = self.items[1]
                self.items[1] = temp

    def print_items(self):
        print(self.items)

if __name__=="__main__":
    h = Heap()
    h.print_items()
    for i in range(1, 10):
        h.insert(i)
    h.print_items()
    print(h.heap_sort())

    for i in range(1, 10):
        h.insert(i)
    print("n extracts")
    h.print_items()
    for i in range(1, 10):
        print(h.extract_max())
        h.print_items()
