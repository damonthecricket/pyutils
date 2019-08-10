
import unittest

from . import test_array
from . import test_csv
from . import test_file
from . import test_folder


loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests( loader.loadTestsFromModule(test_array)  )
suite.addTests( loader.loadTestsFromModule(test_csv)    )
suite.addTests( loader.loadTestsFromModule(test_file) 	)
suite.addTests( loader.loadTestsFromModule(test_folder) )

runner = unittest.TextTestRunner(verbosity = 4)
result = runner.run(suite)