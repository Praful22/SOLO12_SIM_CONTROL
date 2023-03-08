import time

import pybullet as p
import pybullet_data
from scipy.spatial.transform import Rotation

URDF = "./data/urdf/"

class Simulation(object):

    def __init__(self, simulation_type) -> None:

        self._wall = "./data/urdf/wall.urdf"
        self._stairs = "./data/urdf/stair.urdf"
        # self.setup(sim_config=simulation_type)

    def setup(self, sim_config = "height_terrain"):
        py_client = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # p.createCollisionShape(p.GEOM_PLANE)
        # p.createMultiBody(0, 0)
        p.setGravity(0,0,-9.81)
        p.setTimeStep(0.001) 
        if sim_config == "height_terrian":
            rot_stair1 =  Rotation.from_euler('xyz', [0, 0, 180], degrees=True)
            rot_wall = Rotation.from_euler('xyz', [0, 0, 0], degrees=True)
            stair1_pos, stair1_rot = [2, 0, 0], rot_stair1.as_quat()
            wall1_pos, wall1_rot = [2, -1.0, 0.4], rot_wall.as_quat()
            wall2_pos, wall2_rot = [2, 1.0,0.4], rot_wall.as_quat()
            p.loadURDF(self._stairs, basePosition = stair1_pos, baseOrientation = stair1_rot, useFixedBase = 1)
            # p.loadURDF(self._wall, basePosition = wall1_pos, baseOrientation = wall1_rot, useFixedBase = 1)
            p.loadURDF(self._wall, basePosition = wall2_pos, baseOrientation = wall1_rot, useFixedBase = 1)

        elif sim_config == "obstacles_stairs":
            pass


        return py_client


    