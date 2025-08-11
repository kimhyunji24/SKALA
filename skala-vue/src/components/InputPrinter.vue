<template>
    <h1>입력값 출력하기</h1>
    <input type="text" v-model.trim="msg" placeholder="아무 글자를 입력하세요"></input> 
    <!-- v-model 선언 = 양방향 데이터 바인딩 -->
    <p v-text="msg"></p>
    

</template>

<script setup>
import { ref } from 'vue'
const msg = ref("")


</script>
<style scoped></style>