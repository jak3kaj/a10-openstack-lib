# Copyright 2015,  A10 Networks
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from neutron_lib.api import converters

import validators

EXTENSION = 'a10-device'

SERVICE = "A10_DEVICE"

VTHUNDERS = 'a10_vthunders'
VTHUNDER = 'a10_vthunder'

DEVICES = 'a10_devices'
DEVICE = 'a10_device'

DEVICE_KEYS = 'a10_device_keys'
DEVICE_KEY = 'a10_device_key'

DEVICE_VALUES = 'a10_device_values'
DEVICE_VALUE = 'a10_device_value'

RESOURCE_ATTRIBUTE_MAP = {
    VTHUNDERS: {
        'id': {
            'allow_post': False,
            'allow_put': True,
            'validate': {
                'type:uuid': None
            },
            'is_a10_opt': False,
            'is_visible': True,
            'primary_key': True
        },
        'tenant_id': {
            'allow_post': True,
            'allow_put': False,
            'required_by_policy': True,
            'is_a10_opt': False,
            'is_visible': True
        },
        'name': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': ''
        },
        'description': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': '',
        },
        'host': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'username': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'password': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_a10_opt': False,
            'is_visible': False,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'api_version': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:values': ['2.1', '3.0']
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'protocol': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:values': ['http', 'https']
            },
            'is_visible': True,
            'is_a10_opt': False,
            'convert_to': lambda attr: validators.convert_to_lower,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'port': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:range': [0, 65535]
            },
            'convert_to': lambda attr: attr.convert_to_int,
            'is_a10_opt': False,
            'is_visible': True,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'nova_instance_id': {
            'allow_post': False,
            'allow_put': False,
            'validate': {
                'type:uuid': None
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'management_network': {
            'allow_post': True,
            'allow_put': False,
            'validate': {
                'type:string': None,
            },
            'is_a10_opt': True,
            'is_visible': False,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED,
            'convert_list_to': lambda attr: attr.convert_to_list
        },
        'data_networks': {
            'allow_post': True,
            'allow_put': False,
            'validate': {
                'type:a10_list': {
                    'type:string': None,
                }
            },
            'is_a10_opt': True,
            'is_visible': False,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED,
            'convert_list_to': lambda attr: attr.convert_to_list
        },
        'image': {
            'allow_post': True,
            'allow_put': False,
            'validate': {
                'type:string': None,
            },
            'is_a10_opt': True,
            'is_visible': False,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'flavor': {
            'allow_post': True,
            'allow_put': False,
            'validate': {
                'type:string': None,
            },
            'is_a10_opt': True,
            'is_visible': False,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'a10_opts': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:a10_list': {
                    'type:string': None,
                }
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': []
        }

    },

    DEVICES: {
        'id': {
            'allow_post': False,
            'allow_put': True,
            'validate': {
                'type:uuid': None
            },
            'is_a10_opt': False,
            'is_visible': True,
            'primary_key': True
        },
        'tenant_id': {
            'allow_post': True,
            'allow_put': False,
            'required_by_policy': True,
            'is_a10_opt': False,
            'is_visible': True
        },
        'name': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': ''
        },
        'description': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': '',
        },
        'host': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'username': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'password': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_a10_opt': False,
            'is_visible': False,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'api_version': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:values': ['2.1', '3.0']
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'protocol': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:values': ['http', 'https']
            },
            'is_a10_opt': False,
            'is_visible': True,
            'convert_to': lambda attr: validators.convert_to_lower,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'port': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:range': [0, 65535]
            },
            'convert_to': lambda attr: attr.convert_to_int,
            'is_a10_opt': False,
            'is_visible': True,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'autosnat': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:boolean': None,
            },
            'convert_to': lambda attr: validators.convert_to_boolean,
            'is_a10_opt': True,
            'is_visible': True,
            'default': False
        },
        'v_method': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:values': ['LSI', 'ADP'],
            },
            'is_a10_opt': True,
            'is_visible': True,
            'default': 'LSI'
        },
        'status': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:boolean': None,
            },
            'convert_to': lambda attr: validators.convert_to_boolean,
            'is_a10_opt': True,
            'is_visible': True,
            'default': True
        },
        'source_nat_pool': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_a10_opt': True,
            'is_visible': True,
            'default': ''
        },
        'use_float': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:boolean': None,
            },
            'convert_to': lambda attr: validators.convert_to_boolean,
            'is_a10_opt': True,
            'is_visible': True,
            'default': False
        },
        'ipinip': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:boolean': None,
            },
            'convert_to': lambda attr: validators.convert_to_boolean,
            'is_a10_opt': True,
            'is_visible': True,
            'default': False
        },
        'write_memory': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:boolean': None,
            },
            'convert_to': lambda attr: validators.convert_to_boolean,
            'is_a10_opt': True,
            'is_visible': True,
            'default': True
        },
        'shared_partition': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None,
            },
            'is_a10_opt': True,
            'is_visible': True,
            'default': 'shared'
        },
        'ha_sync_list': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:a10_list': {
                    'type:string': None,
                }
            },
            'is_a10_opt': True,
            'is_visible': True,
            'convert_list_to': lambda attr: attr.convert_to_list,
            'default': []
        },
        'default_virtual_server_vrid': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:a10_nullable': {
                    'type:int': None,
                },
            },
            'is_a10_opt': True,
            'is_visible': True,
            'default': None
        },
        'conn_limit': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:range': [0, 8000000]
            },
            'convert_to': lambda attr: attr.convert_to_int,
            'is_a10_opt': True,
            'is_visible': True,
            'default': 8000000
        },
        'config': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                #'type:string': None,
                'type:a10_list': {
                    'type:string': None,
                }
            },
            #'convert_list_to': lambda attr: converters.convert_kvp_list_to_dict,
            'is_a10_opt': False,
            'is_visibile': True,
            #'default': '',
            'default': [],
        },
        'a10_opts': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:a10_list': {
                    'type:string': None,
                }
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': []
        }
    },

    DEVICE_KEYS: {
        'id': {
            'allow_post': False,
            'allow_put': False,
            'is_a10_opt': False,
            'is_visible': True,
            'primary_key': True,
            'validate': {
                'type:uuid': None
            }
        },
        'tenant_id': {
            'allow_post': True,
            'allow_put': False,
            'required_by_policy': True,
            'is_a10_opt': False,
            'is_visible': True
        },
        'name': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'description': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': '',
        },
    },

    DEVICE_VALUES: {
        'id': {
            'allow_post': False,
            'allow_put': False,
            'is_a10_opt': False,
            'is_visible': True,
            'primary_key': True,
            'validate': {
                'type:uuid': None
            }
        },
        'tenant_id': {
            'allow_post': True,
            'allow_put': False,
            'required_by_policy': True,
            'is_a10_opt': False,
            'is_visible': True
        },
        'value': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_a10_opt': False,
            'is_visible': True,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'key_id': {
            'allow_post': True,
            'allow_put': True,
            'is_a10_opt': False,
            'is_visible': True,
            'validate': {
                'type:uuid': None,
                'type:a10_reference': DEVICE_KEY,
            },
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'associated_obj_id': {
            'allow_post': True,
            'allow_put': True,
            'is_a10_opt': False,
            'is_visible': True,
            'validate': {
                'type:uuid': None,
                'type:a10_reference': DEVICE,
            },
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
    }
}

VALIDATORS = validators.VALIDATORS
