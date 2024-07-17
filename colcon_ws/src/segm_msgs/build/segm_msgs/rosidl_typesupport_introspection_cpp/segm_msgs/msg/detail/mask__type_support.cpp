// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from segm_msgs:msg/Mask.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "segm_msgs/msg/detail/mask__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace segm_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Mask_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) segm_msgs::msg::Mask(_init);
}

void Mask_fini_function(void * message_memory)
{
  auto typed_message = static_cast<segm_msgs::msg::Mask *>(message_memory);
  typed_message->~Mask();
}

size_t size_function__Mask__mask(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<uint8_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Mask__mask(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<uint8_t> *>(untyped_member);
  return &member[index];
}

void * get_function__Mask__mask(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<uint8_t> *>(untyped_member);
  return &member[index];
}

void resize_function__Mask__mask(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<uint8_t> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Mask_message_member_array[1] = {
  {
    "mask",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(segm_msgs::msg::Mask, mask),  // bytes offset in struct
    nullptr,  // default value
    size_function__Mask__mask,  // size() function pointer
    get_const_function__Mask__mask,  // get_const(index) function pointer
    get_function__Mask__mask,  // get(index) function pointer
    resize_function__Mask__mask  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Mask_message_members = {
  "segm_msgs::msg",  // message namespace
  "Mask",  // message name
  1,  // number of fields
  sizeof(segm_msgs::msg::Mask),
  Mask_message_member_array,  // message members
  Mask_init_function,  // function to initialize message memory (memory has to be allocated)
  Mask_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Mask_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Mask_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace segm_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<segm_msgs::msg::Mask>()
{
  return &::segm_msgs::msg::rosidl_typesupport_introspection_cpp::Mask_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, segm_msgs, msg, Mask)() {
  return &::segm_msgs::msg::rosidl_typesupport_introspection_cpp::Mask_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
