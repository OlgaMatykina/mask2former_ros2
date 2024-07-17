// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from segm_msgs:msg/Obstacles.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "segm_msgs/msg/detail/obstacles__struct.hpp"
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

void Obstacles_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) segm_msgs::msg::Obstacles(_init);
}

void Obstacles_fini_function(void * message_memory)
{
  auto typed_message = static_cast<segm_msgs::msg::Obstacles *>(message_memory);
  typed_message->~Obstacles();
}

size_t size_function__Obstacles__classes_ids(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Obstacles__classes_ids(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__Obstacles__classes_ids(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void resize_function__Obstacles__classes_ids(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

size_t size_function__Obstacles__masks(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<segm_msgs::msg::Mask> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Obstacles__masks(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<segm_msgs::msg::Mask> *>(untyped_member);
  return &member[index];
}

void * get_function__Obstacles__masks(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<segm_msgs::msg::Mask> *>(untyped_member);
  return &member[index];
}

void resize_function__Obstacles__masks(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<segm_msgs::msg::Mask> *>(untyped_member);
  member->resize(size);
}

size_t size_function__Obstacles__distances(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Obstacles__distances(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__Obstacles__distances(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void resize_function__Obstacles__distances(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Obstacles_message_member_array[5] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(segm_msgs::msg::Obstacles, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "num",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(segm_msgs::msg::Obstacles, num),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "classes_ids",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(segm_msgs::msg::Obstacles, classes_ids),  // bytes offset in struct
    nullptr,  // default value
    size_function__Obstacles__classes_ids,  // size() function pointer
    get_const_function__Obstacles__classes_ids,  // get_const(index) function pointer
    get_function__Obstacles__classes_ids,  // get(index) function pointer
    resize_function__Obstacles__classes_ids  // resize(index) function pointer
  },
  {
    "masks",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<segm_msgs::msg::Mask>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(segm_msgs::msg::Obstacles, masks),  // bytes offset in struct
    nullptr,  // default value
    size_function__Obstacles__masks,  // size() function pointer
    get_const_function__Obstacles__masks,  // get_const(index) function pointer
    get_function__Obstacles__masks,  // get(index) function pointer
    resize_function__Obstacles__masks  // resize(index) function pointer
  },
  {
    "distances",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(segm_msgs::msg::Obstacles, distances),  // bytes offset in struct
    nullptr,  // default value
    size_function__Obstacles__distances,  // size() function pointer
    get_const_function__Obstacles__distances,  // get_const(index) function pointer
    get_function__Obstacles__distances,  // get(index) function pointer
    resize_function__Obstacles__distances  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Obstacles_message_members = {
  "segm_msgs::msg",  // message namespace
  "Obstacles",  // message name
  5,  // number of fields
  sizeof(segm_msgs::msg::Obstacles),
  Obstacles_message_member_array,  // message members
  Obstacles_init_function,  // function to initialize message memory (memory has to be allocated)
  Obstacles_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Obstacles_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Obstacles_message_members,
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
get_message_type_support_handle<segm_msgs::msg::Obstacles>()
{
  return &::segm_msgs::msg::rosidl_typesupport_introspection_cpp::Obstacles_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, segm_msgs, msg, Obstacles)() {
  return &::segm_msgs::msg::rosidl_typesupport_introspection_cpp::Obstacles_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
