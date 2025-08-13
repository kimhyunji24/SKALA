<template>
  <div class="d-flex justify-content-center align-items-center vh-100 bg-light">
    <div class="card p-4 shadow-sm" style="width: 24rem;">
      <h2 class="card-title text-center mb-4">회원가입</h2>
      <form @submit.prevent="handleSignup">
        <div class="mb-3">
          <label for="newUsername" class="form-label">아이디</label>
          <input
            type="text"
            class="form-control"
            id="newUsername"
            v-model="newUsername"
            required
          />
        </div>
        <div class="mb-3">
          <label for="newPassword" class="form-label">비밀번호</label>
          <input
            type="password"
            class="form-control"
            id="newPassword"
            v-model="newPassword"
            required
          />
        </div>
        <button type="submit" class="btn btn-success w-100">가입하기</button>
      </form>
      <div class="text-center mt-3">
        <router-link to="/" class="btn btn-link">로그인 페이지로 돌아가기</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const newUsername = ref('');
const newPassword = ref('');
const router = useRouter();

const handleSignup = () => {
  // 실제 회원가입 로직 (예: API 호출)은 여기에 구현
  alert(`회원가입 성공! 아이디: ${newUsername.value}`);
  router.push('/'); // 로그인 페이지로 이동
};
</script>

<style scoped>
/* 추가적인 스타일링 */
</style>
