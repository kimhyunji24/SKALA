<template>
    <div>
        <h2>🍔 </h2>
        <button @click="eatFood(1)">햄버거 (+1kg)</button>
        <button @click="eatFood(2)">피자 (+2kg)</button>
    </div>
</template>

<script setup>

const emit = defineEmits(['eat'])

function eatFood(amount) {
    emit('eat', amount)
}

</script>