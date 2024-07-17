// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from segm_msgs:msg/Mask.idl
// generated code does not contain a copyright notice

#ifndef SEGM_MSGS__MSG__DETAIL__MASK__STRUCT_H_
#define SEGM_MSGS__MSG__DETAIL__MASK__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'mask'
#include "rosidl_runtime_c/primitives_sequence.h"

// Struct defined in msg/Mask in the package segm_msgs.
typedef struct segm_msgs__msg__Mask
{
  rosidl_runtime_c__uint8__Sequence mask;
} segm_msgs__msg__Mask;

// Struct for a sequence of segm_msgs__msg__Mask.
typedef struct segm_msgs__msg__Mask__Sequence
{
  segm_msgs__msg__Mask * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} segm_msgs__msg__Mask__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SEGM_MSGS__MSG__DETAIL__MASK__STRUCT_H_
