class State:

    def __init__(self, machine):
        self.machine = machine

    def insert_quarter(self):
        pass

    def eject_quarter(self):
        pass

    def turn_crank(self):
        pass

    def dispense(self):
        pass


class SoldOutState(State):

    def insert_quarter(self):
        print('껌 매진입니다~~')


class NoQuarterState(State):

    def insert_quarter(self):
        print('동전이 들어갔습니다.')
        self.machine.state = self.machine.HAS_QUARTER


class HasQuarterState(State):

    def eject_quarter(self):
        print('동전 환불')
        self.machine.state = self.machine.NO_QUARTER

    def turn_crank(self):
        print('레버를 돌리셨습니다.')
        self.machine.state = self.machine.SOLD


class SoldState(State):

    def dispense(self):
        self.machine.release_ball()
        if self.machine.count > 0:
            self.machine.state = self.machine.NO_QUARTER
            return
        print('껌 소진')
        self.machine.state = self.machine.SOLD_OUT


class GumballMachine:

    def __init__(self, count):
        self.SOLD_OUT = SoldOutState(self)
        self.NO_QUARTER = NoQuarterState(self)
        self.HAS_QUARTER = HasQuarterState(self)
        self.SOLD = SoldState(self)
        self.state = self.SOLD_OUT
        self.count = count
        if count > 0:
            self.state = self.NO_QUARTER

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def release_ball(self):
        print('또르륵 (껌 굴러가는 소리)')
        if self.count > 0:
            self.count -= 1

machine = GumballMachine(5)
machine.insert_quarter()
machine.turn_crank()
machine.turn_crank()