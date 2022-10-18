from abc import ABC, abstractmethod


class switchable(ABC):
    
    @abstractmethod
    def turn_on(self):
        '''Turns on the switchable object'''

    @abstractmethod
    def turn_off(self):
        '''Turns off the switchable object'''


class lightbulb(switchable):

    def turn_on(self)  -> None:
        print(f"the {self.__class__.__name__} is turned on")

    def turn_off(self)  -> None:
        print(f"the {self.__class__.__name__} is turned off")


class fairy_lights(switchable):
    def turn_on(self)  -> None:
        print(f"the {self.__class__.__name__} is turned on")

    def turn_off(self)  -> None:
        print(f"the {self.__class__.__name__} is turned off")


class power_switcher:

    def __init__(self, l:switchable) -> None:
        self.l = l
        self.turned_on = False

    def switch(self) -> None:
        if self.turned_on:
            self.l.turn_off()
            self.turned_on = False
        else:
            self.l.turn_on()
            self.turned_on = True



f = fairy_lights()
p = power_switcher(f)
p.switch()
p.switch()


l = lightbulb()
p = power_switcher(l)
p.switch()
p.switch()


# OUTPUT:

# the fairy_lights is turned on
# the fairy_lights is turned off
# the lightbulb is turned on
# the lightbulb is turned off
