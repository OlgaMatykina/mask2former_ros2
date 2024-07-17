// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from segm_msgs:msg/Obstacles.idl
// generated code does not contain a copyright notice
#include "segm_msgs/msg/detail/obstacles__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `classes_ids`
// Member `distances`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `masks`
#include "segm_msgs/msg/detail/mask__functions.h"

bool
segm_msgs__msg__Obstacles__init(segm_msgs__msg__Obstacles * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    segm_msgs__msg__Obstacles__fini(msg);
    return false;
  }
  // num
  // classes_ids
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->classes_ids, 0)) {
    segm_msgs__msg__Obstacles__fini(msg);
    return false;
  }
  // masks
  if (!segm_msgs__msg__Mask__Sequence__init(&msg->masks, 0)) {
    segm_msgs__msg__Obstacles__fini(msg);
    return false;
  }
  // distances
  if (!rosidl_runtime_c__float__Sequence__init(&msg->distances, 0)) {
    segm_msgs__msg__Obstacles__fini(msg);
    return false;
  }
  return true;
}

void
segm_msgs__msg__Obstacles__fini(segm_msgs__msg__Obstacles * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // num
  // classes_ids
  rosidl_runtime_c__int32__Sequence__fini(&msg->classes_ids);
  // masks
  segm_msgs__msg__Mask__Sequence__fini(&msg->masks);
  // distances
  rosidl_runtime_c__float__Sequence__fini(&msg->distances);
}

bool
segm_msgs__msg__Obstacles__are_equal(const segm_msgs__msg__Obstacles * lhs, const segm_msgs__msg__Obstacles * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // num
  if (lhs->num != rhs->num) {
    return false;
  }
  // classes_ids
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->classes_ids), &(rhs->classes_ids)))
  {
    return false;
  }
  // masks
  if (!segm_msgs__msg__Mask__Sequence__are_equal(
      &(lhs->masks), &(rhs->masks)))
  {
    return false;
  }
  // distances
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->distances), &(rhs->distances)))
  {
    return false;
  }
  return true;
}

bool
segm_msgs__msg__Obstacles__copy(
  const segm_msgs__msg__Obstacles * input,
  segm_msgs__msg__Obstacles * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // num
  output->num = input->num;
  // classes_ids
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->classes_ids), &(output->classes_ids)))
  {
    return false;
  }
  // masks
  if (!segm_msgs__msg__Mask__Sequence__copy(
      &(input->masks), &(output->masks)))
  {
    return false;
  }
  // distances
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->distances), &(output->distances)))
  {
    return false;
  }
  return true;
}

segm_msgs__msg__Obstacles *
segm_msgs__msg__Obstacles__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  segm_msgs__msg__Obstacles * msg = (segm_msgs__msg__Obstacles *)allocator.allocate(sizeof(segm_msgs__msg__Obstacles), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(segm_msgs__msg__Obstacles));
  bool success = segm_msgs__msg__Obstacles__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
segm_msgs__msg__Obstacles__destroy(segm_msgs__msg__Obstacles * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    segm_msgs__msg__Obstacles__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
segm_msgs__msg__Obstacles__Sequence__init(segm_msgs__msg__Obstacles__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  segm_msgs__msg__Obstacles * data = NULL;

  if (size) {
    data = (segm_msgs__msg__Obstacles *)allocator.zero_allocate(size, sizeof(segm_msgs__msg__Obstacles), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = segm_msgs__msg__Obstacles__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        segm_msgs__msg__Obstacles__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
segm_msgs__msg__Obstacles__Sequence__fini(segm_msgs__msg__Obstacles__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      segm_msgs__msg__Obstacles__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

segm_msgs__msg__Obstacles__Sequence *
segm_msgs__msg__Obstacles__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  segm_msgs__msg__Obstacles__Sequence * array = (segm_msgs__msg__Obstacles__Sequence *)allocator.allocate(sizeof(segm_msgs__msg__Obstacles__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = segm_msgs__msg__Obstacles__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
segm_msgs__msg__Obstacles__Sequence__destroy(segm_msgs__msg__Obstacles__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    segm_msgs__msg__Obstacles__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
segm_msgs__msg__Obstacles__Sequence__are_equal(const segm_msgs__msg__Obstacles__Sequence * lhs, const segm_msgs__msg__Obstacles__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!segm_msgs__msg__Obstacles__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
segm_msgs__msg__Obstacles__Sequence__copy(
  const segm_msgs__msg__Obstacles__Sequence * input,
  segm_msgs__msg__Obstacles__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(segm_msgs__msg__Obstacles);
    segm_msgs__msg__Obstacles * data =
      (segm_msgs__msg__Obstacles *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!segm_msgs__msg__Obstacles__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          segm_msgs__msg__Obstacles__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!segm_msgs__msg__Obstacles__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
