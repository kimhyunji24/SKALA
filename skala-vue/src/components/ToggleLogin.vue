<template>
    <div>
        <button @click="toggleLogin">Toggle Login</button>
        <template v-if="isLoggedIn">
            <!-- if-else가 같은 레벨이라 붙어있어서 한번에 불가능해서 template으로 묶어서 처리.-->
            <p id="login-true">Welcome back!</p>
            <a href="https://google.com" target="_blank">구글 이동</a>
            <p>showshowshow</p>
        </template>
        <template v-else >
            <p id="login-false">Please log in.</p>
        </template>
    </div>
</template>

<script setup>
import { ref } from 'vue';
const isLoggedIn = ref(false); //변수

const toggleLogin = () => {
    isLoggedIn.value = !isLoggedIn.value;
    };
</script>