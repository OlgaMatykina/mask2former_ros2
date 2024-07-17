// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from segm_msgs:msg/Obstacles.idl
// generated code does not contain a copyright notice

#ifndef SEGM_MSGS__MSG__DETAIL__OBSTACLES__BUILDER_HPP_
#define SEGM_MSGS__MSG__DETAIL__OBSTACLES__BUILDER_HPP_

#include "segm_msgs/msg/detail/obstacles__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace segm_msgs
{

namespace msg
{

namespace builder
{

class Init_Obstacles_distances
{
public:
  explicit Init_Obstacles_distances(::segm_msgs::msg::Obstacles & msg)
  : msg_(msg)
  {}
  ::segm_msgs::msg::Obstacles distances(::segm_msgs::msg::Obstacles::_distances_type arg)
  {
    msg_.distances = std::move(arg);
    return std::move(msg_);
  }

private:
  ::segm_msgs::msg::Obstacles msg_;
};

class Init_Obstacles_masks
{
public:
  explicit Init_Obstacles_masks(::segm_msgs::msg::Obstacles & msg)
  : msg_(msg)
  {}
  Init_Obstacles_distances masks(::segm_msgs::msg::Obstacles::_masks_type arg)
  {
    msg_.masks = std::move(arg);
    return Init_Obstacles_distances(msg_);
  }

private:
  ::segm_msgs::msg::Obstacles msg_;
};

class Init_Obstacles_classes_ids
{
public:
  explicit Init_Obstacles_classes_ids(::segm_msgs::msg::Obstacles & msg)
  : msg_(msg)
  {}
  Init_Obstacles_masks classes_ids(::segm_msgs::msg::Obstacles::_classes_ids_type arg)
  {
    msg_.classes_ids = std::move(arg);
    return Init_Obstacles_masks(msg_);
  }

private:
  ::segm_msgs::msg::Obstacles msg_;
};

class Init_Obstacles_num
{
public:
  explicit Init_Obstacles_num(::segm_msgs::msg::Obstacles & msg)
  : msg_(msg)
  {}
  Init_Obstacles_classes_ids num(::segm_msgs::msg::Obstacles::_num_type arg)
  {
    msg_.num = std::move(arg);
    return Init_Obstacles_classes_ids(msg_);
  }

private:
  ::segm_msgs::msg::Obstacles msg_;
};

class Init_Obstacles_header
{
public:
  Init_Obstacles_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Obstacles_num header(::segm_msgs::msg::Obstacles::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Obstacles_num(msg_);
  }

private:
  ::segm_msgs::msg::Obstacles msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::segm_msgs::msg::Obstacles>()
{
  return segm_msgs::msg::builder::Init_Obstacles_header();
}

}  // namespace segm_msgs

#endif  // SEGM_MSGS__MSG__DETAIL__OBSTACLES__BUILDER_HPP_
