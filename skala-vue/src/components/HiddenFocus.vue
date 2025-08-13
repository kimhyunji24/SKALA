<template>
    <h1>
        <slot></slot> 
        <!-- slot tag로 app.vue에서 생성됨  -->
    </h1>
    <div>
        <button @click="showInputBox">입력창 열기</button>
        <div v-if="isVisible">
            <input ref="inputRef" placeholder="이름 입력" />
        </div>
    </div>
</template>

<script setup>
import { nextTick, ref } from 'vue'

const isVisible = ref(false)
const inputRef = ref(null)

async function showInputBox() {
    isVisible.value = true
    await nextTick() //async와 await는 세트 | 화면이 새로 갱신됐을 때 기다렸다가 실행.
    inputRef.value?.focus()
}

</script>
