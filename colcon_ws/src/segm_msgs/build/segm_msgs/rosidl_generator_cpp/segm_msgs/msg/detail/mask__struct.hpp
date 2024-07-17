// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from segm_msgs:msg/Mask.idl
// generated code does not contain a copyright notice

#ifndef SEGM_MSGS__MSG__DETAIL__MASK__STRUCT_HPP_
#define SEGM_MSGS__MSG__DETAIL__MASK__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__segm_msgs__msg__Mask __attribute__((deprecated))
#else
# define DEPRECATED__segm_msgs__msg__Mask __declspec(deprecated)
#endif

namespace segm_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Mask_
{
  using Type = Mask_<ContainerAllocator>;

  explicit Mask_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit Mask_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _mask_type =
    std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other>;
  _mask_type mask;

  // setters for named parameter idiom
  Type & set__mask(
    const std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other> & _arg)
  {
    this->mask = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    segm_msgs::msg::Mask_<ContainerAllocator> *;
  using ConstRawPtr =
    const segm_msgs::msg::Mask_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<segm_msgs::msg::Mask_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<segm_msgs::msg::Mask_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      segm_msgs::msg::Mask_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<segm_msgs::msg::Mask_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      segm_msgs::msg::Mask_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<segm_msgs::msg::Mask_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<segm_msgs::msg::Mask_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<segm_msgs::msg::Mask_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__segm_msgs__msg__Mask
    std::shared_ptr<segm_msgs::msg::Mask_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__segm_msgs__msg__Mask
    std::shared_ptr<segm_msgs::msg::Mask_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Mask_ & other) const
  {
    if (this->mask != other.mask) {
      return false;
    }
    return true;
  }
  bool operator!=(const Mask_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Mask_

// alias to use template instance with default allocator
using Mask =
  segm_msgs::msg::Mask_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace segm_msgs

#endif  // SEGM_MSGS__MSG__DETAIL__MASK__STRUCT_HPP_
