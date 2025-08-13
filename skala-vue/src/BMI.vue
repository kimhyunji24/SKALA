<template>
    <!-- <input id="input" v-model="msg" placeholder="Enter a message">
    <p id="message">Message: {{msg}} </p> -->


    <!-- <InputPrinter></InputPrinter>
    <ClassBinder></ClassBinder>

    <StyleChanger></StyleChanger> -->
    <!-- <ConditionalElement></ConditionalElement> -->
    <!-- <ChatComment></ChatComment> -->
    <!-- <Reactive></Reactive> -->
    <!-- <ShallowSample></ShallowSample> -->
    <!-- <RefSample></RefSample> -->
    <!-- <ToJsonString></ToJsonString> -->
    <!-- <WatchSample></WatchSample> -->
    <!-- <BMI></BMI>  -->

    <!-- <label> 부모 메시지 :
        <input type="text" v-model="message"></input>
    </label>
    <button @click="sendMessage">전달</button>  -->
        <!-- sendMessage라는 이벤트 전달 -->
    <!-- <hr />
    <TeensChild ref="childRef" :parentMessage="messageToChild" @response="recvResponse"/>
    <hr />
    <div>
        자식의 응답 : {{ responseFromChild }}
    </div> -->
    <div>
        <h1> BMI </h1>
        <p> 현재 체중 : {{ weight }}kg</p>
        <p> 현재 키: {{ height }}cm</p>
        <p>BMI: {{ bmi }} ({{ bmiStatus }})</p>
        <EatFood @eat="gainWeight" />
        <PracticeSkill @practice="loseWeight" />
    </div>



</template>



<script setup>
import ChatComment from './components/ChatComment.vue';
import ClassBinder from './components/ClassBinder.vue';
import InputPrinter from './components/InputPrinter.vue';
import StyleChanger from './components/StyleChanger.vue';
import ConditionalElement from './components/ToggleLogin.vue'
import Reactive from './components/Reactive.vue'
import ShallowSample from './components/ShallowSample.vue';
import RefSample from './components/RefSample.vue';
import ToJsonString from './components/ToJsonString.vue';
import WatchSample from './components/WatchSample.vue';
import BMI from './components/BMI.vue';
import TeensChild from './components/TeensChild.vue';


// const message = ref('')
// const messageToChild = ref('')
// const responseFromChild = ref('')
// const childRef = ref()

// function sendMessage(){
//     messageToChild.value = message.value
//     childRef.value?.letMeKnow("확인 필요")
// }

// function recvResponse(yesno) {
//     responseFromChild.value = yesno
// }



import { ref, computed } from 'vue'
import EatFood from './components/EatFood.vue'
import PracticeSkill from './components/PracticeSkill.vue'

const height = 175 // cm
const weight = ref(60)

const bmi = computed(() => {
    const h = height / 100
    return Math.floor(weight.value / (h * h))
})
const bmiStatus = computed(() => {
        if (bmi.value < 18.5) return '저체중'
        if (bmi.value < 23) return '정상'
        if (bmi.value < 25) return '과체중'
    return '비만'   
})

function gainWeight(amount) {
weight.value += amount
}

function loseWeight(amount) {
weight.value -= amount
}
w

</script>

<style scoped></style>