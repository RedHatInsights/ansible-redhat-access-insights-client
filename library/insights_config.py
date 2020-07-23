ANSIBLE_METADATA = {
     'metadata_version': '1.1',
     'status': ['preview'],
     'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: insights_config
short_description: This module handles initial configuration of the insights client on install
description:
  - Supply values for various configuration options that you would like to use. On install
  this module will add those values to the insights-client.conf file prior to registering.
version_added: "3.0"
options:
  username:
    description:
    - Insights basic auth username. If defined this will change, set, or remove the username
    in the insights configuration. To remove a username set this value to an empty string.
    required: false
  password:
    description:
    - Insights basic auth password. If defined this will change, set, or remove the password
    in the insights configuration. To remove a password set this value to an empty string.
    required: false
  auto_config:
    description:
    - Attempt to auto-configure the network connection with Satellite or RHSM. Default is True.
    required: false
  authmethod:
    description:
    - Authentication method for the Portal (BASIC, CERT). Default is BASIC. Note: when
    auto_config is enabled, CERT will be used if RHSM or Satellite is detected.
    required: false
  display_name:
    description:
    - Custom display name to appear in the Insights web UI. Only used on machine registration.
    Blank by default.
    required: false
  insights_name:
    description:
    - For now, this is just 'insights-client', but it could change in the future so having
    it as a variable is just preparing for that.
    required: false
  proxy:
    description:
    - This set an optional proxy for the insights client to connect through if the client
    is behind a firewall or requires a proxy. Default is unspecified (none).
    required: false
  obfuscate:
    description:
    - Obfuscate IP addresses.
    Default is unspecified (none).
    required: false
  obfuscate_hostname:
    description:
    - Obfuscate hostname. Requires obfuscate=True.
    Default is unspecified (none).
    required: false
'''

EXAMPLES = '''
- name: Configure the insights client to register with username and password
    insights_config:
      username: "rhn_support" or "{{ redhat_portal_username }}" if passing in as a role variable
      password: "rhn_password" or "{{ redhat_portal_password }}"
      auto_config: False or "{{ auto_config }}"
      authmethod: BASIC or "{{ authmethod }}"
      proxy: "{{ insights_proxy }}"
      obfuscate: "{{ insights_obfuscate }}"
      obfuscate_hostname: "{{ insights_obfuscate_hostname }}"
  become: true

- name: Configure the insights client to register with RHSM and no display name
    insights_config:
  become: true

Note: The above example calls the insights_config module with no parameters. This is because auto_config defaults to True
which in turn forces the client to try RHSM (or Satellite)

- name: Configure the insights client to register with RHSM and a display name
    insights_config:
      display_name: "nice_name" or "{{ insights_display_name }}" if passing in as a role variable
  become: true
'''
