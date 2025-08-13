import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from './pages/LoginPage.vue';
import MainPage from './pages/main.vue';
import AboutPage from './pages/AboutPage.vue';
import SignupPage from './pages/SignupPage.vue';

// 라우트 정의
const routes = [
  {
    path: '/',
    name: 'Login',
    component: LoginPage,
  },
  {
    path: '/main',
    name: 'Main',
    component: MainPage,
    meta: { requiresAuth: true }, // 인증이 필요한 페이지
  },
  {
    path: '/about',
    name: 'About',
    component: AboutPage,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignupPage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// 전역 가드 (인증 체크)
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('isLoggedIn');
  if (to.meta.requiresAuth && !isAuthenticated) {
    // 인증이 필요하지만 로그인되지 않았을 경우, 로그인 페이지로 리디렉션
    next({ name: 'Login' });
  } else {
    next();
  }
});

export default router;
