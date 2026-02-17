import cifLib.cifFinder as fnd


def test_countTest():
    """Testing the cif counting"""

    expCount = 100
    assert expCount == fnd.getCifCount('cifs4Tests')
