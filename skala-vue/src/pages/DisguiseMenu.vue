<template>
<div>
<h1>⚙️ 둔갑술 선택 메뉴</h1>
<button @click="goToDisguise('호랑이')"> 호랑이로 둔갑</button>
<button @click="goToDisguise('도깨비')">도깨비로 둔갑</button>
</div>
</template>
<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

function goToDisguise(target) {
// “/disguise?target="호랑이" 형태로 변환. 그리고 주소창서는 target값 숨기기
  // `path`와 `query`를 사용하여 주소창에 `?target=호랑이`와 같은 쿼리 파라미터를 추가합니다.
    router.push({
        path: '/disguise',
        state: { target: target }
    });
}
</script>