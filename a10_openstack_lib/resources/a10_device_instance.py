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

EXTENSION = 'a10-device-instance'

SERVICE = "A10_DEVICE_INSTANCE"

RESOURCES = 'a10_device_instances'
RESOURCE = 'a10_device_instance'

RESOURCE_ATTRIBUTE_MAP = {
    RESOURCES: {
        'id': {
            'allow_post': False,
            'allow_put': True,
            'validate': {
                'type:uuid': None
            },
            'is_visible': True,
            'primary_key': True
        },
        'tenant_id': {
            'allow_post': True,
            'allow_put': False,
            'required_by_policy': True,
            'is_visible': True
        },
        'name': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_visible': True,
            'default': ''
        },
        'description': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_visible': True,
            'default': '',
        },
        'host': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_visible': True,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'username': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_visible': True,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'password': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_visible': False,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'api_version': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:values': ['2.1', '3.0']
            },
            'is_visible': True
        },
        'protocol': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:values': ['http', 'https']
            },
            'is_visible': True,
            'convert_to': lambda attr: convert_to_lower,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'port': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:range': [0, 65535]
            },
            'convert_to': lambda attr: attr.convert_to_int,
            'is_visible': True,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'nova_instance_id': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:uuid': None
            },
            'is_visible': True,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'networks': {
            'allow_post': True,
            'allow_put': True,
            'is_visible': False,
            'default': [],
            'convert_list_to': lambda attr: attr.convert_to_list
        },
        'image': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None,
            },
            'is_visible': False,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        },
        'flavor': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None,
            },
            'is_visible': False,
            'default': lambda attr: attr.ATTR_NOT_SPECIFIED
        }

    }
}


def convert_to_lower(input):
    try:
        return input.lower()
    except AttributeError:
        return input


def convert_to_int(input):
    try:
        return int(input)
    except ValueError:
        return 0


class AttributesLibWrapper(object):
    """Neutron lib moves stuff. Move it back."""

    def __init__(self, attributes):
        self._attributes = attributes
        self._converters = getattr(attributes, 'converters', {})
        self._validators = getattr(attributes, 'validators', {})

    def __getattr__(self, key):
        try:
            return getattr(self._attributes, key)
        except:
            pass

        # Maybe it moved to converters
        try:
            return getattr(self._attributes.converters, key)
        except:
            pass

        # Maybe it moved to validators
        try:
            return getattr(self._attributes.validators, key)
        except:
            pass

        # Dave's not here, man
        return self.__getattribute__(key)
