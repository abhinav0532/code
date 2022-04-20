class Tower:
    def_init_(self)
    self.terminate = 1

    def printMove(self, source, destination):
     print("{} -> {}".format(source, destination))

    def move(self, disc, source, destination, auxillary):
        if(disc == self.terminate):
            self.printMove(source, destination)
        else:
            self.move(disc-1, source, auxillary, destination)
            self.move(1, source, destination, auxillary)
            self.move(disc-1, auxillary, destination, source)


t = Tower();
t.move(3,'A','B','C')
