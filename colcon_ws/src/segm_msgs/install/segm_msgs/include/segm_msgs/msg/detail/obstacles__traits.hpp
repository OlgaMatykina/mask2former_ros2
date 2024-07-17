// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from segm_msgs:msg/Obstacles.idl
// generated code does not contain a copyright notice

#ifndef SEGM_MSGS__MSG__DETAIL__OBSTACLES__TRAITS_HPP_
#define SEGM_MSGS__MSG__DETAIL__OBSTACLES__TRAITS_HPP_

#include "segm_msgs/msg/detail/obstacles__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<segm_msgs::msg::Obstacles>()
{
  return "segm_msgs::msg::Obstacles";
}

template<>
inline const char * name<segm_msgs::msg::Obstacles>()
{
  return "segm_msgs/msg/Obstacles";
}

template<>
struct has_fixed_size<segm_msgs::msg::Obstacles>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<segm_msgs::msg::Obstacles>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<segm_msgs::msg::Obstacles>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SEGM_MSGS__MSG__DETAIL__OBSTACLES__TRAITS_HPP_
