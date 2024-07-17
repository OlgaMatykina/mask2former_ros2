// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from segm_msgs:msg/Obstacles.idl
// generated code does not contain a copyright notice

#ifndef SEGM_MSGS__MSG__DETAIL__OBSTACLES__STRUCT_H_
#define SEGM_MSGS__MSG__DETAIL__OBSTACLES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'classes_ids'
// Member 'distances'
#include "rosidl_runtime_c/primitives_sequence.h"
// Member 'masks'
#include "segm_msgs/msg/detail/mask__struct.h"

// Struct defined in msg/Obstacles in the package segm_msgs.
typedef struct segm_msgs__msg__Obstacles
{
  std_msgs__msg__Header header;
  int32_t num;
  rosidl_runtime_c__int32__Sequence classes_ids;
  segm_msgs__msg__Mask__Sequence masks;
  rosidl_runtime_c__float__Sequence distances;
} segm_msgs__msg__Obstacles;

// Struct for a sequence of segm_msgs__msg__Obstacles.
typedef struct segm_msgs__msg__Obstacles__Sequence
{
  segm_msgs__msg__Obstacles * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} segm_msgs__msg__Obstacles__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SEGM_MSGS__MSG__DETAIL__OBSTACLES__STRUCT_H_
