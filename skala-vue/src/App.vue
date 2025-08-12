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
    <label> 부모 메시지 :
        <input type="text" v-model="message"></input>
    </label>
    <button @click="sendMessage">전달</button> 
    <!-- sendMessage라는 이벤트 전달 -->
    <hr />
    <TeensChild ref="childRef" :parentMessage="messageToChild" @response="recvResponse"/>
    <hr />
    <div>
        자식의 응답 : {{ responseFromChild }}
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

import {ref} from "vue"

const message = ref('')
const messageToChild = ref('')
const responseFromChild = ref('')
const childRef = ref()

function sendMessage(){
    messageToChild.value = message.value
    childRef.value?.letMeKnow("확인 필요")
}

function recvResponse(yesno) {
    responseFromChild.value = yesno
}
</script>

<style scoped></style>