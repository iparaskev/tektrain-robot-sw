"""The exceptions of the library."""


class PidevicesError(Exception):
    """Base class for all exceptions in pidevices."""


class NotSupportedInterface(PidevicesError):
    """Error when an invalid interface name is used."""


class NotInstalledInterface(PidevicesError):
    """Error when there isn't any supported library installed for the 
       currrent interface."""


class InvalidHPWMPin(PidevicesError):
    """Error with invalid hardware pwm pin."""


class NotOutputPin(PidevicesError):
    """Error when try to use non output pin for an output function."""


class NotPwmPin(PidevicesError):
    """Error when try to use a non pwm pin for a pwm function."""


class NotInputPin(PidevicesError):
    """Error when try to use non input pin for an input function."""


class InvalidMode(PidevicesError):
    """Error when inserting wrong operation mode for cytron lf."""


class NotConnectedCalPin(PidevicesError):
    """Error when trying to calibrate cytron lf without cal pin connected."""
    

class MoreValuesThanChannels(PidevicesError):
    """Give more values than channels in a servo driver with multiple 
    channels.
    """


class NotModZero(PidevicesError):
    """Not integral multiple."""


class OutOfRange(PidevicesError):
    """Error when a distance sensor returns a measurment out of it's range."""
    pass
