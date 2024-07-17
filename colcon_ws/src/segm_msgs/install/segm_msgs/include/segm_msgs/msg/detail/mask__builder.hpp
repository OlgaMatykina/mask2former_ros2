// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from segm_msgs:msg/Mask.idl
// generated code does not contain a copyright notice

#ifndef SEGM_MSGS__MSG__DETAIL__MASK__BUILDER_HPP_
#define SEGM_MSGS__MSG__DETAIL__MASK__BUILDER_HPP_

#include "segm_msgs/msg/detail/mask__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace segm_msgs
{

namespace msg
{

namespace builder
{

class Init_Mask_mask
{
public:
  Init_Mask_mask()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::segm_msgs::msg::Mask mask(::segm_msgs::msg::Mask::_mask_type arg)
  {
    msg_.mask = std::move(arg);
    return std::move(msg_);
  }

private:
  ::segm_msgs::msg::Mask msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::segm_msgs::msg::Mask>()
{
  return segm_msgs::msg::builder::Init_Mask_mask();
}

}  // namespace segm_msgs

#endif  // SEGM_MSGS__MSG__DETAIL__MASK__BUILDER_HPP_
