from operator import itemgetter
from Domains import Bus
from Domains import Route
from Repos import BusRepo
from Repos import RouteRepo
import unittest

class BusController:

    def __init__(self, BusRepo, RouteRepo):
        '''
        initializer for the Bus Controller
        '''
        self.BusRepo = BusRepo
        self.RouteRepo = RouteRepo

    def usageincrease(self, busID, routeID):
        '''
        param busID:
        param routeID:
        return: the usage attribute of the bus is increased by one in case of correct data entered
        '''
        if self.BusRepo.findByIDandRouteID(busID, routeID) != None:
            i = self.BusRepo.findByIDandRouteID(busID, routeID)
            newroutetimes = self.BusRepo.data[i].getroutetimes()
            newroutetimes += 1
            self.BusRepo.data[i].setroutetimes(newroutetimes)
        else:
            raise Exception("Bus ID or route code are invalid!")

    def getAllbusesforaroute(self, routeID):
        '''
        param routeID
        return: a list of all the buses that are using the given route
        '''
        v = []
        for bus in self.BusRepo.getAll():
            if bus.getrouteID() == routeID:
                v.append(bus)

        return v

    def busesdistance(self):
        '''
        return: a list of all the buses sorted by the distance travelled
        '''
        v = []
        for bus in self.BusRepo.getAll():
            for route in self.RouteRepo.getAll():
                if bus.getrouteID() == route.getID():
                    r = bus.getroutetimes()
                    l = route.getlengthkm()
                    dist = r * l
                    n = [dist, bus]
                    v.append(n)
        v.sort(key=itemgetter(0), reverse=True)
        return v

def BusControllerTest():

        RepoBus = BusRepo()
        RepoRoute = RouteRepo()
        bus1 = Bus(1, 1, "Mercedes", 2)
        bus2 = Bus(2, 1, "Audi", 3)
        route1 = Route(1, 23)
        RepoBus.addBus(bus1)
        RepoBus.addBus(bus2)
        RepoRoute.addRoute(route1)
        ctrl = BusController(RepoBus, RepoRoute)

        ctrl.usageincrease(2, 1)

        r = ctrl.getAllbusesforaroute(1)
        assert r[0] == bus1

        v = ctrl.busesdistance()
        assert v[0][0] == 92
        assert v[1][0] == 46

BusControllerTest()
