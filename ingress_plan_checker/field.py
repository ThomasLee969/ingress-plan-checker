class Field(object):
    AP = 1250

    """Field"""
    def __init__(self, *apexes):
        super(Field, self).__init__()
        self.apexes = apexes

        self.signed_area = signed_area(apexes)
        self.area = abs(self.signed_area)

    def __repr__(self):
        return "<field (%s, %s, %s)>" % (self.apexes[0].index,
                                         self.apexes[1].index,
                                         self.apexes[2].index)

    def cover(self, portals):
        """Cover portals"""
        for po in portals:
            if (not po.in_field and self.contains(po)):
                po.in_field = True

    def contains(self, portal):
        """Check whether a portal is inside this field"""
        # Using barycentric coordinates.
        # Algorithm from http://stackoverflow.com/questions/2049582/
        #                how-to-determine-a-point-in-a-triangle.
        # Thanks Andreas Brinck & andreasdr.
        apexes = self.apexes

        s = 1 / (2 * self.signed_area) * (
            portal.x * (apexes[2].y - apexes[0].y) +
            apexes[0].x * (portal.y - apexes[2].y) +
            apexes[2].x * (apexes[0].y - portal.y))

        t = 1 / (2 * self.signed_area) * (
            portal.x * (apexes[0].y - apexes[1].y) +
            apexes[0].x * (apexes[1].y - portal.y) +
            apexes[1].x * (portal.y - apexes[0].y))

        return s > 0 and t > 0 and 1 - s - t > 0

def signed_area(apexes):
    area = 0
    for i in range(3):
        area += apexes[i].x * (apexes[i - 2].y - apexes[i - 1].y)
    return area / 2
