from spaceone.core.pygrpc.server import GRPCServer
from .cost import Cost
from .job import Job
from .data_source import DataSource

__all__ = ["app"]

app = GRPCServer()
app.add_service(DataSource)
app.add_service(Job)
app.add_service(Cost)
