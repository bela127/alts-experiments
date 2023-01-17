from alts.modules.blueprint import BaselineBlueprint
from alts.modules.oracle.data_source import GaussianProcessDataSource, BrownianProcessDataSource
from alts.modules.data_process.process import DataSourceProcess
from alts.modules.oracle.query_queue import FCFSQueryQueue

GPDS = GaussianProcessDataSource


gp = GPDS()()
b1 = BaselineBlueprint(
    repeat=3,
    process=DataSourceProcess(
        query_queue=FCFSQueryQueue(),
        data_source=gp
    ),
    exp_name="multi_runs",
)

b2 = BaselineBlueprint(
    process=DataSourceProcess(
        query_queue=FCFSQueryQueue(),
        data_source=GPDS()
    ),
    exp_name="one_run",
)

b3 = BaselineBlueprint(
    process=DataSourceProcess(
        query_queue=FCFSQueryQueue(),
        data_source=gp
    ),
    exp_name="repeat_run",
)

blueprints = [b1,b2,b3]

if __name__ == "__main__":
    from alts.core.experiment_runner import ExperimentRunner
    er = ExperimentRunner(xblueprints)
    er.run_experiments()