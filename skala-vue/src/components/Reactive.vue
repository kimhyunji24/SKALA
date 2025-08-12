<script setup>
import { reactive , ref} from 'vue'

const user = reactive({name : '홍길동', age : 20})
// const user = ref({name : '홍길동', age : 20})
// const fruits = ref(['사과','배'])

const fruits = reactive(['사과','배'])

function increaseAge(){
    user.age++
}
function addFruit(){
    fruits.value.push('귤')
}
</script>

<template>
    <div>
        <p> 이름: <input v-model="user.name" /></p>
        <p> 나이 : {{ user.age }} <button @click="user.age++"> 한살 더 </button></p>
        <p> 과일목록 : {{ fruits.join(', ') }}</p>
        <button @click="fruits.push('귤')"> 과일 추가 </button>
    </div>
</template>
