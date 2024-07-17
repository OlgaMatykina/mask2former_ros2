// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from segm_msgs:msg/Mask.idl
// generated code does not contain a copyright notice
#include "segm_msgs/msg/detail/mask__rosidl_typesupport_fastrtps_cpp.hpp"
#include "segm_msgs/msg/detail/mask__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace segm_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_segm_msgs
cdr_serialize(
  const segm_msgs::msg::Mask & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: mask
  {
    cdr << ros_message.mask;
  }
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_segm_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  segm_msgs::msg::Mask & ros_message)
{
  // Member: mask
  {
    cdr >> ros_message.mask;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_segm_msgs
get_serialized_size(
  const segm_msgs::msg::Mask & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: mask
  {
    size_t array_size = ros_message.mask.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    size_t item_size = sizeof(ros_message.mask[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_segm_msgs
max_serialized_size_Mask(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: mask
  {
    size_t array_size = 0;
    full_bounded = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static bool _Mask__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const segm_msgs::msg::Mask *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _Mask__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<segm_msgs::msg::Mask *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _Mask__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const segm_msgs::msg::Mask *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _Mask__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_Mask(full_bounded, 0);
}

static message_type_support_callbacks_t _Mask__callbacks = {
  "segm_msgs::msg",
  "Mask",
  _Mask__cdr_serialize,
  _Mask__cdr_deserialize,
  _Mask__get_serialized_size,
  _Mask__max_serialized_size
};

static rosidl_message_type_support_t _Mask__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_Mask__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace segm_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_segm_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<segm_msgs::msg::Mask>()
{
  return &segm_msgs::msg::typesupport_fastrtps_cpp::_Mask__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, segm_msgs, msg, Mask)() {
  return &segm_msgs::msg::typesupport_fastrtps_cpp::_Mask__handle;
}

#ifdef __cplusplus
}
#endif
