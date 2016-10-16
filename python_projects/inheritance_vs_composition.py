
class Abc(object):
    def get_abc(self):
        print 'I am parent from abc'

    def get1_abc(self):
        print 'i am parent from abc1'


class Abc1(Abc):
    def get_abc(self):
        print 'I am abc1'
        super(Abc1, self).get_abc()
        print 'I am abc1'


a = Abc()
b = Abc1()
a.get_abc()
b.get_abc()
b.get1_abc()


class AbcComposition(object):
    def __init__(self):
        self.Abc = Abc()
        self.Abc1 = Abc1()

    def get_abc(self):
        self.Abc.get_abc()
        self.Abc1.get_abc()

c = AbcComposition()
c.get_abc()

