// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from segm_msgs:msg/Mask.idl
// generated code does not contain a copyright notice

#ifndef SEGM_MSGS__MSG__DETAIL__MASK__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define SEGM_MSGS__MSG__DETAIL__MASK__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "segm_msgs/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "segm_msgs/msg/detail/mask__struct.hpp"

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

#include "fastcdr/Cdr.h"

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
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_segm_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  segm_msgs::msg::Mask & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_segm_msgs
get_serialized_size(
  const segm_msgs::msg::Mask & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_segm_msgs
max_serialized_size_Mask(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace segm_msgs

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_segm_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, segm_msgs, msg, Mask)();

#ifdef __cplusplus
}
#endif

#endif  // SEGM_MSGS__MSG__DETAIL__MASK__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
