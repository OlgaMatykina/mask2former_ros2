// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from segm_msgs:msg/Mask.idl
// generated code does not contain a copyright notice
#include "segm_msgs/msg/detail/mask__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `mask`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
segm_msgs__msg__Mask__init(segm_msgs__msg__Mask * msg)
{
  if (!msg) {
    return false;
  }
  // mask
  if (!rosidl_runtime_c__uint8__Sequence__init(&msg->mask, 0)) {
    segm_msgs__msg__Mask__fini(msg);
    return false;
  }
  return true;
}

void
segm_msgs__msg__Mask__fini(segm_msgs__msg__Mask * msg)
{
  if (!msg) {
    return;
  }
  // mask
  rosidl_runtime_c__uint8__Sequence__fini(&msg->mask);
}

bool
segm_msgs__msg__Mask__are_equal(const segm_msgs__msg__Mask * lhs, const segm_msgs__msg__Mask * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // mask
  if (!rosidl_runtime_c__uint8__Sequence__are_equal(
      &(lhs->mask), &(rhs->mask)))
  {
    return false;
  }
  return true;
}

bool
segm_msgs__msg__Mask__copy(
  const segm_msgs__msg__Mask * input,
  segm_msgs__msg__Mask * output)
{
  if (!input || !output) {
    return false;
  }
  // mask
  if (!rosidl_runtime_c__uint8__Sequence__copy(
      &(input->mask), &(output->mask)))
  {
    return false;
  }
  return true;
}

segm_msgs__msg__Mask *
segm_msgs__msg__Mask__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  segm_msgs__msg__Mask * msg = (segm_msgs__msg__Mask *)allocator.allocate(sizeof(segm_msgs__msg__Mask), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(segm_msgs__msg__Mask));
  bool success = segm_msgs__msg__Mask__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
segm_msgs__msg__Mask__destroy(segm_msgs__msg__Mask * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    segm_msgs__msg__Mask__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
segm_msgs__msg__Mask__Sequence__init(segm_msgs__msg__Mask__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  segm_msgs__msg__Mask * data = NULL;

  if (size) {
    data = (segm_msgs__msg__Mask *)allocator.zero_allocate(size, sizeof(segm_msgs__msg__Mask), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = segm_msgs__msg__Mask__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        segm_msgs__msg__Mask__fini(&data[i - 1]);
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
segm_msgs__msg__Mask__Sequence__fini(segm_msgs__msg__Mask__Sequence * array)
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
      segm_msgs__msg__Mask__fini(&array->data[i]);
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

segm_msgs__msg__Mask__Sequence *
segm_msgs__msg__Mask__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  segm_msgs__msg__Mask__Sequence * array = (segm_msgs__msg__Mask__Sequence *)allocator.allocate(sizeof(segm_msgs__msg__Mask__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = segm_msgs__msg__Mask__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
segm_msgs__msg__Mask__Sequence__destroy(segm_msgs__msg__Mask__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    segm_msgs__msg__Mask__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
segm_msgs__msg__Mask__Sequence__are_equal(const segm_msgs__msg__Mask__Sequence * lhs, const segm_msgs__msg__Mask__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!segm_msgs__msg__Mask__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
segm_msgs__msg__Mask__Sequence__copy(
  const segm_msgs__msg__Mask__Sequence * input,
  segm_msgs__msg__Mask__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(segm_msgs__msg__Mask);
    segm_msgs__msg__Mask * data =
      (segm_msgs__msg__Mask *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!segm_msgs__msg__Mask__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          segm_msgs__msg__Mask__fini(&data[i]);
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
    if (!segm_msgs__msg__Mask__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
