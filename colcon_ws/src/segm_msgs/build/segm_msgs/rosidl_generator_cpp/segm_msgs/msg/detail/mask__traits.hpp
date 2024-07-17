// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from segm_msgs:msg/Mask.idl
// generated code does not contain a copyright notice

#ifndef SEGM_MSGS__MSG__DETAIL__MASK__TRAITS_HPP_
#define SEGM_MSGS__MSG__DETAIL__MASK__TRAITS_HPP_

#include "segm_msgs/msg/detail/mask__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<segm_msgs::msg::Mask>()
{
  return "segm_msgs::msg::Mask";
}

template<>
inline const char * name<segm_msgs::msg::Mask>()
{
  return "segm_msgs/msg/Mask";
}

template<>
struct has_fixed_size<segm_msgs::msg::Mask>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<segm_msgs::msg::Mask>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<segm_msgs::msg::Mask>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SEGM_MSGS__MSG__DETAIL__MASK__TRAITS_HPP_
