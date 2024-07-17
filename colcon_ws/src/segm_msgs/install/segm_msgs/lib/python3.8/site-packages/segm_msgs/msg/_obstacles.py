# generated from rosidl_generator_py/resource/_idl.py.em
# with input from segm_msgs:msg/Obstacles.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'classes_ids'
# Member 'distances'
import array  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Obstacles(type):
    """Metaclass of message 'Obstacles'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('segm_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'segm_msgs.msg.Obstacles')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__obstacles
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__obstacles
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__obstacles
            cls._TYPE_SUPPORT = module.type_support_msg__msg__obstacles
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__obstacles

            from segm_msgs.msg import Mask
            if Mask.__class__._TYPE_SUPPORT is None:
                Mask.__class__.__import_type_support__()

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Obstacles(metaclass=Metaclass_Obstacles):
    """Message class 'Obstacles'."""

    __slots__ = [
        '_header',
        '_num',
        '_classes_ids',
        '_masks',
        '_distances',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'num': 'int32',
        'classes_ids': 'sequence<int32>',
        'masks': 'sequence<segm_msgs/Mask>',
        'distances': 'sequence<float>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int32')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['segm_msgs', 'msg'], 'Mask')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.num = kwargs.get('num', int())
        self.classes_ids = array.array('i', kwargs.get('classes_ids', []))
        self.masks = kwargs.get('masks', [])
        self.distances = array.array('f', kwargs.get('distances', []))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.num != other.num:
            return False
        if self.classes_ids != other.classes_ids:
            return False
        if self.masks != other.masks:
            return False
        if self.distances != other.distances:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @property
    def num(self):
        """Message field 'num'."""
        return self._num

    @num.setter
    def num(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'num' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'num' field must be an integer in [-2147483648, 2147483647]"
        self._num = value

    @property
    def classes_ids(self):
        """Message field 'classes_ids'."""
        return self._classes_ids

    @classes_ids.setter
    def classes_ids(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'i', \
                "The 'classes_ids' array.array() must have the type code of 'i'"
            self._classes_ids = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -2147483648 and val < 2147483648 for val in value)), \
                "The 'classes_ids' field must be a set or sequence and each value of type 'int' and each integer in [-2147483648, 2147483647]"
        self._classes_ids = array.array('i', value)

    @property
    def masks(self):
        """Message field 'masks'."""
        return self._masks

    @masks.setter
    def masks(self, value):
        if __debug__:
            from segm_msgs.msg import Mask
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, Mask) for v in value) and
                 True), \
                "The 'masks' field must be a set or sequence and each value of type 'Mask'"
        self._masks = value

    @property
    def distances(self):
        """Message field 'distances'."""
        return self._distances

    @distances.setter
    def distances(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'distances' array.array() must have the type code of 'f'"
            self._distances = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'distances' field must be a set or sequence and each value of type 'float'"
        self._distances = array.array('f', value)
