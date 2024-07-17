// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from segm_msgs:msg/Obstacles.idl
// generated code does not contain a copyright notice
#include "segm_msgs/msg/detail/obstacles__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "segm_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "segm_msgs/msg/detail/obstacles__struct.h"
#include "segm_msgs/msg/detail/obstacles__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/primitives_sequence.h"  // classes_ids, distances
#include "rosidl_runtime_c/primitives_sequence_functions.h"  // classes_ids, distances
#include "segm_msgs/msg/detail/mask__functions.h"  // masks
#include "std_msgs/msg/detail/header__functions.h"  // header

// forward declare type support functions
size_t get_serialized_size_segm_msgs__msg__Mask(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_segm_msgs__msg__Mask(
  bool & full_bounded,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, segm_msgs, msg, Mask)();
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_segm_msgs
size_t get_serialized_size_std_msgs__msg__Header(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_segm_msgs
size_t max_serialized_size_std_msgs__msg__Header(
  bool & full_bounded,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_segm_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, std_msgs, msg, Header)();


using _Obstacles__ros_msg_type = segm_msgs__msg__Obstacles;

static bool _Obstacles__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Obstacles__ros_msg_type * ros_message = static_cast<const _Obstacles__ros_msg_type *>(untyped_ros_message);
  // Field name: header
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, Header
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->header, cdr))
    {
      return false;
    }
  }

  // Field name: num
  {
    cdr << ros_message->num;
  }

  // Field name: classes_ids
  {
    size_t size = ros_message->classes_ids.size;
    auto array_ptr = ros_message->classes_ids.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: masks
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, segm_msgs, msg, Mask
      )()->data);
    size_t size = ros_message->masks.size;
    auto array_ptr = ros_message->masks.data;
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_serialize(
          &array_ptr[i], cdr))
      {
        return false;
      }
    }
  }

  // Field name: distances
  {
    size_t size = ros_message->distances.size;
    auto array_ptr = ros_message->distances.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  return true;
}

static bool _Obstacles__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Obstacles__ros_msg_type * ros_message = static_cast<_Obstacles__ros_msg_type *>(untyped_ros_message);
  // Field name: header
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, Header
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->header))
    {
      return false;
    }
  }

  // Field name: num
  {
    cdr >> ros_message->num;
  }

  // Field name: classes_ids
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->classes_ids.data) {
      rosidl_runtime_c__int32__Sequence__fini(&ros_message->classes_ids);
    }
    if (!rosidl_runtime_c__int32__Sequence__init(&ros_message->classes_ids, size)) {
      return "failed to create array for field 'classes_ids'";
    }
    auto array_ptr = ros_message->classes_ids.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: masks
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, segm_msgs, msg, Mask
      )()->data);
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->masks.data) {
      segm_msgs__msg__Mask__Sequence__fini(&ros_message->masks);
    }
    if (!segm_msgs__msg__Mask__Sequence__init(&ros_message->masks, size)) {
      return "failed to create array for field 'masks'";
    }
    auto array_ptr = ros_message->masks.data;
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_deserialize(
          cdr, &array_ptr[i]))
      {
        return false;
      }
    }
  }

  // Field name: distances
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->distances.data) {
      rosidl_runtime_c__float__Sequence__fini(&ros_message->distances);
    }
    if (!rosidl_runtime_c__float__Sequence__init(&ros_message->distances, size)) {
      return "failed to create array for field 'distances'";
    }
    auto array_ptr = ros_message->distances.data;
    cdr.deserializeArray(array_ptr, size);
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_segm_msgs
size_t get_serialized_size_segm_msgs__msg__Obstacles(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Obstacles__ros_msg_type * ros_message = static_cast<const _Obstacles__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name header

  current_alignment += get_serialized_size_std_msgs__msg__Header(
    &(ros_message->header), current_alignment);
  // field.name num
  {
    size_t item_size = sizeof(ros_message->num);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name classes_ids
  {
    size_t array_size = ros_message->classes_ids.size;
    auto array_ptr = ros_message->classes_ids.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name masks
  {
    size_t array_size = ros_message->masks.size;
    auto array_ptr = ros_message->masks.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += get_serialized_size_segm_msgs__msg__Mask(
        &array_ptr[index], current_alignment);
    }
  }
  // field.name distances
  {
    size_t array_size = ros_message->distances.size;
    auto array_ptr = ros_message->distances.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Obstacles__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_segm_msgs__msg__Obstacles(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_segm_msgs
size_t max_serialized_size_segm_msgs__msg__Obstacles(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: header
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_std_msgs__msg__Header(
        full_bounded, current_alignment);
    }
  }
  // member: num
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: classes_ids
  {
    size_t array_size = 0;
    full_bounded = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: masks
  {
    size_t array_size = 0;
    full_bounded = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_segm_msgs__msg__Mask(
        full_bounded, current_alignment);
    }
  }
  // member: distances
  {
    size_t array_size = 0;
    full_bounded = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _Obstacles__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_segm_msgs__msg__Obstacles(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_Obstacles = {
  "segm_msgs::msg",
  "Obstacles",
  _Obstacles__cdr_serialize,
  _Obstacles__cdr_deserialize,
  _Obstacles__get_serialized_size,
  _Obstacles__max_serialized_size
};

static rosidl_message_type_support_t _Obstacles__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Obstacles,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, segm_msgs, msg, Obstacles)() {
  return &_Obstacles__type_support;
}

#if defined(__cplusplus)
}
#endif
