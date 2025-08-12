<template>
    <label> 카운트
        <input type="number" v-modle="obj.count"></input>
    </label>

    <label> 이름
        <input type="text" v-modle="obj.name"input>
    </label>

    <p> {{ message }}</p>
</template>

<script setup>
import {ref, watch, reactive} from "vue"

const count = ref(0)
const message = ref('')

const name = ref('')
const obj = reactive({
    count:0,
    name:'홍길동'
})

watch([count, name], (newValue, oldValue) => {
    console.log(newValue, oldValue)
    message.value = "카운트  : ${newValue[0]}, 이름 : ${newValue[1]}"
})
watch(count, watchCount)


</script>
