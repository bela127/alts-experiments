
from alts.modules.oracle.data_source import LineDataSource
from alts.modules.blueprint import BaselineBlueprint
from alts.modules.data_process.process import DataSourceProcess
from alts.modules.query.query_sampler import LatinHypercubeQuerySampler, UniformQuerySampler
from alts.core.experiment_modules import InitQueryExperimentModules
from alts.core.query.query_selector import ResultQuerySelector
from alts.modules.query.query_optimizer import NoQueryOptimizer
from alts.modules.query.query_decider import AllQueryDecider


blueprint = BaselineBlueprint(
    repeat=3,

    process=DataSourceProcess(
        data_source=LineDataSource((1,),(1,))
    ),

    experiment_modules = InitQueryExperimentModules(
    initial_query_sampler = LatinHypercubeQuerySampler(num_queries=10),
    query_selector=ResultQuerySelector(
        query_optimizer=NoQueryOptimizer(query_sampler=LatinHypercubeQuerySampler()),
        query_decider=AllQueryDecider(),
        ),
    ),
)

if __name__ == "__main__":
    from alts.core.experiment_runner import ExperimentRunner
    er = ExperimentRunner([blueprint])
    er.run_experiments()