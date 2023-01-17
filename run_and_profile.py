#from alts.experiments.datasource_test import blueprint
from alts.experiments.gausian_datasource_test import blueprints
from alts.core.experiment_runner import ExperimentRunner

blueprints = blueprints # = [blueprint]

if __name__ == '__main__': 
    er = ExperimentRunner(blueprints)
    er.run_experiments()