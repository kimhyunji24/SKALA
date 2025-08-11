<!-- 색상, 사이즈 입력받아서 적용누르면 div박스가 해당 스타일로 변경. -->
<!-- 박스의 기본 스타일은 지정돼있고, 변경되는 속성은 객체형식으로 바인딩 -->
<template>
  <div class="container">
    <h2>스타일 변경하기 🎨</h2>
    <div class="controls">
      <div class="input-group">
        <label for="color-input">색상 (영문):</label>
        <input id="color-input" type="text" v-model="colorInput" placeholder="예: red, blue, green" />
      </div>
      <div class="input-group">
        <label for="size-input">사이즈 (px 단위):</label>
        <input id="size-input" type="number" v-model="sizeInput" placeholder="예: 100" />
      </div>
      <button @click="applyStyles">적용</button>
    </div>

    <div class="box-wrapper">
      <div :style="boxStyle"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

// 사용자가 입력할 값을 저장하는 반응형 데이터
// 초기값을 영문 색상으로 변경
const colorInput = ref('green'); 
const sizeInput = ref(100);

// '적용' 버튼을 눌렀을 때 변경될 스타일 속성을 저장하는 객체
const dynamicStyleObject = ref({
  backgroundColor: 'green',
  width: '100px',
  height: '100px',
});

// '적용' 버튼을 누르면 실행되는 메서드
const applyStyles = () => {
  dynamicStyleObject.value = {
    // 입력된 영문 색상 이름을 그대로 사용
    backgroundColor: colorInput.value,
    // 입력된 숫자에 'px' 단위를 붙여서 사용
    width: `${sizeInput.value}px`,
    height: `${sizeInput.value}px`,
  };
};

// 최종적으로 div에 적용될 스타일을 계산하는 computed 속성
const boxStyle = computed(() => {
  // 1. 박스의 기본 스타일 (변경되지 않음)
  const baseStyle = {
    border: '2px solid #35495e',
    transition: 'all 0.3s ease',
  };

  // 2. 기본 스타일과 동적 스타일 객체를 합쳐서 최종 스타일 반환
  return {
    ...baseStyle,
    ...dynamicStyleObject.value,
  };
});
</script>

<style scoped>
/* 컴포넌트 전체 스타일 */
.container {
  font-family: 'Arial', sans-serif;
  max-width: 400px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-color: #f9f9f9;
}

h2 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 24px;
}

.controls {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-bottom: 25px;
}

.input-group {
  display: flex;
  flex-direction: column;
}

.input-group label {
  margin-bottom: 5px;
  font-weight: bold;
  color: #333;
}

.input-group input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 10px 15px;
  border: none;
  background-color: #42b883;
  color: white;
  font-size: 16px;
  font-weight: bold;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

button:hover {
  background-color: #359d70;
}

.box-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 200px; /* 박스가 커져도 레이아웃이 깨지지 않도록 최소 높이 지정 */
  background-color: #fff;
  border-radius: 8px;
  padding: 20px;
}
</style>