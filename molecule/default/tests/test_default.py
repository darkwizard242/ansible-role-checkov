import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_checkov_binary_exists(host):
    assert host.file('/usr/local/bin/checkov').exists


def test_checkov_binary_file(host):
    assert host.file('/usr/local/bin/checkov').is_file


def test_checkov_binary_which(host):
    assert host.check_output('which checkov') == '/usr/local/bin/checkov'
