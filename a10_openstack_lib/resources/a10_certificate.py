# Copyright (C) 2016 A10 Networks Inc. All rights reserved.
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

EXTENSION = 'a10-certificate'

SERVICE = "A10_CERTIFICATE"

CERTIFICATES = 'a10_certificates'
CERTIFICATE = 'a10_certificate'

CERTIFICATE_BINDING = 'a10_certificate_binding'
CERTIFICATE_BINDINGS = 'a10_certificate_bindings'

RESOURCE_ATTRIBUTE_MAP = {
    CERTIFICATES: {
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
        'cert_data': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_visible': True,
            'required_by_policy': True
        },
        'key_data': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None
            },
            'is_visible': True,
            'default': ''
        },
        'intermediate_data': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None,
            },
            'is_visible': True,
            'default': ''
        },
        'password': {
            'allow_post': True,
            'allow_put': True,
            'validate': {
                'type:string': None,
            },
            'is_visible': True,
            'default': ''

        }
    },

    CERTIFICATE_BINDINGS: {
        'id': {
            'allow_post': False,
            'allow_put': False,
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
            'is_visible': True
        },
        'certificate_id': {
            'allow_post': True,
            'allow_put': True,
            'is_visible': True
        },
        'listener_id': {
            'allow_post': True,
            'allow_put': True,
            'is_visible': True
        },
        'listener_name': {
            'allow_post': False,
            'allow_put': False,
            'is_visible': True
        },
        'certificate_name': {
            'allow_post': False,
            'allow_put': False,
            'is_visible': True
        }
    }
}


def convert_to_lower(input):
    try:
        return input.lower()
    except AttributeError:
        return input


def convert_to_float(input):
    try:
        return float(input)
    except ValueError:
        return input


def convert_nullable(convert_value):
    def f(input):
        if input is not None:
            return convert_value(input)
        return None
    return f


def validate_float(data, options):
    if not isinstance(data, float):
        return "'%s' is not a number" % input


def validate_reference(data, options):
    """Referential integrity is enforced by the data model"""
    return None


def validate_nullable(validators):
    def f(data, options):
        if data is not None:
            for rule in options:
                value_validator = validators[rule]
                reason = value_validator(data, options[rule])
                if reason:
                    return reason
    return f


VALIDATORS = {
    'a10_type:float': lambda validators: validate_float,
    'a10_type:reference': lambda validators: validate_reference,
    'a10_type:nullable': validate_nullable
}
