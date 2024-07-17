// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from segm_msgs:msg/Obstacles.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "segm_msgs/msg/detail/obstacles__rosidl_typesupport_introspection_c.h"
#include "segm_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "segm_msgs/msg/detail/obstacles__functions.h"
#include "segm_msgs/msg/detail/obstacles__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `classes_ids`
// Member `distances`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `masks`
#include "segm_msgs/msg/mask.h"
// Member `masks`
#include "segm_msgs/msg/detail/mask__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void Obstacles__rosidl_typesupport_introspection_c__Obstacles_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  segm_msgs__msg__Obstacles__init(message_memory);
}

void Obstacles__rosidl_typesupport_introspection_c__Obstacles_fini_function(void * message_memory)
{
  segm_msgs__msg__Obstacles__fini(message_memory);
}

size_t Obstacles__rosidl_typesupport_introspection_c__size_function__Mask__masks(
  const void * untyped_member)
{
  const segm_msgs__msg__Mask__Sequence * member =
    (const segm_msgs__msg__Mask__Sequence *)(untyped_member);
  return member->size;
}

const void * Obstacles__rosidl_typesupport_introspection_c__get_const_function__Mask__masks(
  const void * untyped_member, size_t index)
{
  const segm_msgs__msg__Mask__Sequence * member =
    (const segm_msgs__msg__Mask__Sequence *)(untyped_member);
  return &member->data[index];
}

void * Obstacles__rosidl_typesupport_introspection_c__get_function__Mask__masks(
  void * untyped_member, size_t index)
{
  segm_msgs__msg__Mask__Sequence * member =
    (segm_msgs__msg__Mask__Sequence *)(untyped_member);
  return &member->data[index];
}

bool Obstacles__rosidl_typesupport_introspection_c__resize_function__Mask__masks(
  void * untyped_member, size_t size)
{
  segm_msgs__msg__Mask__Sequence * member =
    (segm_msgs__msg__Mask__Sequence *)(untyped_member);
  segm_msgs__msg__Mask__Sequence__fini(member);
  return segm_msgs__msg__Mask__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember Obstacles__rosidl_typesupport_introspection_c__Obstacles_message_member_array[5] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(segm_msgs__msg__Obstacles, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "num",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(segm_msgs__msg__Obstacles, num),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "classes_ids",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(segm_msgs__msg__Obstacles, classes_ids),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "masks",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(segm_msgs__msg__Obstacles, masks),  // bytes offset in struct
    NULL,  // default value
    Obstacles__rosidl_typesupport_introspection_c__size_function__Mask__masks,  // size() function pointer
    Obstacles__rosidl_typesupport_introspection_c__get_const_function__Mask__masks,  // get_const(index) function pointer
    Obstacles__rosidl_typesupport_introspection_c__get_function__Mask__masks,  // get(index) function pointer
    Obstacles__rosidl_typesupport_introspection_c__resize_function__Mask__masks  // resize(index) function pointer
  },
  {
    "distances",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(segm_msgs__msg__Obstacles, distances),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Obstacles__rosidl_typesupport_introspection_c__Obstacles_message_members = {
  "segm_msgs__msg",  // message namespace
  "Obstacles",  // message name
  5,  // number of fields
  sizeof(segm_msgs__msg__Obstacles),
  Obstacles__rosidl_typesupport_introspection_c__Obstacles_message_member_array,  // message members
  Obstacles__rosidl_typesupport_introspection_c__Obstacles_init_function,  // function to initialize message memory (memory has to be allocated)
  Obstacles__rosidl_typesupport_introspection_c__Obstacles_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Obstacles__rosidl_typesupport_introspection_c__Obstacles_message_type_support_handle = {
  0,
  &Obstacles__rosidl_typesupport_introspection_c__Obstacles_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_segm_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, segm_msgs, msg, Obstacles)() {
  Obstacles__rosidl_typesupport_introspection_c__Obstacles_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  Obstacles__rosidl_typesupport_introspection_c__Obstacles_message_member_array[3].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, segm_msgs, msg, Mask)();
  if (!Obstacles__rosidl_typesupport_introspection_c__Obstacles_message_type_support_handle.typesupport_identifier) {
    Obstacles__rosidl_typesupport_introspection_c__Obstacles_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Obstacles__rosidl_typesupport_introspection_c__Obstacles_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
