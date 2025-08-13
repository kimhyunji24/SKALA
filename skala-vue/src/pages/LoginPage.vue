<template>
  <div class="d-flex justify-content-center align-items-center vh-100 bg-light">
    <div class="card p-4 shadow-sm" style="width: 24rem;">
      <h2 class="card-title text-center mb-4">로그인</h2>
      <form @submit.prevent="handleLogin">
        <div class="mb-3">
          <label for="username" class="form-label">아이디</label>
          <input
            type="text"
            class="form-control"
            id="username"
            v-model="username"
            required
          />
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">비밀번호</label>
          <input
            type="password"
            class="form-control"
            id="password"
            v-model="password"
            required
          />
        </div>
        <button type="submit" class="btn btn-primary w-100">로그인</button>
      </form>
      <div class="text-center mt-3">
        <router-link to="/signup" class="btn btn-link">회원가입</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const username = ref('');
const password = ref('');
const router = useRouter();

const handleLogin = () => {
  // 실제 로그인 로직 (예: API 호출)은 여기에 구현
  // 예시를 위해 간단한 로직 사용
  if (username.value === 'test' && password.value === '1234') {
    // 로그인 성공 시, localStorage에 상태 저장
    localStorage.setItem('isLoggedIn', 'true');
    alert('로그인 성공!');
    router.push('/main'); // MainPage로 이동
  } else {
    alert('아이디 또는 비밀번호가 올바르지 않습니다.');
  }
};
</script>

<style scoped>
/* 추가적인 스타일링 */
</style>
