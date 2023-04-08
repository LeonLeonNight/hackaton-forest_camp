import attr

@attr.s(auto_attribs=True)
class JournalNotFound(Exception):
    message: str = "Journal Not Found"

@attr.s(auto_attribs=True)
class Registered_drivers_kppNotFound(Exception):
    message: str = "Registered drivers list Not Found"