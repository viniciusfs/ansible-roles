import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_firewalld_package(Package):
    firewalld = Package('firewalld')

    assert firewalld.is_installed


def test_firewall_service(Service):
    firewalld = Service('firewalld')

    assert firewalld.is_running
    assert firewalld.is_enabled
