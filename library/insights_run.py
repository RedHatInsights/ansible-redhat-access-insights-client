#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: insights_run

short_description: This module runs the insights client

description:
    - This module will run the insights client

options:
    insights_name:
        description:
            - For now, this is just 'insights-client', but it could change in the future
            so having it as a variable is just preparing for that
        required: false

author:
    - Ivan Aragonés (based on insights_register by Jason Stephens (@Jason-RH) )
'''

EXAMPLES = '''
# Normal Run
- name: Run insights client
  insights_run:

# Run with alternative insights binary name
- name: Run insights client
  insights_run:
    insights_name: 'redhat-access-insights'

Note: The above example for registering redhat-access-insights requires that the playbook be
changed to install redhat-access-insights and that redhat-access-insights is also passed into
the insights_config module and that the file paths be changed when using the file module
'''

RETURN = '''
original_message:
    description: The Insights agent is able to be executed
    type: str
message:
    description: The Insights agent has been executed
'''

from ansible.module_utils.basic import AnsibleModule
import subprocess

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        #state=dict(choices=['present', 'absent'], default='present'),
        insights_name=dict(type='str', required=False, default='insights-client')
        #display_name=dict(type='str', required=False, default=''),
        #force_reregister=dict(type='bool', required=False, default=False)
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    insights_name = module.params['insights_name']

    if module.check_mode:
        return result

    try:
        reg_out = subprocess.call([insights_name])
    except:
        # result['changed'] = False
        # result['Failed'] = True
        result['msg'] = result['message'] = "The Insights agent could'nt be executed. Is the insights-client installed?"
        module.fail_json(**result)

    if reg_out is 0:
        result['changed'] = True
        result['message'] = 'The Insights agent has been executed. Data has been uploaded'
        module.exit_json(**result)
    else:
        result['changed'] = False
        result['message'] = 'The Insights agent has not been executed'
        module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
