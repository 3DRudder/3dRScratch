# coding=utf-8
from __future__ import unicode_literals

from blockext import *

from  ns3DRudder import *
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

	@predicate("IsDeviceConnected")
	def IsDeviceConnected(self):
		return sdk.IsDeviceConnected(0)
		
	@reporter("DeviceVersion")
	def DeviceVersion(self):
		return sdk.GetVersion(0)

	@reporter("DeviceStatus")
	def DeviceStatus(self):
		return sdk.GetStatus(0)
		
	@reporter("DeviceAxisaX")
	def DeviceAxisaX(self):
		return axis.GetXAxis()
	@reporter("DeviceAxisaY")
	def DeviceAxisaY(self):
		return axis.GetYAxis()
	@reporter("DeviceAxisaZ")
	def DeviceAxisaZ(self):
		return axis.GetZAxis()
	@reporter("DeviceAxisrZ")
	def DeviceAxisrZ(self):
		return axis.GetZRotation()



	
class Th3dRudder(Thread):

	def __init__(self):
		Thread.__init__(self)
		
	def run(self):
		global sdk
		global axis
		global status
		sdk=GetSDK()
		sdk.Init()
		axis = Axis()
		curve = Curve()
		status=NoStatus
		loop = 1
		while(loop):
			#sdk.GetAxis(0,ValueWithCurveNonSymmetricalPitch,axis,curve)
			sdk.GetAxis(0,NormalizedValue,axis)
			status=sdk.GetStatus(0)
			time.sleep(30.0 / 1000.0)



descriptor = Descriptor(
	name = "3dRudder",
	port = 1280,
	blocks = get_decorated_blocks_from_class(Server3dR),
	menus = dict(
		pizza = ["tomato", "cheese", "hawaii"],
	),
)

extension = Extension(Server3dR, descriptor)

if __name__ == "__main__":

	thread_3dRudder=Th3dRudder()
	thread_3dRudder.start()
	extension.run_forever(debug=True)	
