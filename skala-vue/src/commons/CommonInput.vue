<template>
  <div class="mb-3">
    <label :for="id" class="form-label" :class="sizeClass">
      {{ label }}
    </label>
    <input
      :id="id"
      :type="type"
      class="form-control"
      :class="sizeClass"
      :placeholder="placeholder"
      @keyup.enter="$emit('enter')"
    >
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  label: {
    type: String,
    required: true,
  },
  type: {
    type: String,
    default: 'text',
  },
  placeholder: {
    type: String,
    default: '',
  },
  size: {
    type: String,
    validator: (value) => ['sm', 'lg', ''].includes(value),
    default: '',
  },
});

const id = `input-${Math.random().toString(36).substring(2, 9)}`;

const sizeClass = computed(() => {
  if (props.size === 'lg') {
    return 'form-control-lg';
  } else if (props.size === 'sm') {
    return 'form-control-sm';
  }
  return '';
});

const emit = defineEmits(['enter']);
</script>

<style scoped></style>