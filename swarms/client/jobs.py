from .utils.hal import get_link
from . import CrudService


class Jobs(CrudService):
    path = "jobs"

    # copy a job
    def copy(self, job):
        return self.client.post(get_link(job, "copy"))
