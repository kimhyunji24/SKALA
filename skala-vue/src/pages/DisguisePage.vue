<template>
    <div>
        <h1> 둔갑술 시전!</h1>
        <p>홍길동이 <strong>{{ target }}</strong>(으)로 변신했습니다 !</p>
    </div>
</template>
<script setup>
import { useRoute, useRouter } from 'vue-router'
import { onMounted, ref } from 'vue'

const route = useRoute()
const router = useRouter()
const target = ref('???')

onMounted(() => {
        // 브라우저 URL에서 query 부분 제거
    if (history.state && history.state.target) {
        target.value = history.state.target
    }
})

</script>