"""Test the dtool_lookup_client_dependency_graph_plugin package."""


def test_version_is_string():
    import dtool_lookup_client_dependency_graph_plugin as plugin
    assert isinstance(plugin.__version__, str)
