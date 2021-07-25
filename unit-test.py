import time

import prisma.utils.push as push
import prisma.api.cartelist as cartelist
import prisma.utils.worker as worker
import prisma.utils.cartelutils as cutils

cartels = cartelist.getmissionsdict()

cartel = cartels['cartel3']

print(cutils.muchotesto(cartel))

