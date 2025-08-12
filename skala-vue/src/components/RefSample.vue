
<template>
<input v-model="name" @keyup.enter="show"/>
<input v-model="age" type="number" @keyup.enter="show"/>
</template>

<script setup>
import { reactive, ref, toRef } from 'vue'

const state = reactive({
    name: '홍길동',
    age: 20
})

// const {name} = state
// const {age} = state //state를 쓰면, 이미 state 변수로 치환되었기 때문에 반응성이 사라짐. 

const { name } = toRef(state, 'name')
const { age } = toRef(state, 'age')
</script>