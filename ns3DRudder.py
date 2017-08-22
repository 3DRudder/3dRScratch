# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_ns3DRudder')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_ns3DRudder')
    _ns3DRudder = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ns3DRudder', [dirname(__file__)])
        except ImportError:
            import _ns3DRudder
            return _ns3DRudder
        if fp is not None:
            try:
                _mod = imp.load_module('_ns3DRudder', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ns3DRudder = swig_import_helper()
    del swig_import_helper
else:
    import _ns3DRudder
del _swig_python_version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


_3DRUDDER_SDK_MAX_DEVICE = _ns3DRudder._3DRUDDER_SDK_MAX_DEVICE
_3DRUDDER_SDK_VERSION = _ns3DRudder._3DRUDDER_SDK_VERSION
Success = _ns3DRudder.Success
NotConnected = _ns3DRudder.NotConnected
Fail = _ns3DRudder.Fail
IncorrectCommand = _ns3DRudder.IncorrectCommand
Timeout = _ns3DRudder.Timeout
WrongSignature = _ns3DRudder.WrongSignature
NotReady = _ns3DRudder.NotReady
Other = _ns3DRudder.Other
CurveXAxis = _ns3DRudder.CurveXAxis
CurveYAxis = _ns3DRudder.CurveYAxis
CurveZAxis = _ns3DRudder.CurveZAxis
CurveZRotation = _ns3DRudder.CurveZRotation
CurveYaw = _ns3DRudder.CurveYaw
CurvePitch = _ns3DRudder.CurvePitch
CurveRoll = _ns3DRudder.CurveRoll
CurveUpDown = _ns3DRudder.CurveUpDown
CurveMax = _ns3DRudder.CurveMax
NoStatus = _ns3DRudder.NoStatus
NoFootStayStill = _ns3DRudder.NoFootStayStill
Initialisation = _ns3DRudder.Initialisation
PutYourFeet = _ns3DRudder.PutYourFeet
PutSecondFoot = _ns3DRudder.PutSecondFoot
StayStill = _ns3DRudder.StayStill
InUse = _ns3DRudder.InUse
ExtendedMode = _ns3DRudder.ExtendedMode
End = _ns3DRudder.End
UserRefAngle = _ns3DRudder.UserRefAngle
NormalizedValue = _ns3DRudder.NormalizedValue
ValueWithCurve = _ns3DRudder.ValueWithCurve
NormalizedValueNonSymmetricalPitch = _ns3DRudder.NormalizedValueNonSymmetricalPitch
ValueWithCurveNonSymmetricalPitch = _ns3DRudder.ValueWithCurveNonSymmetricalPitch
class Tone(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Tone, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Tone, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _ns3DRudder.new_Tone(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_setmethods__["m_nFrequency"] = _ns3DRudder.Tone_m_nFrequency_set
    __swig_getmethods__["m_nFrequency"] = _ns3DRudder.Tone_m_nFrequency_get
    if _newclass:
        m_nFrequency = _swig_property(_ns3DRudder.Tone_m_nFrequency_get, _ns3DRudder.Tone_m_nFrequency_set)
    __swig_setmethods__["m_nDurationOfTone"] = _ns3DRudder.Tone_m_nDurationOfTone_set
    __swig_getmethods__["m_nDurationOfTone"] = _ns3DRudder.Tone_m_nDurationOfTone_get
    if _newclass:
        m_nDurationOfTone = _swig_property(_ns3DRudder.Tone_m_nDurationOfTone_get, _ns3DRudder.Tone_m_nDurationOfTone_set)
    __swig_setmethods__["m_nPauseAfterTone"] = _ns3DRudder.Tone_m_nPauseAfterTone_set
    __swig_getmethods__["m_nPauseAfterTone"] = _ns3DRudder.Tone_m_nPauseAfterTone_get
    if _newclass:
        m_nPauseAfterTone = _swig_property(_ns3DRudder.Tone_m_nPauseAfterTone_get, _ns3DRudder.Tone_m_nPauseAfterTone_set)
    __swig_destroy__ = _ns3DRudder.delete_Tone
    __del__ = lambda self: None
Tone_swigregister = _ns3DRudder.Tone_swigregister
Tone_swigregister(Tone)

class Curve(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Curve, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Curve, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        if self.__class__ == Curve:
            _self = None
        else:
            _self = self
        this = _ns3DRudder.new_Curve(_self, *args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ns3DRudder.delete_Curve
    __del__ = lambda self: None

    def GetDeadZone(self):
        return _ns3DRudder.Curve_GetDeadZone(self)

    def GetXSat(self):
        return _ns3DRudder.Curve_GetXSat(self)

    def GetYMax(self):
        return _ns3DRudder.Curve_GetYMax(self)

    def GetExp(self):
        return _ns3DRudder.Curve_GetExp(self)

    def SetDeadZone(self, fV):
        return _ns3DRudder.Curve_SetDeadZone(self, fV)

    def SetXSat(self, fV):
        return _ns3DRudder.Curve_SetXSat(self, fV)

    def SetYMax(self, fV):
        return _ns3DRudder.Curve_SetYMax(self, fV)

    def SetExp(self, fV):
        return _ns3DRudder.Curve_SetExp(self, fV)

    def CalcCurveValue(self, fValue):
        return _ns3DRudder.Curve_CalcCurveValue(self, fValue)
    __swig_setmethods__["m_fDeadZone"] = _ns3DRudder.Curve_m_fDeadZone_set
    __swig_getmethods__["m_fDeadZone"] = _ns3DRudder.Curve_m_fDeadZone_get
    if _newclass:
        m_fDeadZone = _swig_property(_ns3DRudder.Curve_m_fDeadZone_get, _ns3DRudder.Curve_m_fDeadZone_set)
    __swig_setmethods__["m_fxSat"] = _ns3DRudder.Curve_m_fxSat_set
    __swig_getmethods__["m_fxSat"] = _ns3DRudder.Curve_m_fxSat_get
    if _newclass:
        m_fxSat = _swig_property(_ns3DRudder.Curve_m_fxSat_get, _ns3DRudder.Curve_m_fxSat_set)
    __swig_setmethods__["m_fyMax"] = _ns3DRudder.Curve_m_fyMax_set
    __swig_getmethods__["m_fyMax"] = _ns3DRudder.Curve_m_fyMax_get
    if _newclass:
        m_fyMax = _swig_property(_ns3DRudder.Curve_m_fyMax_get, _ns3DRudder.Curve_m_fyMax_set)
    __swig_setmethods__["m_fExp"] = _ns3DRudder.Curve_m_fExp_set
    __swig_getmethods__["m_fExp"] = _ns3DRudder.Curve_m_fExp_get
    if _newclass:
        m_fExp = _swig_property(_ns3DRudder.Curve_m_fExp_get, _ns3DRudder.Curve_m_fExp_set)
    def __disown__(self):
        self.this.disown()
        _ns3DRudder.disown_Curve(self)
        return weakref_proxy(self)
Curve_swigregister = _ns3DRudder.Curve_swigregister
Curve_swigregister(Curve)

class CurveArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CurveArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CurveArray, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _ns3DRudder.new_CurveArray()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def InitLinear(self):
        return _ns3DRudder.CurveArray_InitLinear(self)

    def InitFactory(self):
        return _ns3DRudder.CurveArray_InitFactory(self)

    def GetCurve(self, nCurve):
        return _ns3DRudder.CurveArray_GetCurve(self, nCurve)

    def SetCurve(self, nCurve, pCurve):
        return _ns3DRudder.CurveArray_SetCurve(self, nCurve, pCurve)
    __swig_destroy__ = _ns3DRudder.delete_CurveArray
    __del__ = lambda self: None
CurveArray_swigregister = _ns3DRudder.CurveArray_swigregister
CurveArray_swigregister(CurveArray)

class Axis(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Axis, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Axis, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _ns3DRudder.new_Axis()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_setmethods__["m_aX"] = _ns3DRudder.Axis_m_aX_set
    __swig_getmethods__["m_aX"] = _ns3DRudder.Axis_m_aX_get
    if _newclass:
        m_aX = _swig_property(_ns3DRudder.Axis_m_aX_get, _ns3DRudder.Axis_m_aX_set)
    __swig_setmethods__["m_aY"] = _ns3DRudder.Axis_m_aY_set
    __swig_getmethods__["m_aY"] = _ns3DRudder.Axis_m_aY_get
    if _newclass:
        m_aY = _swig_property(_ns3DRudder.Axis_m_aY_get, _ns3DRudder.Axis_m_aY_set)
    __swig_setmethods__["m_aZ"] = _ns3DRudder.Axis_m_aZ_set
    __swig_getmethods__["m_aZ"] = _ns3DRudder.Axis_m_aZ_get
    if _newclass:
        m_aZ = _swig_property(_ns3DRudder.Axis_m_aZ_get, _ns3DRudder.Axis_m_aZ_set)
    __swig_setmethods__["m_rZ"] = _ns3DRudder.Axis_m_rZ_set
    __swig_getmethods__["m_rZ"] = _ns3DRudder.Axis_m_rZ_get
    if _newclass:
        m_rZ = _swig_property(_ns3DRudder.Axis_m_rZ_get, _ns3DRudder.Axis_m_rZ_set)

    def GetXAxis(self):
        return _ns3DRudder.Axis_GetXAxis(self)

    def GetYAxis(self):
        return _ns3DRudder.Axis_GetYAxis(self)

    def GetZAxis(self):
        return _ns3DRudder.Axis_GetZAxis(self)

    def GetZRotation(self):
        return _ns3DRudder.Axis_GetZRotation(self)

    def GetPhysicalRoll(self):
        return _ns3DRudder.Axis_GetPhysicalRoll(self)

    def GetPhysicalPitch(self):
        return _ns3DRudder.Axis_GetPhysicalPitch(self)

    def GetUpDown(self):
        return _ns3DRudder.Axis_GetUpDown(self)

    def GetPhysicalYaw(self):
        return _ns3DRudder.Axis_GetPhysicalYaw(self)
    __swig_destroy__ = _ns3DRudder.delete_Axis
    __del__ = lambda self: None
Axis_swigregister = _ns3DRudder.Axis_swigregister
Axis_swigregister(Axis)

class IEvent(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IEvent, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IEvent, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _ns3DRudder.delete_IEvent
    __del__ = lambda self: None

    def OnConnect(self, nDeviceNumber):
        return _ns3DRudder.IEvent_OnConnect(self, nDeviceNumber)

    def OnDisconnect(self, nDeviceNumber):
        return _ns3DRudder.IEvent_OnDisconnect(self, nDeviceNumber)

    def __init__(self):
        if self.__class__ == IEvent:
            _self = None
        else:
            _self = self
        this = _ns3DRudder.new_IEvent(_self, )
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    def __disown__(self):
        self.this.disown()
        _ns3DRudder.disown_IEvent(self)
        return weakref_proxy(self)
IEvent_swigregister = _ns3DRudder.IEvent_swigregister
IEvent_swigregister(IEvent)

class CSdk(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CSdk, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CSdk, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _ns3DRudder.new_CSdk()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ns3DRudder.delete_CSdk
    __del__ = lambda self: None

    def Init(self):
        return _ns3DRudder.CSdk_Init(self)

    def GetSDKVersion(self):
        return _ns3DRudder.CSdk_GetSDKVersion(self)

    def GetNumberOfConnectedDevice(self):
        return _ns3DRudder.CSdk_GetNumberOfConnectedDevice(self)

    def IsDeviceConnected(self, nPortNumber):
        return _ns3DRudder.CSdk_IsDeviceConnected(self, nPortNumber)

    def GetVersion(self, nPortNumber, bUseCmd=False):
        return _ns3DRudder.CSdk_GetVersion(self, nPortNumber, bUseCmd)

    def HideSystemDevice(self, nPortNumber, bHide):
        return _ns3DRudder.CSdk_HideSystemDevice(self, nPortNumber, bHide)

    def IsSystemDeviceHidden(self, nPortNumber):
        return _ns3DRudder.CSdk_IsSystemDeviceHidden(self, nPortNumber)

    def PlaySnd(self, nPortNumber, nFrequency, nDuration):
        return _ns3DRudder.CSdk_PlaySnd(self, nPortNumber, nFrequency, nDuration)

    def PlaySndEx(self, *args):
        return _ns3DRudder.CSdk_PlaySndEx(self, *args)

    def GetUserOffset(self, nPortNumber, pAxis):
        return _ns3DRudder.CSdk_GetUserOffset(self, nPortNumber, pAxis)

    def GetAxis(self, nPortNumber, nMode, pAxis, pCurve=None):
        return _ns3DRudder.CSdk_GetAxis(self, nPortNumber, nMode, pAxis, pCurve)

    def GetStatus(self, nPortNumber):
        return _ns3DRudder.CSdk_GetStatus(self, nPortNumber)

    def GetSensor(self, nPortNumber, nIndex):
        return _ns3DRudder.CSdk_GetSensor(self, nPortNumber, nIndex)

    def SetFreeze(self, nPortNumber, bEnable):
        return _ns3DRudder.CSdk_SetFreeze(self, nPortNumber, bEnable)

    def GetErrorText(self, nError):
        return _ns3DRudder.CSdk_GetErrorText(self, nError)

    def SetEvent(self, pEvent):
        return _ns3DRudder.CSdk_SetEvent(self, pEvent)

    def CalcCurveValue(self, fDeadZone, fxSat, fyMax, fExp, fValue):
        return _ns3DRudder.CSdk_CalcCurveValue(self, fDeadZone, fxSat, fyMax, fExp, fValue)
CSdk_swigregister = _ns3DRudder.CSdk_swigregister
CSdk_swigregister(CSdk)


def GetSDK():
    return _ns3DRudder.GetSDK()
GetSDK = _ns3DRudder.GetSDK

def EndSDK():
    return _ns3DRudder.EndSDK()
EndSDK = _ns3DRudder.EndSDK
# This file is compatible with both classic and new-style classes.


