import attr

@attr.s(auto_attribs=True)
class ProfileNotFound(Exception):
    message: str = "Profile Not Found"


@attr.s(auto_attribs=True)
class TournamentNotFound(Exception):
    message: str = "Tournament Not Found"


@attr.s(auto_attribs=True)
class TeamNotFound(Exception):
    message: str = "Team Not Found"


@attr.s(auto_attribs=True)
class TeammateNotFound(Exception):
    message: str = "Teammate Not Found"
