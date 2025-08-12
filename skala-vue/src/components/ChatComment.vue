<template>
  <div class="comment-container">
    <h2>댓글</h2>
    <!-- 댓글 목록 -->
    <ul class="comment-list">
      <li v-if="comments.length === 0" class="no-comments">
        아직 댓글이 없습니다. 첫 댓글을 남겨주세요!
      </li>
      <li v-for="comment in comments" :key="comment.id" class="comment-item">
        {{ comment.text }}
      </li>
    </ul>

    <!-- 댓글 입력 폼 -->
    <div class="comment-form">
      <input
        v-model="newComment"
        @keyup.enter="addComment"
        type="text"
        placeholder="댓글을 입력하세요"
        class="comment-input"
      />
      <button @click="addComment" class="add-button">등록</button> 
      <!-- 키를 눌렀을 때 말고 떼었을 때 적용되는게 사용자 입장에서 더 자연스러움 -->
      <button @click="removeComment" class="remove-button">삭제</button>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// 댓글 목록을 저장할 반응형 배열
// 각 댓글은 고유 id와 텍스트를 가진 객체입니다.
const comments = ref([
  { id: 1, text: 'Vue.js 정말 재미있네요!' },
  { id: 2, text: 'v-for 디렉티브는 정말 강력해요.' },
]);

// 사용자가 입력 중인 새로운 댓글 텍스트
const newComment = ref('');

// 다음 댓글에 할당할 고유 ID 카운터
// 실제 애플리케이션에서는 UUID나 서버에서 받은 ID를 사용하는 것이 더 좋습니다.
let nextCommentId = ref(comments.value.length + 1);

// 댓글을 추가하는 함수
const addComment = () => {
  // 입력값의 앞뒤 공백을 제거
  const trimmedComment = newComment.value.trim();

  // 공백 제거 후 내용이 없으면 함수 종료 (빈 댓글 등록 방지)
  if (!trimmedComment) {
    return;
  }

  // 새로운 댓글 객체를 생성하여 배열의 뒤에 추가
  comments.value.push({
    id: nextCommentId.value++,
    text: trimmedComment,
  });

  // 입력창을 초기화
  newComment.value = '';
};
</script>

<style scoped>
/* 컴포넌트 전체 스타일 */
.comment-container {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  max-width: 600px;
  margin: 40px auto;
  padding: 24px;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

h2 {
  margin-top: 0;
  margin-bottom: 20px;
  color: #333;
  text-align: center;
}

/* 댓글 목록 스타일 */
.comment-list {
  list-style-type: none;
  padding: 0;
  margin-bottom: 24px;
  min-height: 100px;
}

.comment-item {
  background-color: #ffffff;
  padding: 12px 16px;
  border-radius: 8px;
  margin-bottom: 10px;
  border: 1px solid #eee;
  color: #555;
  word-wrap: break-word;
  transition: transform 0.2s ease-in-out;
}

.comment-item:hover {
    transform: translateX(5px);
}

.no-comments {
  text-align: center;
  color: #888;
  padding: 20px;
}

/* 댓글 입력 폼 스타일 */
.comment-form {
  display: flex;
  gap: 10px;
}

.comment-input {
  flex-grow: 1;
  padding: 12px 16px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 16px;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.comment-input:focus {
  outline: none;
  border-color: #42b983;
  box-shadow: 0 0 0 3px rgba(66, 185, 131, 0.2);
}

.add-button {
  padding: 12px 20px;
  border: none;
  background-color: #42b983;
  color: white;
  border-radius: 8px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.1s;
}

.add-button:hover {
  background-color: #36a473;
}

.add-button:active {
  transform: scale(0.98);
}
</style>
