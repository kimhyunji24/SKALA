<template>
    <ChildComponent :items="items">
        <!-- 스코프 슬롯을 통해 각 item을 렌더링 -->
        <template #item="{ item }">
        <li>{{ item.name }}</li>
</template>
</ChildComponent>
</template>
<script setup>
import ChildComponent from './slotchild.vue';
//부모 컴포넌트에서 데이터를 선언
const items = [
    { id: 1, name: 'Apple' },
    { id: 2, name: 'Banana' },
    { id: 3, name: 'Cherry' }
];
</script>