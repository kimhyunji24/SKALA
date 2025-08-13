<template>
    <ul>
        <!-- 부모로부터 전달받은 items 데이터를 기반으로 슬롯을 렌더링 -->
        <slot name="item" v-for="item in items" :item="item" :key="item.id"></slot>
    </ul>
</template>
<script setup>
import { defineProps } from 'vue';
    // 부모로부터 items 데이터를 props로 전달받음
defineProps({
    items: {
        type: Array,
        required: true
    }
});
</script>