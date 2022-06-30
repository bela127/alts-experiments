from alts.modules.queried_data_pool import FlatQueriedDataPool
from alts.core.oracle.oracle import Oracle
from alts.core.query.query_optimizer import NoQueryOptimizer
from alts.core.query.selection_criteria import NoSelectionCriteria
from alts.modules.query.query_sampler import LatinHypercubeQuerySampler
from alts.core.oracle.augmentation import NoAugmentation
from alts.modules.stopping_criteria import LearningStepStoppingCriteria
from alts.core.blueprint import Blueprint
from alts.core.oracle.data_source import DataSource
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
    GausianProcessDataSource,
    )
from alts.modules.evaluator import PlotNewDataPointsEvaluator
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
    GausianProcessDataSource,
]

def create_blueprints():
    blueprints = []
    ds: DataSource
    for ds in dss:
        blueprint = Blueprint(
                                repeat=1,
                                stopping_criteria= LearningStepStoppingCriteria(10),
                                oracle = Oracle(
                                    data_source=ds((1,),(1,)),
                                    augmentation= NoAugmentation()
                                ),
                                queried_data_pool=FlatQueriedDataPool(),
                                initial_query_sampler=LatinHypercubeQuerySampler(num_queries=20),
                                query_optimizer=NoQueryOptimizer(
                                    selection_criteria=NoSelectionCriteria(),
                                    num_queries=10,
                                    query_sampler=LatinHypercubeQuerySampler(),
                                ),
                                experiment_modules=ExperimentModules(),
                                evaluators=[PlotNewDataPointsEvaluator(), ],
                                exp_name="-"+ds.__name__
                            )
        blueprints.append(blueprint)
    return blueprints
    

blueprints = create_blueprints()