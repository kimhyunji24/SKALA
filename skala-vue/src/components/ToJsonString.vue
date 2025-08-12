<script setup>
import { ref, reactive } from 'vue'
function toJsonString(value) {
    if (value && typeof value === 'object') {
        if ('value' in value && (value.__v_isRef === true || value.__v_isShallow === true)) {
            value = value.value
        }
    }
    return JSON.stringify(value, null, 2)
}
const primitive = 123
const obj = { name: "홍길동", age : 30}
const arr = [1, 2, 3]
const r1 = ref({ city: '서울'})
const r2 = reactive({ job: '개발자'})

const results = []
results.push(toJsonString(primitive))
results.push(toJsonString(obj))
results.push(toJsonString(arr))
results.push(toJsonString(r1))
results.push(toJsonString(r2))

console.log(toJsonString(num), toJsonString(obj), toJsonString(arr), toJsonString(r1), toJsonString(r2))
</script>