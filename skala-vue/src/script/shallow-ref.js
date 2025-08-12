import { shallowReactive } from "vue";
export const userRef = shallowReactive({
    name: "홍길동",
    address: {
    city: "서울",
    zip: "12345",
    },
});
export function updateName(newName) {
userRef.name = newName;
}
export function updateCity(newCity) {
userRef.address.city = newCity; 
//value자체만 감지해서 바뀔 때 바뀌기 때문에 화면에 도시 변경버튼을 눌러도 바뀌지않음
}