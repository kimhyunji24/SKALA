<template>
  <div class="container mt-5">
    <h3>성별</h3>
    <CommonRadio :options="studentGenders" name="gender" v-model="selectedGender" />

    <hr class="my-4">

    <h3>학년</h3>
    <CommonRadio :options="studentGrades" name="grade" v-model="selectedGrade" />
    
    <div class="mt-4">
      <p>선택된 성별: {{ selectedGender }}</p>
      <p>선택된 학년: {{ selectedGrade }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import CommonRadio from './commons/CommonRadio.vue';

const studentGenders = [
  { label: "남학생", value: "남학생" },
  { label: "여학생", value: "여학생" },
];

const studentGrades = [
  { label: "1학년", value: "1학년" },
  { label: "2학년", value: "2학년" },
  { label: "3학년", value: "3학년" },
];

const selectedGender = ref("");
const selectedGrade = ref("");
</script>