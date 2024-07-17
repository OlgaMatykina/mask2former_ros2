// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from segm_msgs:msg/Mask.idl
// generated code does not contain a copyright notice

#ifndef SEGM_MSGS__MSG__DETAIL__MASK__FUNCTIONS_H_
#define SEGM_MSGS__MSG__DETAIL__MASK__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "segm_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "segm_msgs/msg/detail/mask__struct.h"

/// Initialize msg/Mask message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * segm_msgs__msg__Mask
 * )) before or use
 * segm_msgs__msg__Mask__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_segm_msgs
bool
segm_msgs__msg__Mask__init(segm_msgs__msg__Mask * msg);

/// Finalize msg/Mask message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_segm_msgs
void
segm_msgs__msg__Mask__fini(segm_msgs__msg__Mask * msg);

/// Create msg/Mask message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * segm_msgs__msg__Mask__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_segm_msgs
segm_msgs__msg__Mask *
segm_msgs__msg__Mask__create();

/// Destroy msg/Mask message.
/**
 * It calls
 * segm_msgs__msg__Mask__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_segm_msgs
void
segm_msgs__msg__Mask__destroy(segm_msgs__msg__Mask * msg);

/// Check for msg/Mask message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_segm_msgs
bool
segm_msgs__msg__Mask__are_equal(const segm_msgs__msg__Mask * lhs, const segm_msgs__msg__Mask * rhs);

/// Copy a msg/Mask message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_segm_msgs
bool
segm_msgs__msg__Mask__copy(
  const segm_msgs__msg__Mask * input,
  segm_msgs__msg__Mask * output);

/// Initialize array of msg/Mask messages.
/**
 * It allocates the memory for the number of elements and calls
 * segm_msgs__msg__Mask__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_segm_msgs
bool
segm_msgs__msg__Mask__Sequence__init(segm_msgs__msg__Mask__Sequence * array, size_t size);

/// Finalize array of msg/Mask messages.
/**
 * It calls
 * segm_msgs__msg__Mask__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_segm_msgs
void
segm_msgs__msg__Mask__Sequence__fini(segm_msgs__msg__Mask__Sequence * array);

/// Create array of msg/Mask messages.
/**
 * It allocates the memory for the array and calls
 * segm_msgs__msg__Mask__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_segm_msgs
segm_msgs__msg__Mask__Sequence *
segm_msgs__msg__Mask__Sequence__create(size_t size);

/// Destroy array of msg/Mask messages.
/**
 * It calls
 * segm_msgs__msg__Mask__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_segm_msgs
void
segm_msgs__msg__Mask__Sequence__destroy(segm_msgs__msg__Mask__Sequence * array);

/// Check for msg/Mask message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_segm_msgs
bool
segm_msgs__msg__Mask__Sequence__are_equal(const segm_msgs__msg__Mask__Sequence * lhs, const segm_msgs__msg__Mask__Sequence * rhs);

/// Copy an array of msg/Mask messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_segm_msgs
bool
segm_msgs__msg__Mask__Sequence__copy(
  const segm_msgs__msg__Mask__Sequence * input,
  segm_msgs__msg__Mask__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // SEGM_MSGS__MSG__DETAIL__MASK__FUNCTIONS_H_
