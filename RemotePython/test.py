import time
import numpy
from zmqRemoteApi import RemoteAPIClient

resultData = list

client = RemoteAPIClient()
sim = client.getObject('sim')
client.setStepping(True)
bill = sim.getObject('./Bill')
robot = sim.getObject('./Omnirob')

sim.startSimulation()
while (t := sim.getSimulationTime()) < 30:
    s = f'Simulation time: {t:.2f} [s]'
    pos1 = sim.getObjectPosition(bill,0)
    pos2 = sim.getObjectPosition(robot,0)
    dist = numpy.linalg.norm(numpy.subtract(pos1,pos2))
    resultData.append([t,dist])
    client.step()
sim.stopSimulation()


