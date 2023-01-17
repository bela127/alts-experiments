
from alts.modules.oracle.data_source import LineDataSource, SquareDataSource
from alts.modules.blueprint import BaselineBlueprint
from alts.modules.data_process.process import DataSourceProcess
from alts.modules.oracle.query_queue import FCFSQueryQueue
from alts.modules.stopping_criteria import TimeStoppingCriteria



blueprint = BaselineBlueprint(
    repeat=3,

    process=DataSourceProcess(
        query_queue=FCFSQueryQueue(),
        data_source=LineDataSource((1,),(1,))
    ),

    stopping_criteria = TimeStoppingCriteria(stop_time=12),
    exp_name="datasource_test",
)

if __name__ == "__main__":
    from alts.core.experiment_runner import ExperimentRunner
    er = ExperimentRunner([blueprint])
    er.run_experiments()