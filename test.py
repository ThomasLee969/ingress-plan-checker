from ingress_plan_checker import *


# p = [Portal(0, 0, 0),
#      Portal(5, 0, 1),
#      Portal(2, 5, 2),
#      Portal(2, 3, 3)]

p=[Portal(116325990,40009746,1),
Portal(116326570,40009195,2),
Portal(116327023,40009154,3),
Portal(116325757,40008720,4),
Portal(116325533,40008616,5),
Portal(116326469,40008519,6),
Portal(116325360,40008455,7),
Portal(116325855,40008396,8),
Portal(116326263,40008393,9),
Portal(116325485,40008239,10),
Portal(116326805,40008224,11),
Portal(116327164,40008151,12),
Portal(116326011,40008131,13),
Portal(116326349,40008129,14),
Portal(116326605,40008102,15),
Portal(116325288,40008082,16),
Portal(116324930,40008077,17),
Portal(116325578,40008034,18),
Portal(116326991,40008006,19),
Portal(116327477,40008008,20),
Portal(116324331,40007854,21),
Portal(116324901,40007761,22)]

c = Context(p)

# p[0].link(c, p[1])
# p[0].link(c, p[3])
# p[3].link(c, p[1])
# p[0].link(c, p[2])
# p[1].link(c, p[2])
# p[2].link(c, p[3])
p[4-1 ].link(c, p[5-1])
p[5-1 ].link(c, p[7-1])
p[4-1 ].link(c, p[7-1])
p[2-1 ].link(c, p[4-1])
p[2-1 ].link(c, p[7-1])
p[1-1 ].link(c, p[2-1])
p[7-1 ].link(c, p[1-1])
p[1-1 ].link(c, p[4-1])
p[1-1 ].link(c, p[5-1])
p[7-1 ].link(c, p[3-1])
p[3-1 ].link(c, p[1-1])
p[3-1 ].link(c, p[2-1])
p[16-1].link(c, p[10-1])
p[10-1].link(c, p[7-1])
p[7-1 ].link(c, p[16-1])
p[16-1].link(c, p[3-1])
p[3-1 ].link(c, p[10-1])
p[8-1 ].link(c, p[16-1])
p[3-1 ].link(c, p[8-1])
p[1-1 ].link(c, p[22-1])
p[3-1 ].link(c, p[22-1])
p[22-1].link(c, p[7-1])
p[22-1].link(c, p[16-1])
p[22-1].link(c, p[8-1])
p[22-1].link(c, p[17-1])
p[21-1].link(c, p[17-1])
p[22-1].link(c, p[21-1])
p[1-1 ].link(c, p[21-1])
p[1-1 ].link(c, p[17-1])
p[20-1].link(c, p[15-1])
p[15-1].link(c, p[18-1])
p[20-1].link(c, p[18-1])
p[20-1].link(c, p[12-1])
p[18-1].link(c, p[12-1])
p[12-1].link(c, p[15-1])
p[9-1 ].link(c, p[13-1])
p[13-1].link(c, p[14-1])
p[14-1].link(c, p[9-1])
p[9-1 ].link(c, p[18-1])
p[18-1].link(c, p[14-1])
p[18-1].link(c, p[13-1])
p[11-1].link(c, p[14-1])
p[9-1 ].link(c, p[11-1])
p[9-1 ].link(c, p[12-1])
p[12-1].link(c, p[14-1])
p[12-1].link(c, p[11-1])
p[20-1].link(c, p[6-1])
p[18-1].link(c, p[6-1])
p[6-1 ].link(c, p[12-1])
p[6-1 ].link(c, p[9-1])
p[18-1].link(c, p[19-1])
p[19-1].link(c, p[20-1])
p[6-1 ].link(c, p[22-1])
p[22-1].link(c, p[20-1])
p[22-1].link(c, p[18-1])
p[22-1].link(c, p[19-1])
p[20-1].link(c, p[3-1])
p[3-1 ].link(c, p[6-1])

