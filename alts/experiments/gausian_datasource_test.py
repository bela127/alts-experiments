from alts.modules.queried_data_pool import FlatQueriedDataPool
from alts.modules.data_sampler import KDTreeKNNDataSampler, KDTreeRegionDataSampler
from alts.core.oracle.oracle import Oracle
from alts.core.query.query_optimizer import NoQueryOptimizer
from alts.core.query.selection_criteria import NoSelectionCriteria
from alts.modules.query.query_sampler import LastQuerySampler, RandomChoiceQuerySampler, UniformQuerySampler, LatinHypercubeQuerySampler
from alts.core.oracle.augmentation import NoAugmentation
from alts.modules.stopping_criteria import LearningStepStoppingCriteria
from alts.core.blueprint import Blueprint
from alts.modules.oracle.data_source import GausianProcessDataSource
from alts.modules.evaluator import LogNewDataPointsEvaluator, PlotNewDataPointsEvaluator, PrintNewDataPointsEvaluator, PlotQueryDistEvaluator
from alts.core.experiment_modules import ExperimentModules

gp = GausianProcessDataSource((1,),(1,))()
b1 = Blueprint(
    repeat=3,
    stopping_criteria= LearningStepStoppingCriteria(5),
    oracle = Oracle(
        data_source=gp,
        augmentation= NoAugmentation()
    ),
    queried_data_pool=FlatQueriedDataPool(),
    initial_query_sampler=LatinHypercubeQuerySampler(num_queries=30),
    query_optimizer=NoQueryOptimizer(
        selection_criteria=NoSelectionCriteria(),
        num_queries=10,
        query_sampler=UniformQuerySampler(),
    ),
    experiment_modules=ExperimentModules(),
    evaluators=[PlotNewDataPointsEvaluator(), ],
    exp_name="-multi_runs"
)

b2 = Blueprint(
    repeat=1,
    stopping_criteria= LearningStepStoppingCriteria(5),
    oracle = Oracle(
        data_source=GausianProcessDataSource((1,),(1,)),
        augmentation= NoAugmentation()
    ),
    queried_data_pool=FlatQueriedDataPool(),
    initial_query_sampler=LatinHypercubeQuerySampler(num_queries=30),
    query_optimizer=NoQueryOptimizer(
        selection_criteria=NoSelectionCriteria(),
        num_queries=10,
        query_sampler=UniformQuerySampler(),
    ),
    experiment_modules=ExperimentModules(),
    evaluators=[PlotNewDataPointsEvaluator(), ],
    exp_name="-one_run"
)

b3 = Blueprint(
    repeat=1,
    stopping_criteria= LearningStepStoppingCriteria(5),
    oracle = Oracle(
        data_source=gp,
        augmentation= NoAugmentation()
    ),
    queried_data_pool=FlatQueriedDataPool(),
    initial_query_sampler=LatinHypercubeQuerySampler(num_queries=30),
    query_optimizer=NoQueryOptimizer(
        selection_criteria=NoSelectionCriteria(),
        num_queries=10,
        query_sampler=UniformQuerySampler(),
    ),
    experiment_modules=ExperimentModules(),
    evaluators=[PlotNewDataPointsEvaluator(), ],
    exp_name="-repeat_run"
)

blueprints = [b1,b2,b3]
