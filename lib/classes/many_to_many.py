class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if type(name) != str:
            print("Exception: Name must be string")
        elif len(name) < 3:
            print("Exception: name length out of range")
        elif hasattr(self, "name"):
            print("Exception: Name cannot be changed after instantiation")
        else:
            self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
        pass
    
    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))
        pass
    
    def total_visits(self):
        return len(self.trips())
        pass
    
    def best_visitor(self):
        visit_log = [trip.visitor for trip in self.trips()]

        curr_best_visitor = None
        curr_most_visits = 0
        for visitor in list(set(visit_log)):
            visitor_visits = visit_log.count(visitor)

            if visitor_visits > curr_most_visits:
                curr_most_visits = visitor_visits
                curr_best_visitor = visitor

        print(set(visit_log))
        return curr_best_visitor
        pass
    
    @classmethod
    def most_visited(cls):
        national_park_list = [trip.national_park for trip in Trip.all]
        print(national_park_list)

        curr_most_visited = None
        curr_most_visits = 0
        for national_park in national_park_list:
            national_park_visits = national_park_list.count(national_park)
            
            if national_park_visits > curr_most_visits:
                curr_most_visits = national_park_visits
                curr_most_visited = national_park

        return curr_most_visited
    
    def __repr__(self):
        return f"{self.name}"


class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property 
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, start_date):
        if type(start_date) != str:
            print("Exception: Name must be a string")
        elif len(start_date) < 7:
            print("Exception: Length myst be greater or equal to 7 characters")
        else:
            self._start_date = start_date
    
    @property 
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, end_date):
        if type(end_date) != str:
            print("Exception: Name must be a string")
        elif len(end_date) < 7:
            print("Exception: Length myst be greater or equal to 7 characters")
        else:
            self._end_date = end_date
    
    @property
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self, visitor):
        if not isinstance(visitor, Visitor):
            print("Exception: visitor must be of Visitor class")
        else:
            self._visitor = visitor
    
    @property 
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self, national_park):
        if not isinstance(national_park, NationalPark):
            print("Exception: national park must be of type NationalPark")
        else:
            self._national_park = national_park

class Visitor:
    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if type(name) != str:
            print("Exception: Name must be string")
        elif len(name) >= 15:
            print("Exception: name too long")
        elif len(name) <= 1:
            print("Exception: name too short")
        else:
            self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
        pass
    
    def national_parks(self):
        return list(set(trip.national_park for trip in self.trips()))
        pass
    
    def total_visits_at_park(self, park):
        return len([trip.visitor for trip in Trip.all if trip.national_park == park])
        pass

    def __repr__(self):
        return f"<Visitor: {self.name}>"