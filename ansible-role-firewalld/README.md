# Ansible role: FirewallD

[![Build Status](https://travis-ci.org/viniciusfs/ansible-role-firewalld.svg?branch=master)](https://travis-ci.org/viniciusfs/ansible-role-firewalld)

Installs and configures FirewallD in CentOS/RHEL systems.


## Role Variables

* `firewalld_ports`:
    - Description: List of ports to manage in FirewallD
    - Default: `[]`

* `firewalld_services`:
    - Description: List of services to manage in FirewallD
    - Default: `[]`


## Example Playbook

    - hosts: servers
      roles:
        - role: viniciusfs.firewalld
	  firewalld_services:
	    - service: "https"
	      zone: "public"
	      permanent: True
	      state: "enabled"
	    - service: "ssh"
	      zone: "public"
	      permanent: True
	      state: "enabled"


## License

MIT


## Author Information

* Vinícius Figueiredo <viniciusfs@gmail.com>
