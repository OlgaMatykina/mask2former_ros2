// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from segm_msgs:msg/Obstacles.idl
// generated code does not contain a copyright notice

#ifndef SEGM_MSGS__MSG__DETAIL__OBSTACLES__STRUCT_HPP_
#define SEGM_MSGS__MSG__DETAIL__OBSTACLES__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"
// Member 'masks'
#include "segm_msgs/msg/detail/mask__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__segm_msgs__msg__Obstacles __attribute__((deprecated))
#else
# define DEPRECATED__segm_msgs__msg__Obstacles __declspec(deprecated)
#endif

namespace segm_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Obstacles_
{
  using Type = Obstacles_<ContainerAllocator>;

  explicit Obstacles_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->num = 0l;
    }
  }

  explicit Obstacles_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->num = 0l;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _num_type =
    int32_t;
  _num_type num;
  using _classes_ids_type =
    std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other>;
  _classes_ids_type classes_ids;
  using _masks_type =
    std::vector<segm_msgs::msg::Mask_<ContainerAllocator>, typename ContainerAllocator::template rebind<segm_msgs::msg::Mask_<ContainerAllocator>>::other>;
  _masks_type masks;
  using _distances_type =
    std::vector<float, typename ContainerAllocator::template rebind<float>::other>;
  _distances_type distances;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__num(
    const int32_t & _arg)
  {
    this->num = _arg;
    return *this;
  }
  Type & set__classes_ids(
    const std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other> & _arg)
  {
    this->classes_ids = _arg;
    return *this;
  }
  Type & set__masks(
    const std::vector<segm_msgs::msg::Mask_<ContainerAllocator>, typename ContainerAllocator::template rebind<segm_msgs::msg::Mask_<ContainerAllocator>>::other> & _arg)
  {
    this->masks = _arg;
    return *this;
  }
  Type & set__distances(
    const std::vector<float, typename ContainerAllocator::template rebind<float>::other> & _arg)
  {
    this->distances = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    segm_msgs::msg::Obstacles_<ContainerAllocator> *;
  using ConstRawPtr =
    const segm_msgs::msg::Obstacles_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<segm_msgs::msg::Obstacles_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<segm_msgs::msg::Obstacles_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      segm_msgs::msg::Obstacles_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<segm_msgs::msg::Obstacles_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      segm_msgs::msg::Obstacles_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<segm_msgs::msg::Obstacles_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<segm_msgs::msg::Obstacles_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<segm_msgs::msg::Obstacles_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__segm_msgs__msg__Obstacles
    std::shared_ptr<segm_msgs::msg::Obstacles_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__segm_msgs__msg__Obstacles
    std::shared_ptr<segm_msgs::msg::Obstacles_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Obstacles_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->num != other.num) {
      return false;
    }
    if (this->classes_ids != other.classes_ids) {
      return false;
    }
    if (this->masks != other.masks) {
      return false;
    }
    if (this->distances != other.distances) {
      return false;
    }
    return true;
  }
  bool operator!=(const Obstacles_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Obstacles_

// alias to use template instance with default allocator
using Obstacles =
  segm_msgs::msg::Obstacles_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace segm_msgs

#endif  // SEGM_MSGS__MSG__DETAIL__OBSTACLES__STRUCT_HPP_
