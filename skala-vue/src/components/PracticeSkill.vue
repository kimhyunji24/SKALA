<template>
    <div>
        <h2>🏃 </h2>
        <button @click="practice(1)"> 걷기(-1kg)</button>
        <button @click="practice(2)"> 달리기(-2kg)</button>
    </div>
</template>

<script setup>

const emit = defineEmits(['practice'])

function practice(amount) {
    emit('practice', amount)
}

</script>