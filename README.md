[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-checkov.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-checkov) ![Ansible Role](https://img.shields.io/ansible/role/49193?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/49193?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/49193?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-checkov&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-checkov) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-checkov?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-checkov?color=orange&style=flat-square)

# Ansible Role: checkov

Role to install [checkov](https://github.com/bridgecrewio/checkov) pip package on **Debian/Ubuntu** systems for performing static code analysis based on benchmarks and policies for code written in popular IaC's like Terraform, CloudFormation and Kubernetes.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
checkov_debian_pre_reqs:
  - python3
  - python3-pip
checkov_debian_pre_reqs_desired_state: present
pip_executable: pip3
pip_upgrade_version: latest
checkov_app_debian_package: checkov
checkov_desired_state: present
```

### Variables table:

Variable                              | Value (default)      | Description
------------------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------
checkov_debian_pre_reqs               | python3, python3-pip | Packages required to install AWS CLI on Debian based systems. Using python3 as python2.x is EOL by end of 2020.
checkov_debian_pre_reqs_desired_state | present              | Desired state for AWS CLI pre-requisite apps on Debian systems.
pip_executable                        | pip3                 | The executable to utilize for installing **pip** package of `checkov`.
checkov_app_debian_package            | checkov              | Name of checkov application package require to be installed i.e. `checkov` on Debian based systems.
checkov_desired_state                 | present              | Desired state for AWS CLI.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **checkov** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.checkov
```

For customizing behavior of role (i.e. installation of latest **checkov** package instead of ensure it is installed ) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.checkov
  vars:
    checkov_desired_state: latest
```

For customizing behavior of role (i.e. removal of **checkov** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.checkov
  vars:
    checkov_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-checkov/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/), a DevOps/CloudOps Engineer who loves to learn and contribute to Open Source community.
