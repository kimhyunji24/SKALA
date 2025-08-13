<template>
  <div class="container mt-5">
    <div class="card p-4 shadow-sm">
      <h2 class="text-center">메인 페이지</h2>
      <p class="text-center lead">로그인에 성공했습니다!</p>
      <div class="d-grid gap-2 col-6 mx-auto">
        <button @click="handleLogout" class="btn btn-danger">로그아웃</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const handleLogout = () => {
  localStorage.removeItem('isLoggedIn');
  alert('로그아웃 되었습니다.');
  router.push('/'); // 로그인 페이지로 이동
};
</script>

<style scoped>
/* 추가적인 스타일링 */
</style>
