import unittest
from chalice.cli import click, cli


def load_tests(loader, test_cases, pattern):
    suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


@cli.command()
@click.option('--app',
              help='The application directory.  Defaults to all')
@click.option('--verbose', '-v', count=True, help='Print verbosely')
@click.pass_context
def test(ctx, app, verbose):
    manager = ctx.obj['manager']

    all_tests = []
    for mod in manager.app_modules:
        all_tests += mod.test_cases
    if len(all_tests) == 0:
        print 'No tests'; return
    loader = unittest.TestLoader()
    suite = load_tests(loader, all_tests, None)

    kwargs = {}
    if verbose:
        kwargs.update({'verbosity': 2})
    unittest.TextTestRunner(**kwargs).run(suite)
