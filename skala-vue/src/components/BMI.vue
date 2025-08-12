<template>
  <div>
    <h1>BMI 계산기</h1>

    <div>
      <label>키 (cm): 
            <input type="number" v-model.number="height" />

      </label>
    </div>

    <div>
      <label>체중 (kg): 
            <input type="number" v-model.number="weight" />
      </label>
      <p>{{ bmiIndex }} : {{ bmiMessage }}</p>
    </div>

    <div v-if="bmi > 0">
      <hr />
      <p>BMI 지수: {{ bmi.toFixed(2) }}</p>
      <p>판정: {{ bmiStatus }}</p>
      <p v-if="warningMessage">{{ warningMessage }}</p>
    </div>
  </div>
</template>

<script setup>

import { ref, computed, watch , onMounted, onBeforeUnmount} from 'vue';
// 입력값을 위한 반응형 변수
const height = ref(0);
const weight = ref(0);
const warningMessage = ref('');

// 키와 체중이 변경될 때마다 BMI를 다시 계산
const bmiIndex = computed(()  => {
  if (height.value > 0 && weight.value > 0) {
    const heightInMeters = (height.value / 100);
    return weight.value / (heightInMeters * heightInMeters);
  }
  return 0;
});

// BMI 값에 따라 상태를 결정
const bmiStatus = computed(() => {
  if (bmiIndex.value < 18.5) return '저체중';
  if (bmiIndex.value < 23) return '정상';
  if (bmiIndex.value < 25) return '과체중';
  return '비만';
});

// bmiStatus 값이 변경될 때마다 감지하여 특정 조건일 때 메시지 표시
watch(bmiStatus, (newStatus) => {
  if (newStatus === '과체중' || newStatus === '비만') {
    warningMessage.value = '→ 다이어트 하세요';
  } else {
    warningMessage.value = '';
  }
});

onMounted(() => {
  console.log('컴포넌트가 마운트 되었습니다.')
})
onBeforeUnmount(() => {
  console.log('컴포넌트가 제거되기 직전입니다.')
})
</script>