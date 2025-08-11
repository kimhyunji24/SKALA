<template>
    <div>
        <button @click="toggleLogin">Toggle Login</button>
        <p v-if="isLoggedIn" id="login-true">Welcome back!</p>
        <p v-else id="login-false">Please log in.</p>
    </div>
</template>

<script setup>
import { ref } from 'vue';
const isLoggedIn = ref(false); //변수

const toggleLogin = () => {
    isLoggedIn.value = !isLoggedIn.value;
    };
</script>