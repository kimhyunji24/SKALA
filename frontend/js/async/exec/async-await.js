const drawButton = document.getElementById('drawButton');
const messageDiv = document.getElementById('message');

function drawLottery() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const isWinner = Math.random() < 0.5; // 50% 확률
            isWinner ? resolve("당첨 되었습니다.") : reject("꽝! 다음 기회에...");
        }, 3000);
    });
}

drawButton.addEventListener('click', async () => {
    messageDiv.textContent = "1초 후에 당첨 결과가 발표됩니다.";
    messageDiv.className = 'message'; // 초기화
    // drawButton.disabled = true; // 버튼 비활성화
    console.log("당첨 시작...");
    try {
        const result = await drawLottery();
        messageDiv.textContent = result;
        messageDiv.classList.add('success'); // 파란색
    } catch (error) {
        messageDiv.textContent = error;
        messageDiv.classList.add('failure'); // 빨간색
    }
    // drawButton.disabled = false; // 버튼 활성화
});
