insights-client
========

Installs, configures, and registers a system to the [Red Hat Insights service](http://access.redhat.com/insights).  This role is intended to work on Red Hat Enterprise Linux, though it will generally work on any yum based system that has access to the insights-client RPM or the redhat-access-insights RPM.

Requirements
------------

N/A

Role Variables
--------------

The following variables can be passed in directly with the playbook invocation or placed in a configuration yaml file.
See the section 'Example Playbook' for information on various ways to use these variables. 

* insights_display_name: (optional)

    Sets or resets the Display Name/System Name within Insights.  Insights needs an easily identifiable
    name for each system.  If no explicit display name is given to a system, Insights uses it's hostname.
    If a system's hostname is not easily identifiable, like "localhost" or "d4098731408", you can give
    it a better name by setting 'insights_display_name'

    If undefined (not set at all), this role will not make changes to a system's display name.

    If defined (set) to be the empty string, this role will remove any previously set display name
    for the system, and cause it to use the systems hostname as it's Display name/System name.

    If defined to be a non-empty string, this role will replace any previously set display name
    for the system with the given string.

* redhat_portal_username: (optional)
* redhat_portal_password: (optional)
    If defined, these set, change, or remove the username and password in the Insights configuration.
    If undefined, this role will make no changes to the Insights configuration.

    If defined to a non-empty string this role will set or change the username and password.
    If defined to an empty string this role will remove the username and password.

    These should be valid username/password for Insights/Red Hat Portal/Red Hat Subscription Manager.

    If the username and password are set in the Insights configuration, they will be used as
    credentials for all future interactions with the Insights server.

    These credentials are only necessary if the client system is not registered with Red Hat
    Subscription Manager.  If the username and password are not set in the Insights configuration,
    which is the default initial state, all interactions with the Insights server will use the
    CERT provided by RHSM.

* auto_config: (optional)
    True/False - attempt to auto-configure the network connection with Satellite or RHSM. Default behavior is True.

* authmethod: (optional)
    BASIC/CERT - This parameter is used to set the authentication method for the Portal. Default bahavior is BASIC.
    Note: when 'auto_config' is enabled (set to True), CERT will be used if RHSM or Satellite is detected.

Facts Installed
---------------

This role installs a new fact 'insights' that provides the system's Insights' System Id.  This System
Id can be used to query about the system with the Insights Service API.

Once this role is run against a system, any future playbook run against that same system will have
the system's Insights System Id in the fact 'ansible_local.insights.system_id'.

For example the task:

    - debug: var=ansible_local.insights.system_id

will display the System Id.



Dependencies
------------

N/A

Example Playbook
----------------

    - hosts: all
      roles:
      - { role: redhatinsights.insights-client, when: ansible_os_family == 'RedHat' }

If a system's hostname is not easily identifiable, but inventory_hostname is easily identifiable,
as often happens on some cloud platforms, set insights_display_name set to be inventory_hostname:

    - hosts: all
      roles:
      - role: redhatinsights.insights-client
        insights_display_name: "{{ inventory_hostname }}"
        when: ansible_os_family == 'RedHat'

If you need to run the Insights Client on a system that is not registered to Red Hat Subscription
Manager, as often happens in testing and demoing, set the
redhat_portal_username/redhat_portal_password in a way that keeps them out of the playbook:

Create a YAML file, say insights-client-config.yml, on your workstation containing the following,
with XXXXXX/YYYYYY replaced with our Insights/Portal/RHSM username/password:

    redhat_portal_username: XXXXXX
    redhat_portal_password: YYYYYY

Note: Any of the role variables mentioned earlier can be placed in this configuration file

Change the permissions on the file so that only you can read them, and then any time you invoke
this role, add the ansible-playbook --extra-vars option:

    $ ansible-playbook ... --extra-vars @insights-client-config.yml ...

Note that one of the really useful features of Ansible Tower is role based management of credentials
like this.


Example Use
-----------

1. On a system where [Ansible is installed](http://docs.ansible.com/ansible/intro_installation.html), run the following command:

    ```bash
    $ ansible-galaxy install redhatinsights.insights-client
    ```

1. Copy the Example Playbook to a file named 'install-insights.yml'.

1. Run the following command, replacing 'myhost.example.com' with the name of the
   system where you want to install, configure, and register the insights client.

    ```bash
    $ ansible-playbook --limit=myhost.example.com install-insights.yml
    ```

License and Author
------------------

License: Apache License 2.0
Author: Red Hat, Inc.
