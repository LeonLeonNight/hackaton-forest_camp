import attr

@attr.s(auto_attribs=True)
class JournalNotFound(Exception):
    message: str = "Journal Not Found"