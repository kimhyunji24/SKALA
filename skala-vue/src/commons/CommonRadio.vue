<template>
  <div v-for="(option, index) in options" :key="index" class="form-check">
    <input 
      class="form-check-input" 
      type="radio" 
      :name="name"  
      :id="`${name}-${index}`" 
      :value="option.value" 
      :disabled="option.disabled"
      :checked="modelValue === option.value"
      @change="handleChange(option.label, option.value)"
    >
    <label class="form-check-label" :for="`${name}-${index}`">
      {{ option.label }}
    </label>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  options: {
    type: Array,
    required: true,
  },
  name: {
    type: String,
    required: true, // name 속성을 필수로 지정
  },
  modelValue: {
    type: [String, Number, Boolean],
    default: null,
  }
});

const emit = defineEmits(['update:modelValue', 'changed']);

const handleChange = (label, value) => {
  emit('update:modelValue', value);
  emit('changed', { label, value });
};
</script>