# coding=utf-8
from __future__ import unicode_literals

from blockext import *

from ns3DRudder import *

import sys
from threading import Thread
import time


class Server3dR:
	def __init__(self):
		self.foo = 0

	def _problem(self):
		if not sdk.IsDeviceConnected(0):
			return "3dRudder not connected ..."
			
	def _on_reset(self):
		print("""Reset""")

	@predicate("Is3dRudderConnected")
	def Is3dRudderConnected(self):
		return sdk.IsDeviceConnected(0)

	@reporter("3dRudder_Version")
	def Py3dRudder_Version(self):
		return hex(sdk.GetVersion(0))

	@reporter("3dRudder_Status_Code")
	def Py3dRudder_Status_Code(self):
		return sdk.GetStatus(0)
	
	@reporter("3dRudder_Status")
	def Py3dRudder_Status(self):
		StatusText=['No Status','Do not put your feet on','Initialization','Put Your Feet On','Put Second Foot On','Stay Still','In Use','Extended Mode']
		return StatusText[sdk.GetStatus(0)]

	@reporter("3dRudder_Axis_AX")
	def Py3dRudder_Axis_AX(self):
		return axis.GetXAxis()

	@reporter("3dRudder_Axis_AY")
	def Py3dRudder_Axis_AY(self):
		return axis.GetYAxis()

	@reporter("3dRudder_Axis_AZ")
	def Py3dRudder_Axis_AZ(self):
		return axis.GetZAxis()

	@reporter("3dRudder_Axis_RZ")
	def Py3dRudder_Axis_RZ(self):
		return axis.GetZRotation()

	@command("3dRudder_PlaySnd( %s,%b )", defaults=["",False])
	def Py3dRudder_PlaySnd(self,s,b):
		err=sdk.PlaySndEx(0,str(s),b)
		print (err)

class Th3dRudder_(Thread):

	def __init__(self):
		Thread.__init__(self)

	def run(self):
		global sdk
		global axis
		global status
		
		sdk=GetSDK()
		sdk.Init()
		axis = Axis()
		curve = CurveArray()
		status=NoStatus
		loop = 1
		while(loop):
			sdk.GetAxis(0,ValueWithCurveNonSymmetricalPitch,axis,curve)
			status=sdk.GetStatus(0)
			time.sleep(30.0 / 1000.0)



descriptor = Descriptor(
	name = "3dRudder",
	port = 1280,
	blocks = get_decorated_blocks_from_class(Server3dR),
	menus = dict(
	)
)

extension = Extension(Server3dR, descriptor)

if __name__ == "__main__":

	threadPy3dRudder_=Th3dRudder_()
	threadPy3dRudder_.start()
	extension.run_forever(debug=True)
