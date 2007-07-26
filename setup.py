import setuptools
from numpy.distutils.core import setup


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.set_options(
        ignore_setup_xxx_py=True,
        assume_default_configuration=True,
        delegate_options_to_subpackages=True,
        quiet=True,
    )

    config.add_subpackage('enthought.interpolate')
    config.add_data_files('enthought/__init__.py')

    return config


# Function to convert simple ETS component names and versions to a requirements
# spec that works for both development builds and stable builds.  This relies
# on the Enthought's standard versioning scheme -- see the following write up:
#    https://svn.enthought.com/enthought/wiki/EnthoughtVersionNumbers
def etsdeps(list):
    return ['%s >=%s.dev, <%s.a' % (p,ver,int(ver[:1])+1) for p,ver in list]


# Declare our installation requirements.
install_requires = etsdeps([
    ('enthought.traits', '2.0b1'),
    ])
print 'install_requires:\n\t%s' % '\n\t'.join(install_requires)
test_requires = [
    "nose >= 0.9, ",
    ] + etsdeps([
    ])
print 'test_requires:\n\t%s' % '\n\t'.join(test_requires)


setup(
    author = 'Enthought, Inc',
    author_email = 'info@enthought.com',
    description = "Array interpolation/extrapolation",
    extras_require = {
        # All non-ets dependencies should be in this extra to ensure users can
        # decide whether to require them or not.
        'nonets': [
            "scipy >=0.5.2",
	    "numpy >=1.0.3",
            ],
        },
    install_requires = install_requires,
    license = "BSD",
    name = 'enthought.interpolate',
    namespace_packages = [
        "enthought",
        ],
    tests_require = test_requires,
    test_suite = 'nose.collector',
    url = 'http://code.enthought.com/ets',
    version = '2.0b2',
    **configuration().todict()
)
