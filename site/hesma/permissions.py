from invenio_rdm_records.services.permissions import RDMRecordPermissionPolicy
from invenio_communities.permissions import CommunityPermissionPolicy
from invenio_records_permissions.generators import Generator, AnyUser, SystemProcess
from flask_principal import RoleNeed


class RoleNeeded(Generator):
    def __init__(self, role_name):
        self.role_name = role_name

    def needs(self, **kwargs):
        return [RoleNeed(self.role_name)]


class InstancePermissionPolicy(RDMRecordPermissionPolicy):
    can_create = [SystemProcess(), RoleNeeded("readwrite"), RoleNeeded("admin")]
    can_read = [SystemProcess(), AnyUser()]
    can_read_files = [SystemProcess(), AnyUser()]
    can_search = [SystemProcess(), AnyUser()]
    can_search_versions = [SystemProcess(), AnyUser()]


class InstanceCommunityPermissionPolicy(CommunityPermissionPolicy):
    can_create = [SystemProcess(), RoleNeeded("admin")]
    can_read = [SystemProcess(), AnyUser()]
    can_search = [SystemProcess(), AnyUser()]
    can_featured_search = [SystemProcess(), AnyUser()]
    can_members_search_public = [SystemProcess(), AnyUser()]
