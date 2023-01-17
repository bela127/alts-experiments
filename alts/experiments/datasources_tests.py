
from alts.modules.query.query_sampler import LatinHypercubeQuerySampler
from alts.modules.blueprint import BaselineBlueprint
from alts.core.oracle.data_source import DataSource
from alts.modules.data_process.process import DataSourceProcess
from alts.modules.oracle.query_queue import FCFSQueryQueue
from alts.modules.oracle.data_source import LineDataSource
from alts.modules.stopping_criteria import TimeStoppingCriteria
from alts.modules.query.query_sampler import LatinHypercubeQuerySampler, UniformQuerySampler
from alts.core.experiment_modules import ExperimentModules
from alts.core.query.query_selector import ResultQuerySelector
from alts.modules.query.query_optimizer import NoQueryOptimizer
from alts.modules.query.query_decider import AllQueryDecider

from alts.modules.oracle.data_source import (
    LineDataSource,
    SquareDataSource,
    CrossDataSource,
    DoubleLinearDataSource,
    HourglassDataSource,
    ZDataSource,
    ZInvDataSource,
    LinearPeriodicDataSource,
    SineDataSource,
    HypercubeDataSource,
    StarDataSource,
    GaussianProcessDataSource,
    )
from alts.core.experiment_modules import ExperimentModules

dss = [
    LineDataSource,
    SquareDataSource,
    CrossDataSource,
    DoubleLinearDataSource,
    HourglassDataSource,
    ZDataSource,
    ZInvDataSource,
    LinearPeriodicDataSource,
    SineDataSource,
    HypercubeDataSource,
    StarDataSource,
    GaussianProcessDataSource,
]

def create_blueprints():
    blueprints = []
    ds: DataSource
    for ds in dss:
        blueprint = BaselineBlueprint(
            repeat=1,

            process=DataSourceProcess(
                query_queue=FCFSQueryQueue(),
                data_source=ds(query_shape = (1,), result_shape = (1,))
            ),

            experiment_modules = ExperimentModules(
                query_selector=ResultQuerySelector(
                    query_optimizer=NoQueryOptimizer(query_sampler=LatinHypercubeQuerySampler()),
                    query_decider=AllQueryDecider(),
                    ),
                ),

            stopping_criteria = TimeStoppingCriteria(stop_time=21),
            initial_query_sampler = LatinHypercubeQuerySampler(num_queries=1),
            exp_name=f"{ds.__name__}", # type: ignore
        )

        blueprints.append(blueprint)
    return blueprints
    

blueprints = create_blueprints()


if __name__ == "__main__":
    from alts.core.experiment_runner import ExperimentRunner
    er = ExperimentRunner(blueprints)
    er.run_experiments()