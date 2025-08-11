
<!-- 비어있어도, Template은 무조건 있어야 함. -->

<template>
    <h2>클래스 바인더</h2>
    <!-- class -->
    <div class="primary":class="{ bigText: isBig }">
        클래스 방식 : 글자크기가 커지거나 작아집니다.
    </div>
    <!-- style -->
    <div :style="{ fontSize: isBig ? '24px' : '14px' }">
        스타일 방식: 글자크기가 커지거나 작아집니다.
    </div>
</template>
<script setup>
import { ref } from 'vue'
const isBig = ref(true)
</script>

<style>
.bigText {
    font-size: 24px;
    }
.primary {
    background-color: yellow;
    font-size: 16px;
}
</style>