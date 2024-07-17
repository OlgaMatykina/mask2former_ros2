// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from segm_msgs:msg/Mask.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "segm_msgs/msg/detail/mask__rosidl_typesupport_introspection_c.h"
#include "segm_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "segm_msgs/msg/detail/mask__functions.h"
#include "segm_msgs/msg/detail/mask__struct.h"


// Include directives for member types
// Member `mask`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void Mask__rosidl_typesupport_introspection_c__Mask_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  segm_msgs__msg__Mask__init(message_memory);
}

void Mask__rosidl_typesupport_introspection_c__Mask_fini_function(void * message_memory)
{
  segm_msgs__msg__Mask__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Mask__rosidl_typesupport_introspection_c__Mask_message_member_array[1] = {
  {
    "mask",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(segm_msgs__msg__Mask, mask),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Mask__rosidl_typesupport_introspection_c__Mask_message_members = {
  "segm_msgs__msg",  // message namespace
  "Mask",  // message name
  1,  // number of fields
  sizeof(segm_msgs__msg__Mask),
  Mask__rosidl_typesupport_introspection_c__Mask_message_member_array,  // message members
  Mask__rosidl_typesupport_introspection_c__Mask_init_function,  // function to initialize message memory (memory has to be allocated)
  Mask__rosidl_typesupport_introspection_c__Mask_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Mask__rosidl_typesupport_introspection_c__Mask_message_type_support_handle = {
  0,
  &Mask__rosidl_typesupport_introspection_c__Mask_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_segm_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, segm_msgs, msg, Mask)() {
  if (!Mask__rosidl_typesupport_introspection_c__Mask_message_type_support_handle.typesupport_identifier) {
    Mask__rosidl_typesupport_introspection_c__Mask_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Mask__rosidl_typesupport_introspection_c__Mask_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
