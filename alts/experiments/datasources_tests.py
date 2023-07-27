
from alts.modules.blueprint import BaselineBlueprint
from alts.core.oracle.data_source import DataSource
from alts.modules.data_process.process import DataSourceProcess
from alts.modules.oracle.data_source import LineDataSource

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
                data_source=ds(query_shape = (1,), result_shape = (1,))
            ),
            exp_name=f"{ds.__name__}", # type: ignore
        )

        blueprints.append(blueprint)
    return blueprints
    

blueprints = create_blueprints()


if __name__ == "__main__":
    from alts.core.experiment_runner import ExperimentRunner
    er = ExperimentRunner(blueprints)
    er.run_experiments()