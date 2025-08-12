<template>
    <div>메시지 : {{ props.parentMessage }}</div>
    <button @click="sayYes">감사합니다</button>
    <button @click="sayNo">싫어요ㅜ</button>
</template>

<script setup>
import { watchEffect } from 'vue'


const props = defineProps({
    parentMessage : String
})


watchEffect(() => {
    console.log(props.parentMessage) //값이 변해야 전달이 됨.
})


const emit = defineEmits(['response']) 

function letMeKnow(msg){
    console.log("letMeKnow", msg)
}
defineExpose({
    letMeKnow
})

function sayYes(){
    emit('response', "Yes")
    console.log("ㄱㅅ")
}

function sayNo(){
    emit("response",'no')
    console.log("ㄴㄴ")
}
</script>
