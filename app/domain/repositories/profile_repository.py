from abc import ABC, abstractmethod
from typing import List
import uuid, attr
from app.domain.exception import ProfileNotFound
from app.domain.entity.profile import (Profile, ExtraProfile, BasicProfile)


@attr.s(auto_attribs=True)
class ProfileRepository(ABC):
    _profiles:List[Profile]

    @abstractmethod
    def get_profile(self, 
                    profile_type: str, 
                    profile_id: uuid) -> Profile:
        profile = next((x for x in self._profiles 
                        if x.id == profile_id 
                        and x.profile_type == profile_type
                        ),None)
        return profile
    
    
    @abstractmethod
    def create_profile(self, profile: Profile) -> None:
        self._profiles.append(profile)
    

    @abstractmethod
    def update_profile_basic(self, 
                             profile_type: str, 
                             profile_id: uuid, 
                             basic_profile: BasicProfile) -> None:
        profile = next((x for x in self._profiles 
                        if x.id == profile_id 
                        and x.profile_type == profile_type
                        ), None)
        if profile:
            profile.basic_profile = basic_profile
        else:
            raise ProfileNotFound()
    

    @abstractmethod
    def update_profile_extra(self, 
                             profile_type, 
                             profile_id: uuid, 
                             extra_profiles: List[ExtraProfile]) -> None:
        profile = next((x for x in self._profiles 
                        if x.id == profile_id 
                        and x.profile_type == profile_type
                        ), None)
        if profile:
            profile.extra_profile = extra_profiles
        else:
            raise ProfileNotFound()