<template>
    <input id="input" v-model="msg" placeholder="Enter a message">
    <p id="message">Message: {{msg}} </p>
</template>


<script setup>

import { ref } from 'vue'

const msg = ref()

</script>

<style scoped></style>